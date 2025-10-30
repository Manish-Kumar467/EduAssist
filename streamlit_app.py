import streamlit as st

st.set_page_config(page_title="EduAssist", page_icon="🎓", layout="wide")

st.title("🎓 EduAssist – AI-Powered Learning Assistant")
st.write("Welcome! This is a test deployment of your Streamlit app.")
st.write("If you see this message, your app is running correctly!")

text = st.text_area("Enter some text to summarize:")
if st.button("Summarize"):
    st.write("👉 Summary will appear here.")
