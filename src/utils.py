from src.exception import CustomException
import pickle
import sys
import tensorflow as tf


def save_object(obj, file_path: str):
    """Save an object using pickle."""
    try:
        with open(file_path, 'wb') as file:
            pickle.dump(obj, file)
    except Exception as e:
        raise CustomException(f"Error saving object: {e}", sys)

def load_object(file_path: str):
    """Load an object from a file using pickle or TensorFlow (for .h5 models)."""
    try:
        if file_path.endswith(".h5"):
            return tf.keras.models.load_model(file_path)  # Load TensorFlow model
        else:
            with open(file_path, 'rb') as file:
                return pickle.load(file)
    except Exception as e:
        raise CustomException(f"Error loading object: {e}", sys)
