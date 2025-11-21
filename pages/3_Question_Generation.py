import streamlit as st

def question_gen_page():
    st.title("❓ Question Generator")

    text = st.text_area("Enter content to generate questions", height=200)

    if st.button("Generate Questions"):
        if text.strip() == "":
            st.warning("Please enter some text.")
        else:
            st.subheader("Generated Questions:")
            st.write("1. What is the main idea of the text?")
            st.write("2. What are the key points discussed?")
            st.write("3. How would you summarise this passage?")
            st.write("4. Why is this topic important?")

# --------- PAGE RESTRICTION ----------
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.error("Please login first!")
    st.stop()

question_gen_page()
