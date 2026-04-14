# Heart-Disease-Prediction-using-Machine-Learning
Thus preventing Heart diseases has become more than necessary. Good data-driven systems for predicting heart diseases can improve the entire research and prevention process, making sure that more people can live healthy lives. This is where Machine Learning comes into play. Machine Learning helps in predicting the Heart diseases, and the predictions made are quite accurate.

This project is an AI-powered Heart Disease Prediction System that analyzes patient medical data to predict the likelihood of heart disease. It provides a clinical dashboard interface for real-time analysis and automatically sends reports to both doctors and patients via email.

🚀 Features
🔍 Predicts heart disease using Machine Learning
📊 Interactive Streamlit dashboard
📈 Displays prediction with probability (risk %)
📧 Automated email reporting to doctor & patient
🧾 Structured clinical input form
⚡ Real-time analysis

🧠 Technologies Used
Python
Streamlit
Scikit-learn
Pandas
NumPy
SMTP (Email Automation)

📂 Project Structure
├── app.py                # Streamlit web app
├── model.pkl            # Trained ML model
├── Heart_disease_prediction.ipynb   # Model training notebook
├── output.png           # Sample output
└── README.md

Machine Learning algorithms used:
1. Logistic Regression (Scikit-learn)
2. Naive Bayes (Scikit-learn)
3. Support Vector Machine (Linear) (Scikit-learn)
4. K-Nearest Neighbours (Scikit-learn)
5. Decision Tree (Scikit-learn)
6. Random Forest (Scikit-learn)
7. XGBoost (Scikit-learn)
8. Artificial Neural Network with 1 Hidden layer (Keras)

Accuracy achieved: 95% (Random Forest)

⚙️ Installation & Setup

1️⃣ Clone the repository
git clone https://github.com/iamsanjeebmishra/Heart-Disease-Prediction.git
cd Heart-Disease-Prediction

2️⃣ Install dependencies
pip install -r requirements.txt
(If requirements.txt not present, install manually:)
pip install streamlit pandas numpy scikit-learn

3️⃣ Run the application
streamlit run app.py

🖥️ Usage

Enter patient medical details in the dashboard

Click Predict & Forward Report

View prediction result (High Risk / Low Risk)

Report gets automatically sent via email

📧 Email Configuration

✅ STEP 1: Turn ON 2-Step Verification

Go to 👉 https://myaccount.google.com/security

Find 2-Step Verification
Turn it ON

✅ STEP 2: Generate App Password

Go to 👉 https://myaccount.google.com/apppasswords
Click Generate
You’ll get a 16-digit password
👉 Example:
abcdefghijklmnop

Update sender email credentials in app.py:

SENDER_EMAIL = "your_email@gmail.com"
SENDER_PASS = "your_app_password"

Use Google App Password, not your normal password.

📊 Input Features
Age
Sex
Chest Pain Type
Resting Blood Pressure
Cholesterol
Fasting Blood Sugar
ECG Results
Maximum Heart Rate
Exercise-Induced Angina
Oldpeak
Slope
Number of Major Vessels
Thalassemia

⚠️ Disclaimer

This project is for educational purposes only and should not be used as a substitute for professional medical advice.

👨‍💻 Author

Sanjeeb Kumar Mishra

GitHub: https://github.com/iamsanjeebmishra

⭐ Contribution

Feel free to fork this repository and contribute!

