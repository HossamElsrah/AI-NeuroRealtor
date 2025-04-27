import traceback
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np
import uvicorn

# Initialize FastAPI app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load The Preprocessor & Model
preprocessor = joblib.load('preprocessor.joblib')
model = joblib.load('xgboost_model.joblib')

# log transformation Inverse for Price Predicition
def inverse_log_transform(x):
    return np.expm1(x)

# Define input schema
class PropertyData(BaseModel):
    Area: float
    Rooms: int
    Bathrooms: int
    Type: str
    Furnished: int
    Finished: int
    Feature: str
    City: str
    District: str

# Endpoint for Predicition
@app.post("/predict/")
def predict_property_price(apt_data: PropertyData):
    try:
        # Convert input to DataFrame
        input_data = pd.DataFrame([apt_data.dict()])

        # Apply Preprocessing
        processed_data = preprocessor.transform(input_data)

        # Apply Predict (The Price Will Reaturn as log)
        log_price = model.predict(processed_data)[0]

        # Transform The Price
        price = inverse_log_transform(log_price)

        return {"السعر المتوقع": f"{price:,.0f} جنيه"} 
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=400, detail=str(e))

# Run The Api
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
