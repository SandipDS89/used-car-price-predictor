# 🚗 Used Car Price Prediction Web App

A **machine learning-powered web app** built using **Streamlit** that predicts the **selling price of used cars** based on various car attributes such as kilometers driven, fuel type, transmission, and ownership history.

---

## 📊 Project Description

This project trains multiple regression models using a dataset from **CarDekho**, evaluates their performance, and deploys the best-performing model (Random Forest) through a clean and interactive Streamlit UI.

### 🔍 Features:

- Predict selling price for used cars
- Log-transform target for better accuracy
- Visual insights:
  - Feature Importance
  - Price vs KM Driven
  - Fuel Type vs Average Price
  - Distribution of Selling Price

---

## 🛠️ Technologies Used

- Python
- Pandas & NumPy
- Scikit-learn
- Matplotlib & Seaborn
- Streamlit
- Joblib / Pickle

---

## 📁 Project Structure

used-car-price-predictor/
├── app.py # Streamlit web app
├── CAR DETAILS FROM CAR DEKHO.csv # Dataset
├── linear_regression_model.pkl # Trained model file
├── requirements.txt # Project dependencies
└── README.md # Project documentation 

## Install dependencies:

pip install -r requirements.txt
##  Run the Streamlit app:

streamlit run app.py