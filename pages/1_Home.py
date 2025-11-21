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

    /* Navbar style */
    .navbar {
        background-color: #4B4BFF;
        padding: 15px 30px;
        border-radius: 10px;
        display: flex;
        justify-content: space-around;
        align-items: center;
        margin-bottom: 40px;
        color: white;
        font-weight: bold;
        font-size: 18px;
    }
    .navbar button {
        background-color: transparent;
        border: none;
        color: white;
        font-size: 16px;
        cursor: pointer;
        transition: 0.2s;
        padding: 10px 20px;
        border-radius: 5px;
    }
    .navbar button:hover {
        background-color: rgba(255,255,255,0.2);
    }

    /* Card style with fade-in */
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
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    .card h2 { font-size: 24px; margin-bottom: 10px; }
    .card p { font-size: 16px; color: #555; }
    </style>
""", unsafe_allow_html=True)

# -----------------------------
# Navbar Simulation
# -----------------------------
st.markdown(
    """
    <div class="navbar">
        <button onclick="window.location.href='#'">🏠 Home</button>
        <button onclick="window.location.href='#summarization'">📝 Summarization</button>
        <button onclick="window.location.href='#question'">❓ Question Generation</button>
        <button onclick="window.location.href='#logout'">🚪 Logout</button>
    </div>
    """, unsafe_allow_html=True
)

# -----------------------------
# Page Title
# -----------------------------
st.markdown("<h1 style='text-align: center; color: #4B4BFF;'>Welcome to EduAssist 🎓</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size:18px;'>Select a module from above or scroll down to explore.</p>", unsafe_allow_html=True)
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
        "page": None  # Optional
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
# Buttons at the bottom for navigation
# -----------------------------
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("📝 Go to Summarization"):
        st.switch_page("2_Summarization")

with col2:
    if st.button("❓ Go to Question Generation"):
        st.switch_page("3_Question_Generation")

with col3:
    if st.button("🚪 Logout"):
        st.session_state["logged_in"] = False
        st.switch_page("streamlit_app")
