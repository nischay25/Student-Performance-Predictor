from pathlib import Path

import joblib
import streamlit as st

base_dir = Path(__file__).resolve().parent
model = joblib.load(base_dir / "student_performance_model.pkl")
scaler = joblib.load(base_dir / "scaler.pkl")

st.title("Student Performance Prediction")

gender = st.selectbox("Gender", ["Male", "Female"])
hours = st.number_input("Hours Studied per Week", min_value=0)
tutoring = st.selectbox("Tutoring", ["Yes", "No"])
region = st.selectbox("Region", ["Urban", "Suburban", "Rural"])
attendance = st.slider("Attendance (%)", 0, 100, 90)
parent_education = st.selectbox(
    "Parent Education",
    ["High School", "Graduate", "Postgraduate"]
)

if st.button("Predict"):
    try:
        # Convert categorical values to numeric
        gender_value = 1 if gender == "Male" else 0
        tutoring_value = 1 if tutoring == "Yes" else 0

        region_map = {
            "Urban": 0,
            "Suburban": 1,
            "Rural": 2,
        }
        region_value = region_map[region]

        parent_map = {
            "High School": 1,
            "Graduate": 2,
            "Postgraduate": 3,
        }
        parent_value = parent_map[parent_education]

        new_student = [[
            gender_value,
            float(hours),
            tutoring_value,
            region_value,
            float(attendance),
            parent_value,
        ]]

        new_student_scaled = scaler.transform(new_student)
        prediction = model.predict(new_student_scaled)

        st.success(f"Predicted Exam Score: {prediction[0]:.2f}")
    except Exception as exc:
        st.error(f"Prediction failed: {exc}")