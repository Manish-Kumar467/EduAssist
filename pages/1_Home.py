import streamlit as st

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="EduAssist",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -----------------------------
# Hide default Streamlit UI
# -----------------------------
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Custom card style */
    .card {
        background-color: #f0f2f6;
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        transition: transform 0.2s;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .card:hover {
        transform: scale(1.05);
        box-shadow: 0 8px 16px rgba(0,0,0,0.2);
    }
    .card h2 {
        font-size: 28px;
        margin-bottom: 10px;
    }
    .card p {
        font-size: 16px;
        color: #555;
    }
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# -----------------------------
# Page Title
# -----------------------------
st.markdown("<h1 style='text-align: center; color: #4B4BFF;'>🏠 EduAssist Home</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size:18px;'>Welcome! Choose a module to continue:</p>", unsafe_allow_html=True)
st.write("---")

# -----------------------------
# Module Cards
# -----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📝 Summarisation Module", key="sum"):
        st.switch_page("pages/2_Summarization.py")  # Page name only

with col2:
    if st.button("❓ Question Generation", key="qgen"):
        st.switch_page("pages/3_Question_Generation.py")  # Page name only

with col3:
    if st.button("🚪 Logout", key="logout"):
        st.session_state["logged_in"] = False
        st.switch_page("streamlit_app")  # Main login page

# -----------------------------
# Optional: Add image or illustration
# -----------------------------
st.markdown(
    """
    <div style='text-align:center; margin-top:40px;'>
        <img src='https://img.icons8.com/external-flaticons-lineal-color-flat-icons/64/000000/external-education-online-learning-flaticons-lineal-color-flat-icons.png' 
        alt='EduAssist' style='width:150px; height:auto;'>
    </div>
    """, unsafe_allow_html=True
)
