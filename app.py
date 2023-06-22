#importing librarires
import streamlit as st
import pickle
import numpy as np
import json
# loading and reading the file
# Opening the file
model = pickle.load(open('modelX.pkl','rb'))
# model = open('model.json')
  
# # returns JSON object as 
# # a dictionary
# data = json.load(model)
# # Closing file
# model.close()

# creating welcome page
st.set_page_config(
    page_title="ModelX",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded",
)

#creating a function that uses the file to make predictions
def predict_fat(Density, Age, Weight, Height, Neck, Chest, Abdomen, Hip, Thigh, Knee, Ankle, Biceps, Forearm, Wrist):
    input=np.array([[Density, Age, Weight, Height, Neck, Chest, Abdomen, Hip, Thigh, Knee, Ankle, Biceps, Forearm, Wrist]]).astype(np.float64)
    prediction = model.predict(input)
    
    return int(prediction)

# creating the main function
def main():
    st.title("ModelX - Supermodel Prediction Model")
    html_temp = """
    <div style="background:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;"> ModelX </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html = True)
    
    #taking user input
    Density = st.number_input("Density: ")
    Age = st.number_input('Age', min_value=1, max_value=50, value=1, step=1)
    Weight = st.number_input("Weight: ")
    Height = st.number_input("Height: ")
    Neck = st.number_input("Neck Size: ")
    Chest = st.number_input("Chest Size: ")
    Abdomen = st.number_input("Abdomen Size: ")
    Hip = st.number_input("Hip Width: ")
    Thigh = st.number_input("Thigh Size: ")
    Knee = st.number_input("Knee Size: ")
    Ankle = st.number_input("Ankle Size: ")
    Biceps = st.number_input("Biceps Size: ")
    Forearm = st.number_input("Forearm Size: ")
    Wrist = st.number_input("Wrist Size: ")
    safe_html ="""  
        <div style="background-color:#80ff80; padding:10px >
        <h2 style="color:white;text-align:center;"> The individual is highly suitable for modeling.</h2>
        </div>
    """
    warn_html ="""  
      <div style="background-color:#F4D03F; padding:10px >
      <h2 style="color:white;text-align:center;"> The individual has relatively lower chances for modeling.</h2>
      </div>
    """
    danger_html="""  
      <div style="background-color:#F08080; padding:10px >
       <h2 style="color:black ;text-align:center;"> The individual's chances for modeling are low/uncertain.</h2>
       </div>
    """

    if st.button("Predict the BodyFat"):
        output = predict_fat(Density, Age, Weight, Height, Neck, Chest, Abdomen, Hip, Thigh, Knee, Ankle, Biceps, Forearm, Wrist)
        st.success('The predicted body fat is {}%'.format(output))

        if output > 15 and output < 20:
            print("The individual is highly suitable for modeling.")
            st.markdown(safe_html,unsafe_allow_html=True)
        elif output > 20 and output <25:
            print("The individual has relatively lower chances for modeling")
            st.markdown(warn_html,unsafe_allow_html=True)
        elif output >25:
            print("The individual's chances for modeling are low/uncertain.")
            st.markdown(danger_html,unsafe_allow_html=True)

if __name__=='__main__':
    main()