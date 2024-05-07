from flask import request

from app import app
from app.controllers import PredictionController

prediction_controller = PredictionController()


@app.route('/api/predict-dr-stage', methods=['POST'])
def test_dr_image():
    return prediction_controller.predict_dr_stage(request.files['file'])
