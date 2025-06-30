import streamlit as st
import pickle
import pandas as pd

# Load model
model = pickle.load(open("payment.pkl", "rb"))

# App UI
st.title("💳 Online Payment Fraud Detection")

st.markdown("Enter transaction details below to predict if it's Fraud or Not Fraud.")

# Input fields
step = st.number_input("Step (Time Step)", min_value=0)
type_ = st.selectbox("Transaction Type (0=Cash in, 1=Cash out, etc.)", [0, 1, 2, 3, 4])
amount = st.number_input("Transaction Amount", min_value=0.0)
oldbalanceOrg = st.number_input("Old Balance (Sender)", min_value=0.0)
newbalanceOrig = st.number_input("New Balance (Sender)", min_value=0.0)
oldbalanceDest = st.number_input("Old Balance (Receiver)", min_value=0.0)
newbalanceDest = st.number_input("New Balance (Receiver)", min_value=0.0)

# Prediction
if st.button("Predict"):
    input_data = [[step, type_, amount, oldbalanceOrg, newbalanceOrig, oldbalanceDest, newbalanceDest]]
    prediction = model.predict(input_data)[0]
    result = "🔴 Fraud Transaction" if prediction == 1 else "🟢 Legitimate Transaction"
    st.success(f"Prediction: {result}")
