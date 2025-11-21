import streamlit as st

def summarization_page():
    st.title("📝 Text Summarization")

    text = st.text_area("Enter text for summarization", height=200)

    if st.button("Summarize"):
        if text.strip() == "":
            st.warning("Please enter some text.")
        else:
            words = text.split()
            summary = " ".join(words[:len(words)//2]) + " ..."
            st.subheader("Summary:")
            st.write(summary)

# --------- PAGE RESTRICTION ----------
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.error("Please login first!")
    st.stop()

summarization_page()
