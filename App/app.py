#importing librarires
import streamlit as st
import pickle
import numpy as np
from PIL import Image
import json
# loading and reading the file
# Opening the file
model = pickle.load(open('App/modelx.pkl','rb'))
# model = open('model.json')
  
# # returns JSON object as 
# # a dictionary
# data = json.load(model)
# # Closing file
# model.close()

#creating welcome page
favicon = Image.open("Img/ModelX.png")
st.set_page_config(
    page_title="ModelX",
    page_icon=favicon,
    initial_sidebar_state="expanded",

)
#creating a function that uses the file to make predictions
def predict_fat(Density, Body_mass_Index, Neck, Chest, Abdomen, Hip, Thigh, Knee, Ankle, Biceps, Forearm, Wrist):
    input=np.array([[Density, Body_mass_Index, Neck, Chest, Abdomen, Hip, Thigh, Knee, Ankle, Biceps, Forearm, Wrist]]).astype(np.float64)
    prediction = model.predict(input)
    
    return int(prediction)

# creating the main function
def main():
    st.title("ModelX - Supermodel Prediction Model")
    html_temp = """
    <p> ModelX is a predictive model specifically designed to estimate the body fat percentage of aspiring and established supermodels. 
    This model serves the purpose of aiding individuals who aspire to become supermodels or those in the modeling industry who are interested in assessing their body fat percentage 
    or monitoring their physical attributes relevant to their modeling career.</p>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.title("Input parameters below:")
    # taking user input
    Density = st.number_input("Density (Cm): ")
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

    if st.button("Predict the BodyFat"):
        # Check if all input fields are filled
        if Density and Body_mass_Index and Neck and Chest and Abdomen and Hip and Thigh and Knee and Ankle and Biceps and Forearm and Wrist:
            all_fields_filled = True
        else:
            st.warning('Please fill in all input fields.')

        # Proceed with prediction and display output if all fields are filled
        if all_fields_filled:
            output = predict_fat(Density, Body_mass_Index, Neck, Chest, Abdomen, Hip, Thigh, Knee, Ankle, Biceps, Forearm, Wrist)
            st.success('The predicted body fat is {}%'.format(output))

            if 6 <= output <= 16:
                print("The individual is highly suitable for modeling.")
                st.markdown("The individual is highly suitable for modeling.")
                st.markdown(f"Modeling Success Rate is {100 - output}%")
            elif output > 16 and output <= 22:
                print("The individual has relatively lower chances for modeling.")
                st.markdown("The individual has relatively lower chances for modeling.")
                st.markdown(f"Modeling Success Rate is {100 - output}%")
            elif output > 22:
                print("The individual's chances for modeling are low/uncertain.")
                st.markdown("The individual's chances for modeling are low/uncertain.")
                st.markdown(f"Modeling Success Rate is {100 - output}%")
if __name__=='__main__':
    main()                