# importing technologies
import streamlit as st
import numpy as np
import pickle
import pandas as pd

#load the model and dataframe
df = pd.read_csv("bodyfat.csv")
pipe = pickle.load(open("pipe.pkl", "rb"))

st.title("Supermodel Prediction Model")
