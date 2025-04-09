import pytest
from src.pipeline.predict_pipeline import PredictPipeline

def test_predict_pipeline():
    pipeline = PredictPipeline()
    # Use absolute path for the test image
    result = pipeline.predict("C:/Users/mahid/Downloads/S37 - dataset/dataset/test_set/dogs/dog.4015.jpg")
    print(f"Prediction Result: {result}")  # Print the result
    assert result in ["cat", "dog"], "Prediction must be either 'cat' or 'dog'"