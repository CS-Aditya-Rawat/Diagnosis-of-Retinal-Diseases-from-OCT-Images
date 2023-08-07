import cv2
import numpy as np
from keras.models import load_model
from keras import backend as k

def OCTPrediction(image):
    """
    This function includes entire pipeline, from data preprocessing to making final predictions.
    Input: Image
    Output: Predictions for the input
    """
    model = load_model("DenseNet121.hdf5")
    image = cv2.resize(image, (224, 224))
    image = image / 255.0
    image = np.expand_dims(image, axis=0) 
    pred = model.predict(image)

    class_labels = ["CNV", "DME", "DRUSEN", "NORMAL"]
    predicted_index = np.argmax(pred, axis=1)
    predicted_class_label = class_labels[predicted_index[0]]
    k.clear_session()
    return predicted_class_label