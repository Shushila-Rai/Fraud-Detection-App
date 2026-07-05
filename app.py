import streamlit as st
import pandas as pd
import joblib
import os


model_path = os.path.join('models', 'best_model.pkl') 

if not os.path.exists(model_path):
    st.error(f"Error: '{model_path}' nahi mili. Check karein ki file 'models' folder mein hai.")
    st.stop()

model = joblib.load(model_path)

st.title("🚨 Credit Card Fraud Detector")

with st.form("fraud_form"):
    amount = st.number_input("Transaction Amount", min_value=0.0)
    merchant_category = st.selectbox("Merchant Category", ["Grocery", "Electronics", "Clothing", "Food", "Travel"])
    transaction_hour = st.slider("Transaction Hour", 0, 23, 12)
    device_trust_score = st.slider("Device Trust Score", 0, 100, 50)
    velocity_last_24h = st.number_input("Velocity (last 24h)", min_value=0)
    cardholder_age = st.number_input("Cardholder Age", 18, 90, 30)
    
    submit = st.form_submit_button("Predict")

if submit:
   
    input_data = pd.DataFrame({
        'amount': [amount],
        'merchant_category': [merchant_category],
        'transaction_hour': [transaction_hour],
        'device_trust_score': [device_trust_score],
        'velocity_last_24h': [velocity_last_24h],
        'cardholder_age': [cardholder_age]
    })
    
  
    try:
        prediction = model.predict(input_data)
        if prediction[0] == 1:
            st.error("⚠️ ALERT: Fraud Detected!")
        else:
            st.success("✅ Transaction is Safe.")
    except Exception as e:
        st.error(f"Prediction Error: {e}")