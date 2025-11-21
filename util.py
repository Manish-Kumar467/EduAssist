import streamlit as st

def init_session():
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

def login(username, password):
    # TEMP LOGIN: replace with database credentials later
    if username == "admin" and password == "1234":
        st.session_state["logged_in"] = True
        return True
    return False

def logout():
    st.session_state["logged_in"] = False
