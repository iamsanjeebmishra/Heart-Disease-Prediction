# Heart-Disease-Prediction-using-Machine-Learning
Thus preventing Heart diseases has become more than necessary. Good data-driven systems for predicting heart diseases can improve the entire research and prevention process, making sure that more people can live healthy lives. This is where Machine Learning comes into play. Machine Learning helps in predicting the Heart diseases, and the predictions made are quite accurate.

This project is an AI-powered Heart Disease Prediction System that analyzes patient medical data to predict the likelihood of heart disease. It provides a clinical dashboard interface for real-time analysis and automatically sends reports to both doctors and patients via email.

🚀 Features
1. 🔍 Predicts heart disease using Machine Learning
2. 📊 Interactive Streamlit dashboard
3. 📈 Displays prediction with probability (risk %)
4. 📧 Automated email reporting to doctor & patient
5. 🧾 Structured clinical input form
6. ⚡ Real-time analysis


🧠 Technologies Used
1. Python
2. Streamlit
3. Scikit-learn
4. Pandas
5. NumPy
6. SMTP (Email Automation)


Machine Learning algorithms used:

1. Logistic Regression (Scikit-learn)
2. Naive Bayes (Scikit-learn)
3. Support Vector Machine (Linear) (Scikit-learn)
4. K-Nearest Neighbours (Scikit-learn)
5. Decision Tree (Scikit-learn)
6. Random Forest (Scikit-learn) {Best}
7. XGBoost (Scikit-learn)
8. Artificial Neural Network with 1 Hidden layer (Keras) {Best when the dataset is large}

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

1. Enter patient medical details in the dashboard

2. Click Predict & Forward Report

3. View prediction result (High Risk / Low Risk)

4. Report gets automatically sent via email

📧 Email Configuration

✅ STEP 1: Turn ON 2-Step Verification

1. Go to 👉 https://myaccount.google.com/security
2. Find 2-Step Verification
3. Turn it ON


✅ STEP 2: Generate App Password

1. Go to 👉 https://myaccount.google.com/apppasswords
2. Click Generate
3. You’ll get a 16-digit password
   
👉 Example: abcdefghijklmnop

Update sender email credentials in app.py:

SENDER_EMAIL = "your_email@gmail.com"

SENDER_PASS = "your_app_password"

Use Google App Password, not your normal password.

📊 Input Features
1. Age
2. Sex
3. Chest Pain Type
4. Resting Blood Pressure
5. Cholesterol
6. Fasting Blood Sugar
7. ECG Results
8. Maximum Heart Rate
9. Exercise-Induced Angina
10. Oldpeak
11. Slope
12. Number of Major Vessels
13. Thalassemia

⚠️ Disclaimer

This project is for educational purposes only and should not be used as a substitute for professional medical advice.

👨‍💻 Author

Sanjeeb Kumar Mishra

GitHub: https://github.com/iamsanjeebmishra

LinkedIn: https://linkedin.com/in/iamsanjeebmishra

⭐ Contribution

Feel free to fork this repository and contribute!

