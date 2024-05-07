from flask import jsonify

from app import services
from app.utils import map_dr_severity


class PredictionController:
    def __init__(self):
        pass

    def predict_dr_stage(self, file):
        if file is None or file.filename == '':
            return 'File not found', 400

        try:
            result = services.process_image_for_prediction(file)

            # Return the prediction result
            response = jsonify({"stage": result, "severity": map_dr_severity(result)})
            return response, 200

        except Exception as e:
            print(f"Prediction error: {e}")
            return 'Something went wrong during prediction', 500
