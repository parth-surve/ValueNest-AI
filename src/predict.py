from src.utils import load_model, load_columns
from src.data_preprocessing import preprocess_input
import numpy as np

model = load_model()
columns = load_columns()

def predict_price(total_sqft, bath, balcony, bhk, location):
    x = preprocess_input(total_sqft, bath, balcony, bhk, location, columns)
    prediction = model.predict([x])[0]

    return np.exp(prediction)