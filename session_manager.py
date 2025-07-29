import streamlit as st

class SessionManager:
    @staticmethod
    def init_session():
        if "authenticated" not in st.session_state:
            st.session_state["authenticated"] = False
            st.session_state["user"] = None

    @staticmethod
    def is_authenticated():
        return st.session_state.get("authenticated", False)

    @staticmethod
    def login(email, password):
        if email == "user@example.com" and password == "password":
            st.session_state["authenticated"] = True
            st.session_state["user"] = {"email": email}
            return True
        return False

    @staticmethod
    def logout():
        st.session_state["authenticated"] = False
        st.session_state["user"] = None