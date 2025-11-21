import streamlit as st

st.title("🏠 EduAssist Home")
st.write("Welcome! Choose a module to continue:")

col1, col2 = st.columns(2)

with col1:
    if st.button("📝 Summarisation Module"):
        st.switch_page("2_Summarization")  # ✅ No '.py', no 'pages/'

with col2:
    if st.button("❓ Question Generation"):
        st.switch_page("3_Question_Generation")  # ✅ No '.py', no 'pages/'

if st.button("🚪 Logout"):
    st.session_state["logged_in"] = False
    st.switch_page("streamlit_app")  # ✅ file name without '.py'
