from fastapi import FastAPI
from src.predict import predict_price  

app = FastAPI()

app.get('/')
def home():
    return{'message':'House Price Prediction API Running'}

@app.get('/predict')
def predict(total_sqft:float, bath:int, balcony:int, bhk:int, location:str):
    price = predict_price(total_sqft,bath,balcony,bhk,location)

    return{
        "predicted_price": float(round(price,2))
    }