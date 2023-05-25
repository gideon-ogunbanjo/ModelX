# importing technologies
import streamlit as st
import numpy as np
import pickle
import pandas as pd

#load the model and dataframe
df = pd.read_csv("bodyfat.csv")
# pipe = pickle.load(open("pipe.pkl", "rb"))

st.title("ModelX - Supermodel Prediction Model")

# taking user input

#age
age = st.selectbox('Age: ', df['Age'].unique())

# Density
Density = st.selectbox("Density: ", df['Density'].unique())

# weight
weight = st.selectbox("Weight: ", df['Weight'].unique())

# height
height = st.selectbox("Height: ", df['Height'].unique())

#neck
neck = st.selectbox('Neck Size: ', df['Neck'].unique())

# chest
chest = st.selectbox("Chest Size: ", df['Chest'].unique())

# abdomen
abdomen = st.selectbox("Abdomen Size: ", df['Abdomen'].unique())

# hip
hip = st.selectbox("Hip Size: ", df['Hip'].unique())

#thigh
thigh = st.selectbox('Thigh Size: ', df['Thigh'].unique())

# knee
knee = st.selectbox("Knee Size", df['Knee'].unique())

# ankle
ankle = st.selectbox("Ankle Measurement", df['Ankle'].unique())

# biceps
biceps = st.selectbox("Bicep Size: ", df['Biceps'].unique())

#forearm
forearm = st.selectbox('Forearm Size: ', df['Forearm'].unique())

# wrist
wrist = st.selectbox("Wrist Size: ", df['Wrist'].unique())
