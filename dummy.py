import tensorflow as tf
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

# Assuming you have training data loaded in training_set and test_set
# model.fit(training_set, epochs=25, validation_data=test_set)

# Save the model to the artifacts directory
model.save('artifacts/model.h5')


import pickle
from sklearn.preprocessing import StandardScaler
import os

# Ensure the artifacts directory exists
if not os.path.exists('artifacts'):
    os.makedirs('artifacts')

# Create your preprocessor
preprocessor = StandardScaler()
# Assuming you have training data loaded in training_data
# preprocessor.fit(training_data)

# Save the preprocessor to the artifacts directory
with open('artifacts/preprocessor.pkl', 'wb') as file:
    pickle.dump(preprocessor, file)