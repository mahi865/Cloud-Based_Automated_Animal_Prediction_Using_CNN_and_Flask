import pytest
from src.pipeline.predict_pipeline import PredictPipeline

def test_predict_pipeline():
    pipeline = PredictPipeline()
    # Replace 'path_to_test_image.jpg' with the path to a sample test image
    result = pipeline.predict("dataset\\test_set\\dogs\\dog.4015.jpg")
    print(f"Prediction Result: {result}")  # Print the result
    assert result in ["cat", "dog"], "Prediction must be either 'cat' or 'dog'"