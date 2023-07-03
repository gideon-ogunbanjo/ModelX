# Importing Necessary modules
import numpy as np
import pandas as pd
import pickle as pkl
from sklearn.linear_model import LinearRegression
from pydantic import BaseModel
from fastapi import FastAPI
import uvicorn

# Declaring our FastAPI instance
app = FastAPI()
# Creating class to define the request body
# and the type hints of each attribute
class request_body(BaseModel):
    Density : float
    Body_mass_Index : float
    Neck : float
    Chest : float
    Abdomen : float
    Hip : float
    Thigh : float
    Knee : float
    Ankle : float
    Biceps : float
    Forearm : float
    Wrist : float
# Defining path operation for root endpoint
# Loading file
data = pd.read_pickle('modelX.pkl')

# Getting features and targets from the dataset
X = data.features
y = data.target

# Fitting our Model on the dataset
model = LinearRegression()
model.fit(X,y)

# Creating an Endpoint to receive the data to make prediction on.
@app.post('/predict')
def predict(data : request_body):
    # Making the data in a form suitable for prediction
    test_data = [[
            data.Density,
            data.Body_mass_Index,
            data.Neck,
            data.Chest,
            data.Abdomen,
            data.Hip,
            data.Thigh,
            data.Knee,
            data.Ankle,
            data.Biceps,
            data.Forearm,
            data.Wrist
    ]]
    # Predicting the BodyFat
    class_idx = model.predict(test_data)[0]
     
    # Return the Result
    return { 'BodyFat' : data.target_names[class_idx]}