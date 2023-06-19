#importing librarires
import streamlit as st
import pickle
import numpy as np
import json
# loading and reading the JSON file
# Opening JSON file
model = open('model.json')
  
# returns JSON object as 
# a dictionary
data = json.load(model)
# Closing file
model.close()

# creating welcome page
st.set_page_config(
    page_title="ModelX",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded",
)

from PIL import Image
image = Image.open('ModelX.png')

st.image(image,
      use_column_width=True)

#creating a function to use the pickle file to make predictions
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
    Density = st.text_input("Density","Type Here")
    Age = st.text_input("Age","Type Here")
    Weight = st.text_input("Weight","Type Here")
    Height = st.text_input("Height","Type Here")
    Neck = st.text_input("Neck","Type Here")
    Chest = st.text_input("Chest","Type Here")
    Abdomen = st.text_input("Abdomen","Type Here")
    Hip = st.text_input("Hip","Type Here")
    Thigh = st.text_input("Thigh","Type Here")
    Knee = st.text_input("Knee","Type Here")
    Ankle = st.text_input("Ankle","Type Here")
    Biceps = st.text_input("Biceps","Type Here")
    Forearm = st.text_input("Forearm","Type Here")
    Wrist = st.text_input("Wrist","Type Here")
    safe_html ="""  
        <div style="background-color:#80ff80; padding:10px >
        <h2 style="color:white;text-align:center;"> The individual is Fantastic for modeling</h2>
        </div>
        """
    safe_html ="""  
      <div style="background-color:#80ff80; padding:10px >
      <h2 style="color:white;text-align:center;"> The Individual is suitable</h2>
      </div>
    """
    warn_html ="""  
      <div style="background-color:#F4D03F; padding:10px >
      <h2 style="color:white;text-align:center;"> The individual is managable</h2>
      </div>
    """
    danger_html="""  
      <div style="background-color:#F08080; padding:10px >
       <h2 style="color:black ;text-align:center;"> The individual is not suitable</h2>
       </div>
    """

    if st.button("Predict the BodyFat"):
        output = predict_fat(Density, Age, Weight, Height, Neck, Chest, Abdomen, Hip, Thigh, Knee, Ankle, Biceps, Forearm, Wrist)
        st.success('The age is {}'.format(output))

        if output == 1:
            st.markdown(safe_html,unsafe_allow_html=True)
        elif output == 2:
            st.markdown(warn_html,unsafe_allow_html=True)
        elif output == 3:
            st.markdown(danger_html,unsafe_allow_html=True)

if __name__=='__main__':
    main()