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
