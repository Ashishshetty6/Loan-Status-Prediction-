This Streamlit application predicts whether a loan will be approved or rejected based on applicant details. It uses a Decision Tree Classifier trained on historical loan data.

🚀 Features
Upload a CSV file with applicant data to get batch predictions.
Manually enter individual applicant details to get a real-time prediction.
Uses a pre-trained Decision_tree_model.pkl file.
Simple and user-friendly interface.

 Model
Algorithm: Decision Tree Classifier
Training Accuracy: ~79.2% (based on cross-validation)
Trained using features like income, credit history, property area, and more.

This Loan Approval Prediction App is a simple, interactive web application built using Streamlit and a Decision Tree machine learning model. It allows users to:
Upload CSV files containing loan applicant data to get predictions in bulk.
Manually enter individual applicant details through an intuitive form interface.
The app processes the input data, applies the trained model (Decision_tree_model.pkl), and predicts whether a loan will be approved (Yes) or rejected (No).
This tool is ideal for:
Learning how to deploy machine learning models.
Understanding how various applicant factors (like income, credit history, etc.) influence loan approval.
Quick experimentation or demonstrations for ML pipelines in financial services.
