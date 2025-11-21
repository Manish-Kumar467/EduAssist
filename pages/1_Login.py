import streamlit as st

def login():
    st.title("🔐 EduAssist Login")
    st.write("Enter your admin credentials to continue.")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "1234":
            st.session_state["logged_in"] = True
            st.success("Login successful!")
            st.rerun()  # Updated here
        else:
            st.error("Invalid username or password")

# --------- PAGE ENTRY ----------
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    login()
else:
    st.success("Already logged in!")
    st.write("Go to sidebar and select a page.")
