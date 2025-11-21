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

st.title("📝 Summarisation Module")
st.write("This is where your summarisation logic will go.")

if st.button("⬅️ Back to Home"):
    st.switch_page("/4_Home.py")
