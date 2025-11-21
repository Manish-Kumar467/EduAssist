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

st.title("🏠 EduAssist Home")
st.write("Welcome! Choose a module to continue:")

col1, col2 = st.columns(2)

with col1:
    if st.button("📝 Summarisation Module"):
        st.switch_page("pages/2_Summarization.py")  # ✅ relative to main script

with col2:
    if st.button("❓ Question Generation"):
        st.switch_page("pages/3_Question_Generation.py")  # ✅ relative to main script

if st.button("🚪 Logout"):
    st.session_state["logged_in"] = False
    st.switch_page("streamlit_app.py")  # ✅ relative path to main script
