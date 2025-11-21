import streamlit as st
from utils import init_session

init_session()

if not st.session_state["logged_in"]:
    st.switch_page("streamlit_app")

st.title("📝 Summarization Module")
st.write("Enter educational content to generate a summary.")

text = st.text_area("Enter text to summarize:")

if st.button("Generate the Summary"):
    st.success("Summary will appear here (model integration pending).")
