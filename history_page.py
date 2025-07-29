import streamlit as st
from database.db_connection import get_connection

def show_history_page():
    st.subheader("Your Health Analysis History")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT symptoms, analysis, created_at FROM health_analysis WHERE user_email = %s ORDER BY created_at DESC", (st.session_state.user['email'],))
    rows = cursor.fetchall()

    for r in rows:
        st.info(f"Symptoms: {r[0]}\n\nAnalysis: {r[1]}\n\nDate: {r[2]}")