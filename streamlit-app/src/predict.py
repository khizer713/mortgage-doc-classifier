from tensorflow.keras.models import load_model
import numpy as np
from .preprocess import preprocess_image


def classify_image(image_path, model_path):
    model = load_model(model_path)
    image = preprocess_image(image_path)
    image = np.expand_dims(image, axis=0)
    prediction = model.predict(image)
    return prediction
