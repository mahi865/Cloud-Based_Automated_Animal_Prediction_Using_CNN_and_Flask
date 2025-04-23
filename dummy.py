import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.preprocessing import StandardScaler
import os
import pickle
import numpy as np

# Ensure the artifacts directory exists
if not os.path.exists('artifacts'):
    os.makedirs('artifacts')

# Define the paths for your dataset
dataset_dir = "dataset"
training_set_dir = os.path.join(dataset_dir, "training_set")
test_set_dir = os.path.join(dataset_dir, "test_set")

# Data Preprocessing: Training and Test Set
train_datagen = ImageDataGenerator(
    rescale=1.0 / 255,  # Normalize pixel values to [0, 1]
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True
)

test_datagen = ImageDataGenerator(rescale=1.0 / 255)

training_set = train_datagen.flow_from_directory(
    training_set_dir,
    target_size=(64, 64),  # Match input shape of the CNN
    batch_size=32,
    class_mode="binary"
)

test_set = test_datagen.flow_from_directory(
    test_set_dir,
    target_size=(64, 64),
    batch_size=32,
    class_mode="binary"
)

# Define and Compile the Model
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation="relu", input_shape=(64, 64, 3)),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(32, (3, 3), activation="relu"),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation="relu"),
    tf.keras.layers.Dense(1, activation="sigmoid")  # Binary classification
])

model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

# Train the Model
model.fit(
    training_set,
    validation_data=test_set,
    epochs=1  # Use 1 epoch for testing; increase for real training
)

# Save the Model
model.save("artifacts/model.h5")

# Create and Save the Preprocessor
# We extract all training data to create a StandardScaler
X_train = []
for _ in range(len(training_set)):
    batch = training_set.next()
    X_train.append(batch[0])  # Collect the image data (not labels)

X_train = np.vstack(X_train)  # Stack all batches into a single array
X_train_flattened = X_train.reshape(X_train.shape[0], -1)  # Flatten images

preprocessor = StandardScaler()
preprocessor.fit(X_train_flattened)

# Save the preprocessor to a pickle file
with open("artifacts/preprocessor.pkl", "wb") as file:
    pickle.dump(preprocessor, file)

print("Artifacts created successfully: model.h5 and preprocessor.pkl")