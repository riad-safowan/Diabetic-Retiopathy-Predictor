import torch
import torchvision.transforms as transforms
from PIL import Image


def process_image_for_prediction(file):
    mymodel = torch.load('./dr_model.pth')
    mymodel.eval()

    # Transformations for preprocessing the image
    transform = transforms.Compose([
        transforms.Resize((256, 256)),  # Resize image to match model input size
        transforms.ToTensor(),  # Convert image to tensor
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])  # Normalize image
    ])

    # Load the image from file
    image = Image.open(file)

    # Preprocess the image
    input_image = transform(image).unsqueeze(0)  # Add batch dimension

    # Pass the preprocessed image through the model
    with torch.no_grad():
        output = mymodel(input_image)

    # Interpret the output to get predictions
    predicted_class = torch.argmax(output, dim=1).item()

    print("Predicted Class:", predicted_class)
    return predicted_class
