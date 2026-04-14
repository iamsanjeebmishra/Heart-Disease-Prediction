import streamlit as st
import pandas as pd
import pickle
import numpy as np
import smtplib
from email.message import EmailMessage

# ==========================================
# 1. EMAIL CONFIGURATION
# ==========================================

SENDER_EMAIL = "mrsanjeebkumar@gmail.com"
SENDER_PASS = "xeloeekasizimuzv"  # 16-digit code from Google App Passwords


def send_combined_report(dr_email, pt_email, subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = SENDER_EMAIL
    msg['To'] = f"{dr_email}, {pt_email}"

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(SENDER_EMAIL, SENDER_PASS)
            server.send_message(msg)
        return True
    except Exception as e:
        st.sidebar.error(f"Mail Error: {e}")
        return False


# ==========================================
# 2. LOAD TRAINED MODEL
# ==========================================
try:
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error("CRITICAL ERROR: 'model.pkl' not found! Please place it in the same folder.")

# ==========================================
# 3. DASHBOARD UI SETUP
# ==========================================
st.set_page_config(page_title="Heart Disease Analysis", layout="wide")
st.title("❤️ Heart Disease Clinical Dashboard")
st.markdown("---")

# Sidebar for Contact Details
st.sidebar.header("📧 Report Forwarding")
doctor_email = st.sidebar.text_input("Doctor's Email ID", placeholder="dr_name@hospital.com")
patient_email = st.sidebar.text_input("Patient's Email ID", placeholder="patient@example.com")
st.sidebar.info("The report will be sent to both email IDs upon prediction.")

# ==========================================
# 4. STRICT PARAMETER INPUT FORM
# ==========================================
with st.form("clinical_input_form"):
    st.subheader("Patient Medical Data (Strict Input)")

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input("Age (example: 52) → Integer", min_value=1, max_value=120, value=52)
        sex = st.selectbox("Sex (1 = Male, 0 = Female)", options=[1, 0])
        cp = st.selectbox("Chest Pain Type (0–3) → 0=typical, 1=atypical, 2=non-anginal, 3=asymptomatic",
                          options=[0, 1, 2, 3])
        trestbps = st.number_input("Resting Blood Pressure in mmHg (example: 130)", value=130)
        chol = st.number_input("Serum Cholesterol in mg/dl (example: 230)", value=230)

    with col2:
        fbs = st.selectbox("Fasting Blood Sugar >120 mg/dl (1=True, 0=False)", options=[1, 0])
        restecg = st.selectbox("Resting ECG (0=normal, 1=ST-T abnormality, 2=LV hypertrophy)", options=[0, 1, 2])
        thalach = st.number_input("Maximum Heart Rate Achieved (example: 150)", value=150)
        exang = st.selectbox("Exercise-Induced Angina (1=Yes, 0=No)", options=[1, 0])

    with col3:
        oldpeak = st.number_input("Oldpeak (ST depression, example: 1.4) → Decimal", value=1.4, format="%.1f")
        slope = st.selectbox("Slope of ST Segment (0=up, 1=flat, 2=down)", options=[0, 1, 2])
        ca = st.selectbox("Number of Major Vessels (0–3)", options=[0, 1, 2, 3])
        thal = st.selectbox("Thalassemia (1=normal, 2=fixed defect, 3=reversible defect)", options=[1, 2, 3])

    # Submit Button
    submit = st.form_submit_button("Predict & Forward Report")

# ==========================================
# 5. PREDICTION & OUTPUT LOGIC
# ==========================================
if submit:
    # Creating DataFrame to match backend training columns exactly
    columns = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg',
               'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']

    new_data = [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
    new_df = pd.DataFrame(new_data, columns=columns)

    # Prediction
    prediction = model.predict(new_df)

    # Calculate Chances (Probability)
    try:
        prob = model.predict_proba(new_df)
        chances = np.max(prob) * 100
    except:
        chances = 100.0 if prediction[0] == 1 else 0.0

    st.markdown("---")
    st.subheader("===== FINAL PREDICTION RESULT =====")

    # Formatting text for display and email
    if prediction[0] == 1:
        status_text = "🔴 HIGH RISK: Patient likely has HEART DISEASE"
        st.error(f"{status_text} (Chance: {chances:.2f}%)")
    else:
        status_text = "🟢 LOW RISK: Patient does NOT have heart disease"
        st.success(f"{status_text} (Chance: {chances:.2f}%)")

    # ==========================================
    # 6. REPORT SENDING & SUCCESS MESSAGE
    # ==========================================
    if doctor_email and patient_email:
        report_body = f"""
        HEART DISEASE CLINICAL ANALYSIS REPORT
        --------------------------------------
        RESULT: {status_text}
        CHANCES/PROBABILITY: {chances:.2f}%

        PATIENT PARAMETERS:
        Age: {age}, Sex: {sex}, Chest Pain: {cp}, BP: {trestbps}, 
        Cholesterol: {chol}, Max Heart Rate: {thalach}, ST Depression: {oldpeak}

        This is an automated diagnostic reference forwarded to the healthcare provider and patient.
        """

        with st.spinner("Processing clinical report and mailing..."):
            mail_success = send_combined_report(doctor_email, patient_email, "Urgent: Heart Risk Assessment Report",
                                                report_body)

        if mail_success:
            # THE SUCCESS CONFIRMATION
            st.balloons()
            st.success("✅ **Report sent successfully to the provided email addresses!**")
            st.write(f"Confirmed delivery to Doctor: **{doctor_email}**")
            st.write(f"Confirmed delivery to Patient: **{patient_email}**")
        else:
            st.error("❌ Prediction complete, but email delivery failed. Check your App Password.")
    else:
        st.warning("⚠️ Prediction generated. To send the report, please fill in both Email IDs in the sidebar.")