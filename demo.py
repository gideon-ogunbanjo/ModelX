import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier

st.title("""
ModelX
""")


st.sidebar.header('Input Parameters')
def user_input_features():
    density = st.sidebar.slider('Density', 4.3, 7.9, 5.4)
    age = st.sidebar.slider('Age', 19.0, 30.0, 25.0)
    weight = st.sidebar.slider('Weight', 1.0, 6.9, 1.3)
    height = st.sidebar.slider('Height', 0.1, 2.5, 0.2)
    chest = st.sidebar.slider('Chest', 0.1, 2.5, 0.2)
    abdomen = st.sidebar.slider('Abdomen', 0.1, 2.5, 0.2)
    hip = st.sidebar.slider('Hip', 0.1, 2.5, 0.2)
    thigh = st.sidebar.slider('Thigh', 0.1, 2.5, 0.2)
    knee = st.sidebar.slider('Knee', 0.1, 2.5, 0.2)
    ankle = st.sidebar.slider('Ankle', 0.1, 2.5, 0.2)
    bicep = st.sidebar.slider('Biceps', 0.1, 2.5, 0.2)
    forearm = st.sidebar.slider('Forearm', 0.1, 2.5, 0.2)
    wrist = st.sidebar.slider('Wrist', 0.1, 2.5, 0.2)



    data = {'Density': density,
            'Age': age,
            'Weight': weight,
            'Height': height,
            'Chest':chest,
            'Abdomen':abdomen,
            'Hip':hip,
            'Thigh':thigh,
            'Knee':knee,
            'Ankle':ankle,
            'Biceps':bicep,
            'Forearm':forearm,
            'Wrist':wrist}
    features = pd.DataFrame(data, index=[0])
    return features


df = user_input_features()
st.subheader('User Input parameters')
st.write(df)
iris = datasets.load_iris()
X = iris.data
Y = iris.target
clf = DecisionTreeClassifier()
clf.fit(X, Y)
prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)
st.subheader('Labels of Class and their respective index numbers')
st.write(iris.target_names)
st.subheader('Prediction')
st.write(iris.target_names[prediction])
st.subheader('Prediction Probability')
st.write(prediction_proba)