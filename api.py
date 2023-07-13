import numpy as np
import pandas as pd
import pickle as pkl
from sklearn.linear_model import LinearRegression
from pydantic import BaseModel
from fastapi import FastAPI
import uvicorn
import joblib

app = FastAPI()

# Defines the request body schema using pydantic's BaseModel
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

# Loads the Serialized trained model
super_model = joblib.load('modelX.joblib')

# Creates an endpoint to receive the data for predictions
@app.post('/predict')
def predict(request: RequestBody):
    
    # Makes the data into a form suitable for predictions
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
    
    # Predicts the BodyFat 
    pred_BF = super_model.predict(test_data)[0]
     
    # Returns the Result
    return {
        'BodyFat': pred_BF
        }

# Run the API server
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000, reload=True)

