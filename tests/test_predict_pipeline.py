import pytest
from src.pipeline.predict_pipeline import PredictPipeline
import os

def test_predict_pipeline():
    print("Current Working Directory:", os.getcwd())  # Debugging
    pipeline = PredictPipeline()
    # Use a relative path
    result = pipeline.predict("dataset/test_set/dogs/dog.4001.jpg")
    print(f"Prediction Result: {result}")  # Print the result
    assert result in ["cat", "dog"], "Prediction must be either 'cat' or 'dog'"