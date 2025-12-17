# import libraries
import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Load the saved model and data
model = pickle.load(open('model.pkl', 'rb'))
imputer = pickle.load(open('imputer.pkl', 'rb'))
df = pd.read_csv('cleaned_data.csv')

st.set_page_config(page_title="Air Quality Predictor", layout="wide")
page = st.sidebar.selectbox("Navigate", ["Home/EDA", "Predictor"])

if page == "Home/EDA":
    st.title("Air Quality Analysis Dashboard")
    st.dataframe(df.head())
    # Display statistics instead of image to avoid FileNotFoundError
    st.subheader("Dataset Statistics")
    st.write(df.describe())

elif page == "Predictor":
    st.title("AQI Prediction Tool")
    # Inputs for features
    inputs = []
    col1, col2 = st.columns(2)
    features = ['PM2.5', 'PM10', 'NO', 'NO2', 'NOx', 'NH3', 'CO', 'SO2', 'O3']
    
    for i, feat in enumerate(features):
        with col1 if i % 2 == 0 else col2:
            val = st.number_input(f"Enter {feat}", value=float(df[feat].median()))
            inputs.append(val)
    
    if st.button("Predict AQI"):
        prediction = model.predict([inputs])
        st.success(f"Estimated AQI: {prediction[0]:.2f}")
