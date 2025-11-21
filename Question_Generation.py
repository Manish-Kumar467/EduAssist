import streamlit as st
from utils import init_session

init_session()

if not st.session_state["logged_in"]:
    st.switch_page("streamlit_app.py")

st.title("❓ Question Generation Module")
st.write("Enter content to generate questions.")

text = st.text_area("Enter text:")

if st.button("Generate Questions"):
    st.success("Questions will appear here (model integration pending).")
