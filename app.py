import streamlit as st
from auth.session_manager import SessionManager
from components.auth_pages import show_login_page
from components.sidebar import show_sidebar
from components.analysis_form import show_analysis_form
from components.history_page import show_history_page
from config.app_config import APP_NAME, APP_ICON, APP_DESCRIPTION

st.set_page_config(page_title=APP_NAME, page_icon=APP_ICON, layout="wide")

SessionManager.init_session()

if not SessionManager.is_authenticated():
    show_login_page()
else:
    show_sidebar()
    st.title(f"{APP_ICON} {APP_NAME}")
    st.subheader(APP_DESCRIPTION)

    page = st.session_state.get("page", "analysis")

    if page == "analysis":
        show_analysis_form()
    elif page == "history":
        show_history_page()