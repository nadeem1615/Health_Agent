import streamlit as st
from auth.session_manager import logout

def show_sidebar():
    with st.sidebar:
        st.header("Navigation")
        page = st.radio("Go to", ["Analysis", "History"])
        st.session_state["page"] = page.lower()

        st.write("---")
        if st.button("Logout"):
            logout()
            st.experimental_rerun()