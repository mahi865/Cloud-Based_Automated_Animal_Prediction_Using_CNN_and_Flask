import tensorflow as tf
import pickle
from sklearn.preprocessing import StandardScaler
import os

# Ensure the artifacts directory exists
if not os.path.exists('artifacts'):
    os.makedirs('artifacts')

# Define and compile your model
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3)),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Dummy training data
import numpy as np
X_train = np.random.rand(100, 64, 64, 3)
y_train = np.random.randint(2, size=(100, 1))

# Train the model with dummy data (for demonstration purposes)
model.fit(X_train, y_train, epochs=1)

# Save the model to the artifacts directory
model.save('artifacts/model.h5')

# Create and fit the preprocessor
preprocessor = StandardScaler()
preprocessor.fit(X_train.reshape(100, -1))  # Flatten the images for the scaler

# Save the preprocessor to the artifacts directory
with open('artifacts/preprocessor.pkl', 'wb') as file:
    pickle.dump(preprocessor, file)