import sys
import os
import numpy as np
import pandas as pd
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model  # Import the correct function for loading the model
from src.exception import CustomException
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        try:
            self.model_path = os.path.join("artifacts", "model.h5")
            self.preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")
            self.model = load_model(self.model_path)  # Use load_model instead of load_object
            self.preprocessor = load_object(file_path=self.preprocessor_path)
        except Exception as e:
            raise CustomException(e, sys)

    def predict(self, image_path: str):
        try:
            data = CustomData(image_path)
            test_image = data.get_data_as_image()
            test_image = np.expand_dims(test_image, axis=0)
            data_scaled = self.preprocessor.transform(test_image.reshape(1, -1))  # Flatten the image for the scaler
            preds = self.model.predict(data_scaled)
            return "dog" if preds[0][0] == 1 else "cat"
        except Exception as e:
            raise CustomException(e, sys)


class CustomData:
    def __init__(self, image_path: str):
        self.image_path = image_path

    def get_data_as_image(self):
        try:
            img = image.load_img(self.image_path, target_size=(64, 64))
            img = image.img_to_array(img)
            return img
        except Exception as e:
            raise CustomException(e, sys)