import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load model
with open("Decision_tree_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Loan Approval Prediction App")
st.write("Upload a CSV file or manually enter loan applicant details to predict loan approval.")

# --- Upload CSV Section ---
st.header("1. Upload a CSV File")
uploaded_file = st.file_uploader("Upload loan applicant data CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    st.subheader("Uploaded Data")
    st.write(df.head())

    # Make sure the columns match model input
    try:
        predictions = model.predict(df)
        df['Loan_Approval_Prediction'] = ['Approved' if p == 1 else 'Rejected' for p in predictions]
        st.subheader("Prediction Results")
        st.write(df)
    except Exception as e:
        st.error(f"Prediction failed. Ensure the file matches the required input format. Error: {e}")

# --- Manual Input Section ---
st.header("2. Or Enter Details Manually")

with st.form("manual_entry_form"):
    Gender = st.selectbox("Gender", [1, 0], format_func=lambda x: "Male" if x == 1 else "Female")
    Married = st.selectbox("Married", [1, 0], format_func=lambda x: "Yes" if x == 1 else "No")
    Dependents = st.selectbox("Dependents", [0, 1, 2, 4])
    Education = st.selectbox("Education", [1, 0], format_func=lambda x: "Graduate" if x == 1 else "Not Graduate")
    Self_Employed = st.selectbox("Self Employed", [1, 0], format_func=lambda x: "Yes" if x == 1 else "No")
    ApplicantIncome = st.number_input("Applicant Income", min_value=0)
    CoapplicantIncome = st.number_input("Coapplicant Income", min_value=0)
    LoanAmount = st.number_input("Loan Amount", min_value=0.0)
    Loan_Amount_Term = st.number_input("Loan Amount Term (in days)", min_value=0.0, value=360.0)
    Credit_History = st.selectbox("Credit History", [1.0, 0.0])
    Property_Area = st.selectbox("Property Area", [0, 1, 2], format_func=lambda x: ["Rural", "Semiurban", "Urban"][x])

    submitted = st.form_submit_button("Predict")

    if submitted:
        input_data = pd.DataFrame([[
            Gender, Married, Dependents, Education, Self_Employed,
            ApplicantIncome, CoapplicantIncome, LoanAmount,
            Loan_Amount_Term, Credit_History, Property_Area
        ]], columns=[
            'Gender', 'Married', 'Dependents', 'Education', 'Self_Employed',
            'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
            'Loan_Amount_Term', 'Credit_History', 'Property_Area'
        ])

        prediction = model.predict(input_data)[0]
        result = "✅ Loan Approved" if prediction == 1 else "❌ Loan Rejected"
        st.subheader("Prediction Result")
        st.success(result)
