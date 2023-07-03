import streamlit as st
from PIL import Image
favicon = Image.open("Img/ModelX.png")
st.set_page_config(
    page_title="ModelX",
)

st.write("# ModelX - Supermodel Prediction Machine Learning Model! ")


st.markdown(
    """
    ModelX is a predictive model specifically designed to estimate the body fat percentage of aspiring and established supermodels. 
    This model serves the purpose of aiding individuals who aspire to become supermodels or those in the modeling industry who are interested in 
    assessing their body fat percentage or monitoring their physical attributes relevant to their modeling career.
    ### Want to learn more?
    - Jump into my Github page [Github](https://github.com/Gideon-Ogunbanjo)
"""
)