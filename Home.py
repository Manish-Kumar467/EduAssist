import streamlit as st
from utils import logout, init_session

init_session()

if not st.session_state["logged_in"]:
    st.switch_page("streamlit_app.py")

st.sidebar.title("📚 EduAssist Navigation")
st.sidebar.page_link("Home.py", label="🏠 Dashboard")
st.sidebar.page_link("Summarization.py", label="📝 Summarization")
st.sidebar.page_link("Question_Generation.py", label="❓ Question Generation")

if st.sidebar.button("🚪 Logout"):
    logout()
    st.switch_page("streamlit_app.py")

st.title("🏠 EduAssist Dashboard")
st.write("Welcome to EduAssist – Your AI-powered education assistant.")

st.info("Use the navigation menu on the left to access different features.")
