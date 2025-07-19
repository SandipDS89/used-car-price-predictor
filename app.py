import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

# Load the trained model
model = joblib.load('linear_regression_best_model.pkl')

st.title("🚗 Used Car Price Predictor")
st.markdown("### Enter the car details below:")

# Input fields
km_driven = st.number_input("Kilometers Driven", min_value=0, value=50000, step=1000)
fuel = st.selectbox("Fuel Type", ['Petrol', 'Diesel', 'CNG', 'LPG', 'Electric'])
seller_type = st.selectbox("Seller Type", ['Individual', 'Dealer', 'Trustmark Dealer'])
transmission = st.selectbox("Transmission Type", ['Manual', 'Automatic'])
owner = st.selectbox("Ownership", ['First Owner', 'Second Owner', 'Third Owner', 'Fourth & Above Owner', 'Test Drive Car'])
car_age = st.slider("Age of the Car(Years)", min_value=0, max_value=25, value=5)

# Prediction
if st.button("Predict Selling Price"):
    # Transform input
    input_data = {
        'km_driven': [np.log1p(km_driven)],
        'fuel': [fuel],
        'seller_type': [seller_type],
        'transmission': [transmission],
        'owner': [owner],
        'car_age': [car_age]
    }

    import pandas as pd
    input_df = pd.DataFrame(input_data)

    # Predict log price
    log_price = model.predict(input_df)[0]

    # Convert back to actual price
    predicted_price = np.expm1(log_price)

    st.success(f"💰 Predicted Selling Price: ₹{predicted_price:,.2f}")

