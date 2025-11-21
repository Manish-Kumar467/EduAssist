import streamlit as st
from io import BytesIO
import docx2txt
import PyPDF2
import tempfile
import whisper  # for video transcription
from transformers import pipeline

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="EduAssist Summarisation",
    page_icon="📝",
    layout="wide"
)

st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

st.title("📝 Summarisation Module")
st.write("Upload a PDF, Word document, text file, or a video to generate a summary.")

# -----------------------------
# File uploader
# -----------------------------
uploaded_file = st.file_uploader(
    "Upload your file",
    type=["pdf", "docx", "txt", "mp4", "mkv", "mov", "avi"]
)

if uploaded_file is not None:
    file_type = uploaded_file.name.split(".")[-1].lower()
    raw_text = ""

    # -----------------------------
    # Process PDF
    # -----------------------------
    if file_type == "pdf":
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        for page in pdf_reader.pages:
            raw_text += page.extract_text() + "\n"

    # -----------------------------
    # Process Word document
    # -----------------------------
    elif file_type == "docx":
        raw_text = docx2txt.process(uploaded_file)

    # -----------------------------
    # Process text file
    # -----------------------------
    elif file_type == "txt":
        raw_text = uploaded_file.read().decode("utf-8")

    # -----------------------------
    # Process video
    # -----------------------------
    elif file_type in ["mp4", "mkv", "mov", "avi"]:
        st.info("Transcribing video... this may take a while depending on length.")
        # Save to temp file
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name
        
        # Load Whisper model
        model = whisper.load_model("base")  # you can use "small" for faster speed
        result = model.transcribe(tmp_path)
        raw_text = result["text"]

    else:
        st.error("Unsupported file type!")
        st.stop()

    st.subheader("Extracted Text")
    st.text_area("Preview text:", raw_text, height=200)

    # -----------------------------
    # Summarization
    # -----------------------------
    st.subheader("Summary")

    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")  # HuggingFace model

    if len(raw_text.split()) > 1024:
        # Chunk text if too long
        max_chunk = 1024
        chunks = [raw_text[i:i+max_chunk] for i in range(0, len(raw_text), max_chunk)]
        summary_text = ""
        for chunk in chunks:
            summary = summarizer(chunk, max_length=150, min_length=40, do_sample=False)[0]["summary_text"]
            summary_text += summary + " "
    else:
        summary_text = summarizer(raw_text, max_length=150, min_length=40, do_sample=False)[0]["summary_text"]

    st.success(summary_text)

# -----------------------------
# Back button
# -----------------------------
if st.button("⬅️ Back to Home"):
    st.switch_page("pages/1_Home.py")
