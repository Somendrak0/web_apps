import streamlit as st
import pandas as pd
from sklearn import datasets
import pickle

# Header------------------/
st.header("Irir Dataset Prediction.")

st.write("""
I made this web app to **pridict the species**. You can **predict** by **entering Sepal length, Sepal width, Patel length, Petal width**.
""")

# Sidebar-----------------/
st.sidebar.title('Input data values.')

def userInput():
    sepal_len = st.sidebar.slider("Sepal Length", 4.2, 7.7, 5.7)
    sepal_wid = st.sidebar.slider("Sepal Width", 2.2, 4.4, 3.0)
    petal_len = st.sidebar.slider("Petal Length", 1.2, 6.0, 3.5)
    petal_wid = st.sidebar.slider("Petal Width", 0.1, 2.5, 0.5)

    data = {"sepal length": sepal_len,
            "sepal width": sepal_wid,
            "petal length": petal_len,
            "petal width": petal_wid}
    feature = pd.DataFrame(data, index=[0])
    return feature

df = userInput()

#Showing User Input Values---------/
st.header("User Inputs.")
st.write("""Your input values of **Iris Data**""")

st.write(df)
if st.button("Predict"):
    
    # Prediction-----------------------/
    st.header("Predicted value.")
    st.write("""Predicted Speices of **Iris Flowers.**""")

    model = pickle.load(open("My_First_Iris_Model.pk", 'rb'))
    data = datasets.load_iris()

    pred = model.predict(df)

    st.write(f"""Predicted Value is: **{pred[0]}**""")
    st.write(f"""* Predicted Species: **{data.target_names[pred][0]}.**""")
