
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI()

model = joblib.load("ltv_model.pkl")
columns = joblib.load("model_columns.pkl")

class CustomerData(BaseModel):
    tenure: int
    MonthlyCharges: float

@app.get("/")
def home():
    return {
        "message":"Customer LTV Prediction API Running Successfully"
    }

@app.post("/predict")
def predict(data: CustomerData):

    input_df = pd.DataFrame([data.model_dump()])

    for col in columns:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[columns]

    prediction = model.predict(input_df)

    return {
        "Predicted_LTV": float(prediction[0])
    }
