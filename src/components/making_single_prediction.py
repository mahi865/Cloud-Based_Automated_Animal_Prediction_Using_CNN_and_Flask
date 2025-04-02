import numpy as np
from tensorflow.keras.preprocessing import image
from building_cnn import cnn

# Making a single prediction
test_image = image.load_img('dataset/single_prediction/cat_or_dog_1.jpg', target_size=(64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis=0)
result = cnn.predict(test_image)
training_set_class_indices = {'cats': 0, 'dogs': 1}

if result[0][0] == 1:
    prediction = 'dog'
else:
    prediction = 'cat'

print(prediction)