import streamlit as st
from auth.session_manager import login

def show_login_page():
    st.title("Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if login(email, password):
            st.success("Login successful. Please rerun the app.")
        else:
            st.error("Invalid credentials")