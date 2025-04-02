import os
import sys
import tensorflow as tf
from src.exception import CustomException
from src.utils import save_object
from data_preprocessing import training_set, test_set

class TrainPipeline:
    def __init__(self):
        try:
            self.model_save_path = os.path.join("artifacts", "model.h5")
            self.preprocessor_save_path = os.path.join("artifacts", "preprocessor.pkl")
            self.cnn = self.build_cnn()
        except Exception as e:
            raise CustomException(e, sys)

    def build_cnn(self):
        try:
            cnn = tf.keras.models.Sequential()

            # Step 1 - Convolution
            cnn.add(tf.keras.layers.Conv2D(filters=32, kernel_size=3, activation='relu', input_shape=[64, 64, 3]))

            # Step 2 - Pooling
            cnn.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))

            # Adding a second convolutional layer
            cnn.add(tf.keras.layers.Conv2D(filters=32, kernel_size=3, activation='relu'))
            cnn.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))

            # Step 3 - Flattening
            cnn.add(tf.keras.layers.Flatten())

            # Step 4 - Full Connection
            cnn.add(tf.keras.layers.Dense(units=128, activation='relu'))

            # Step 5 - Output Layer
            cnn.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))

            return cnn
        except Exception as e:
            raise CustomException(e, sys)

    def train(self):
        try:
            # Compiling the CNN
            self.cnn.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

            # Training the CNN on the Training set and evaluating it on the Test set
            self.cnn.fit(x=training_set, validation_data=test_set, epochs=25)

            # Save the model and preprocessor
            save_object(self.cnn, self.model_save_path)
            save_object(training_set.image_data_generator, self.preprocessor_save_path)
        except Exception as e:
            raise CustomException(e, sys)

if __name__ == "__main__":
    train_pipeline = TrainPipeline()
    train_pipeline.train()