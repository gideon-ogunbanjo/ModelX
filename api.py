import numpy as np
import pandas as pd
import pickle as pkl
from sklearn.linear_model import LinearRegression
from pydantic import BaseModel
from fastapi import FastAPI
import uvicorn
import joblib

app = FastAPI()

class RequestBody(BaseModel):
    Density: float
    Body_mass_Index: float
    Neck: float
    Chest: float
    Abdomen: float
    Hip: float
    Thigh: float
    Knee: float
    Ankle: float
    Biceps: float
    Forearm: float
    Wrist: float

# Load the model
super_model = joblib.load('modelX.joblib')

# Create an endpoint to receive the data for prediction
@app.post('/predict')
def predict(request: RequestBody):
    # Making the data in a form suitable for prediction
    test_data = [[
        request.Density,
        request.Body_mass_Index,
        request.Neck,
        request.Chest,
        request.Abdomen,
        request.Hip,
        request.Thigh,
        request.Knee,
        request.Ankle,
        request.Biceps,
        request.Forearm,
        request.Wrist
    ]]
    
    # Predicting the BodyFat
    pred_BF = super_model.predict(test_data)[0]
     
    # Return the Result
    return {'BodyFat': pred_BF}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)

