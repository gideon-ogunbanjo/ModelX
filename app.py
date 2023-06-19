#importing librarires
import streamlit as st
import pickle
import numpy as np

# loading and unpickling the pickle file
model = pickle.load(open('modelX.pkl','rb'))


#creating a function to use the pickle file to make predictions
def predict_fat(Density, Age, Weight, Height, Neck, Chest, Abdomen, Hip, Thigh, Knee, Ankle, Biceps, Forearm, Wrist):
    input=np.array([[Density, Age, Weight, Height, Neck, Chest, Abdomen, Hip, Thigh, Knee, Ankle, Biceps, Forearm, Wrist]]).astype(np.float64)
    prediction = model.predict(input)
    
    return int(prediction)

