import streamlit as st
import streamlit as st

# Hide Streamlit default UI elements
st.set_page_config(
    page_title="EduAssist",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide hamburger and footer using custom CSS
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

def login():
    st.title("🔐 EduAssist Login")
    st.write("Enter your admin credentials to continue.")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "1234":
            st.session_state["logged_in"] = True
            st.switch_page("pages/1_Home.py")  # ✅ no leading slash
        else:
            st.error("Invalid username or password")

# --------- PAGE ENTRY ----------
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    login()
else:
    st.switch_page("pages/1_Home.py")  # ✅ same relative path
