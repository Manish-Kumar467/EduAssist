import streamlit as st
from utils import init_session, login

st.set_page_config(page_title="EduAssist Login", page_icon="🎓", layout="centered")

init_session()

if st.session_state["logged_in"] is True:
    st.switch_page("dashboard")

st.title("🔐 Login to EduAssist")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if login(username, password):
        st.success("Login successful!")
        st.switch_page("dashboard")
    else:
        st.error("Invalid username or password")
