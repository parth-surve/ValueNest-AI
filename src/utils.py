import joblib
import json
from src.config  import MODEL_PATH, COLUMNS_PATH

def load_model():
    return joblib.load(MODEL_PATH)

def load_columns():
    with open(COLUMNS_PATH,'r') as f:
        return json.load(f)