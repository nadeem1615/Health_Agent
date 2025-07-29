import streamlit as st
from services.health_analysis import analyze_symptoms
from database.db_connection import get_connection

def show_analysis_form():
    st.subheader("Enter your symptoms")
    symptoms = st.text_area("Symptoms")

    if st.button("Analyze"):
        result = analyze_symptoms(symptoms)
        st.success(f"Analysis: {result}")

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO health_analysis (user_email, symptoms, analysis) VALUES (%s, %s, %s)",
            (st.session_state.user['email'], symptoms, result)
        )
        conn.commit()