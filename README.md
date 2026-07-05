🚨 Credit Card Fraud Detection System
This project is a Machine Learning-powered application designed to detect fraudulent credit card transactions. It provides an interactive dashboard built with Streamlit to allow users to input transaction details and receive real-time predictions.

🛠 Features
Real-time Prediction: Instantly classify transactions as "Safe" or "Fraud" based on provided inputs.

Interactive Dashboard: A user-friendly interface featuring sliders, dropdowns, and number inputs for ease of use.

ML Integration: Uses a pre-trained joblib model to deliver fast and accurate predictions.

📂 Project Structure
ML_WEEK4_TASK/
├── app.py              # Main Streamlit application script
├── models/             
│   └── best_model.pkl  # Trained machine learning model
├── data/
│   └── credit_card_fraud_10k.csv # Dataset
└── model_training.ipynb # Jupyter notebook for model development

🚀 How to Run
Clone the repository or download the project folder.

Install the required libraries:
Open your terminal in the project folder and run:

Bash
pip install streamlit pandas joblib scikit-learn
Launch the application:

Bash
streamlit run app.py
💡 Tech Stack
Python: Core programming language.

Streamlit: Used for the frontend dashboard and interactivity.

Scikit-Learn: Used for the machine learning pipeline and model training.

Joblib/Pickle: Used for model serialization and loading.

