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
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Remove Streamlit top padding */
.block-container {
    padding-top: 0rem;
}

/* Website-style navbar */
.navbar {
    width: 100%;
    background-color: #4B4BFF;
    padding: 1rem 2rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: sticky;
    top: 0;
    z-index: 100;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}

/* Navbar links */
.navbar a {
    color: white;
    text-decoration: none;
    font-size: 18px;
    font-weight: bold;
    margin: 0 15px;
    padding: 8px 15px;
    border-radius: 8px;
    transition: 0.3s;
}

.navbar a:hover {
    background-color: rgba(255,255,255,0.2);
}

/* Card style */
.card {
    background-color: #f0f2f6;
    padding: 30px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    margin-bottom: 30px;
    opacity: 0;
    transform: translateY(50px);
    animation: fadeInUp 0.8s forwards;
}
@keyframes fadeInUp {
    to { opacity:1; transform: translateY(0); }
}
.card h2 { font-size: 24px; margin-bottom: 10px; }
.card p { font-size: 16px; color: #555; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="navbar">
    <div class="nav-left">
        <a href="#home" id="home">🏠 Home</a>
    </div>
    <div class="nav-right">
        <a href="pages/2_summarization.py" id="summarization">📝 Summarization</a>
        <a href="#question" id="question">❓ Question Generation</a>
        <a href="#logout" id="logout">🚪 Logout</a>
    </div>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# Navbar using Streamlit buttons
# -----------------------------
st.markdown("<div class='navbar'>", unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns([1,1,1,1])

with col1:
    if st.button("🏠 Home" ):
        st.switch_page("pages/1_Home.py")
        

with col2:
    if st.button("📝 Summarization"):
        st.switch_page("pages/2_Summarization.py")

with col3:
    if st.button("❓ Question Generation"):
        st.switch_page("pages/3_Question_Generation.py")

with col4:
    if st.button("🚪 Logout"):
        st.session_state["logged_in"] = False
        st.switch_page("streamlit_app.py")
st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# Page Title
# -----------------------------
st.markdown("<h1 style='text-align: center; color: #4B4BFF;'>Welcome to EduAssist 🎓</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size:18px;'>Select a module below to get started.</p>", unsafe_allow_html=True)
st.write("---")

# -----------------------------
# Module Cards
# -----------------------------
modules = [
    {
        "title": "📝 Summarization Module",
        "desc": "Automatically summarize long documents or articles into concise summaries.",
        "page": "2_Summarization"
    },
    {
        "title": "❓ Question Generation",
        "desc": "Generate relevant questions from any text to aid in learning or quizzes.",
        "page": "3_Question_Generation"
    },
    {
        "title": "📊 Analytics Dashboard",
        "desc": "Track your learning progress and module usage statistics.",
        "page": None
    }
]

for module in modules:
    st.markdown(f"""
        <div class="card">
            <h2>{module['title']}</h2>
            <p>{module['desc']}</p>
        </div>
    """, unsafe_allow_html=True)

# -----------------------------
# Optional bottom buttons for navigation
# -----------------------------

