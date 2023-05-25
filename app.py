# importing technologies
import streamlit as st
import numpy as np
import pickle
import pandas as pd

#load the model and dataframe
df = pd.read_csv("bodyfat.csv")
# pipe = pickle.load(open("pipe.pkl", "rb"))

st.title("ModelX - A Supermodel Prediction Model")

# -- Taking user input -- 
#age

age = st.number_input('Age: ')

# Density
Density = st.number_input("Density: ")

# weight
weight = st.number_input("Weight: ")

# height
height = st.number_input("Height: ")

#neck
neck = st.number_input('Neck Size: ')

# chest
chest = st.number_input("Chest Size: ")

# abdomen
abdomen = st.number_input("Abdomen Size: ")

# hip
hip = st.number_input("Hip Size: ")

#thigh
thigh = st.number_input('Thigh Size: ')

# knee
knee = st.number_input("Knee Size: ")

# ankle
ankle = st.number_input("Ankle Measurement: ")

# biceps
biceps = st.number_input("Bicep Size: ")

#forearm
forearm = st.number_input('Forearm Size: ',)

# wrist
wrist = st.number_input("Wrist Size: ")