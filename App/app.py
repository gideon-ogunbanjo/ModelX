#importing librarires
import streamlit as st
import pickle
import numpy as np
from PIL import Image

# loading and reading the file
# Opening the file
model = pickle.load(open('./App/modelx.pkl', 'rb'))

# Creating the Welcome Page and Page Configuration
favicon = Image.open("Img/ModelX.png")
st.set_page_config(
    page_title="ModelX",
    page_icon=favicon,
    initial_sidebar_state="expanded",
)

# Defining the Prediction Function:
def predict_fat(Density, Body_mass_Index, Neck, Chest, Abdomen, Hip, Thigh, Knee, Ankle, Biceps, Forearm, Wrist):
    input=np.array([[Density, Body_mass_Index, Neck, Chest, Abdomen, Hip, Thigh, Knee, Ankle, Biceps, Forearm, Wrist]]).astype(np.float64)
    prediction = model.predict(input)
    return int(prediction)

# Creating the main function
def main():
    # Displaying ModelX's description
    st.title("ModelX - Supermodel Prediction Model")
    html_temp = """
    <p> ModelX is a predictive model developed for aspiring and established supermodels to estimate body fat percentage. 
    It helps individuals in the modeling industry assess and monitor their physical attributes crucial to their modeling career.</p>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.title("Input parameters below:")
    
    # Taking user input
    Density = st.number_input("Density (g/cm3): ")
    Body_mass_Index = st.number_input("Body Mass Index: ")
    Neck = st.number_input("Neck Size (Cm): ")
    Chest = st.number_input("Chest Size (Cm): ")
    Abdomen = st.number_input("Abdomen Size (Cm): ")
    Hip = st.number_input("Hip Width (Cm): ")
    Thigh = st.number_input("Thigh Size (Cm): ")
    Knee = st.number_input("Knee Size (Cm): ")
    Ankle = st.number_input("Ankle Size (Cm): ")
    Biceps = st.number_input("Biceps Size (Cm): ")
    Forearm = st.number_input("Forearm Size (Cm): ")
    Wrist = st.number_input("Wrist Size (Cm): ")
    
    # Creating HTML Templates for Result Visualization
    safe_html = """  
        <div style="background-color:#09BC8A; padding:10px">
        <h2 style="color:white;text-align:center;"> The individual is highly suitable for modeling.</h2>
        </div>
    """
    warn_html = """  
      <div style="background-color:#FCBA04; padding:10px">
      <h2 style="color:white;text-align:center;"> The individual has relatively lower chances for modeling.</h2>
      </div>
    """
    danger_html = """  
      <div style="background-color:#A50104; padding:10px">
       <h2 style="color:black ;text-align:center;"> The individual's chances for modeling are low/uncertain.</h2>
       </div>
    """

    # Flag variable to track if all input fields are filled
    all_fields_filled = False
    
    # Checking Input Completeness and Making Predictions:
    if st.button("Predict the BodyFat"):
        # Check if all input fields are filled
        if Density and Body_mass_Index and Neck and Chest and Abdomen and Hip and Thigh and Knee and Ankle and Biceps and Forearm and Wrist:
            all_fields_filled = True
        else:
            st.warning('Please fill in all input fields.')

        # Proceed with prediction and display output if all fields are filled
        if all_fields_filled:
            output = predict_fat(Density, Body_mass_Index, Neck, Chest, Abdomen, Hip, Thigh, Knee, Ankle, Biceps, Forearm, Wrist)
            st.success('Predicted body fat percentage: {}%'.format(output))

            if 1 <= output <= 20:
                print("The individual is highly suitable for modeling.")
                st.markdown("The individual is highly suitable for modeling.")
                st.markdown(f"Modeling Success Rate: {100 - output}%")
            elif output > 20 and output <= 23:
                print("The individual has relatively lower chances for modeling.")
                st.markdown("The individual has relatively lower chances for modeling.")
                st.markdown(f"Modeling Success Rate: {100 - output}%")
            elif output > 24:
                print("The individual's chances for modeling are low/uncertain.")
                st.markdown("The individual's chances for modeling are low/uncertain.")
                st.markdown(f"Modeling Success Rate: {100 - output}%")
    link='Created by [Gideon Ogunbanjo](https://gideonogunbanjo.netlify.app)'
    st.markdown(link,unsafe_allow_html=True)
# Main Function Invocation:
if __name__=='__main__':
    main()