# importing technologies
import streamlit as st
import numpy as np
import pickle
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.compose import ColumnTransformer
import joblib

#loading the model dataset ande pickle file
df = pd.read_csv("bodyfat.csv")

with st.columns(3)[1]:
     st.title("ModelX")
with st.columns(3)[1]:
     st.markdown("Supermodel Prediction Model")
st.markdown("Enter user parameters")
# -- Taking user input -- 

#age
age = st.number_input('Age: ')

# Density
density = st.number_input("Density: ")

# weight
weight = st.number_input("Weight: ")

# height
height = st.number_input("Height: ")

#neck
neck = st.number_input("Neck Size: ")

# chest
chest = st.number_input("Chest Size: ")

# abdomen
abdomen = st.number_input("Abdomen Size: ")

# hip
hip = st.number_input("Hip Size: ")

#thigh
thigh = st.number_input("Thigh Size: ")

# knee
knee = st.number_input("Knee Size: ")

# ankle
ankle = st.number_input("Ankle Measurement: ")

# biceps
biceps = st.number_input("Bicep Size: ")

#forearm
forearm = st.number_input("Forearm Size: ")

# wrist
wrist = st.number_input("Wrist Size: ")

# running predictions

if st.button('Predict'):
    ppi = None
    query = np.array([age, density, weight, height, neck, chest, abdomen, hip, thigh, knee, ankle, biceps, forearm, wrist])
    query = query.reshape(1, 14)
    prediction = str(int(np.exp(pipe.predict(query)[0])))
    st.title("The predicted body fat perentage of this individual is: " + prediction)
st.markdown("Created by Gideon Ogunbanjo")