# main.py
from fastapi import FastAPI
from pydantic import BaseModel
import xgboost as xgb
import numpy as np
import joblib
import pandas as pd

# FastAPI create instance
app = FastAPI()

# Define the schema for the input data 
class InputData(BaseModel):
    Global_reactive_power: float
    Voltage: float
    Global_intensity: float
    Sub_metering_1: float
    Sub_metering_2: float
    Sub_metering_3: float
    Year: int
    Month: int
    Day: int
    Dayofweek: int
    Lag1: float
    Lag7: float
    Rolling_Mean_7: float

# Load the model
model = joblib.load("xgb_model.pkl")

# Define the prediction endpoint
@app.post("/predict")
# Predict function to handle the input data and return the prediction
def predict(data: InputData):
    # Transform the input data into a DataFrame
    df = pd.DataFrame([data.dict()])
    #predict
    prediction = model.predict(df)
    return {'prediction': prediction.tolist()[0]}