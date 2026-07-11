
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib


app = FastAPI(
    title="Customer LTV Prediction API"
)


model = joblib.load("ltv_model.pkl")

model_columns = joblib.load("model_columns.pkl")


class CustomerData(BaseModel):

    gender: int
    SeniorCitizen: int
    Partner: int
    Dependents: int
    tenure: int
    PhoneService: int
    MultipleLines: int
    InternetService: int
    OnlineSecurity: int
    OnlineBackup: int
    DeviceProtection: int
    TechSupport: int
    StreamingTV: int
    StreamingMovies: int
    Contract: int
    PaperlessBilling: int
    PaymentMethod: int
    MonthlyCharges: float
    TotalCharges: float
    Avg_Revenue_Per_Month: float
    Customer_Age_Group: int
    Customer_Segment: int


@app.get("/")
def home():
    return {
        "message": "LTV Prediction API Running"
    }


@app.post("/predict")
def predict(data: CustomerData):

    input_df = pd.DataFrame([data.dict()])

    prediction = model.predict(input_df)

    return {
        "Predicted_LTV": float(prediction[0])
    }
