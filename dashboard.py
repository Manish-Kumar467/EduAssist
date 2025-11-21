import streamlit as st
from utils import logout, init_session

init_session()

if not st.session_state["logged_in"]:
    st.switch_page("streamlit_app")

st.sidebar.title("📚 EduAssist Navigation")
st.sidebar.page_link("dashboard", label="🏠 Dashboard")
st.sidebar.page_link("pages/Summarization", label="📝 Summarization")
st.sidebar.page_link("pages/Question_Generation", label="❓ Question Generation")

if st.sidebar.button("🚪 Logout"):
    logout()
    st.switch_page("streamlit_app")

st.title("🏠 EduAssist Dashboard")
st.write("Welcome to EduAssist – Your AI-powered education assistant.")

st.info("Use the navigation menu on the left to access different features.")
