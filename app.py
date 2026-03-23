import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader

def get_pdf_text(docs):
    text = ""
    for pdf in docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text


def main():
    
    load_dotenv()
    st.set_page_config(
        page_title="Document Q&A",
        page_icon="📄",
        layout="wide"
    )

    st.markdown("""
        <style>
        .stApp {
            background-color: #0b1020;
            color: white;
        }

        .main-title {
            font-size: 48px;
            font-weight: 700;
            color: white;
            margin-top: 30px;
            margin-bottom: 20px;
        }

        .ask-label {
            font-size: 20px;
            font-weight: 500;
            color: #d1d5db;
            margin-bottom: 8px;
        }

        .stTextInput > div > div > input {
            background-color: #1f2937;
            color: white;
            border: 1px solid #374151;
            border-radius: 12px;
            padding: 14px;
            font-size: 16px;
        }

        .stTextInput > div > div > input:focus {
            border: 1px solid #6366f1;
            box-shadow: 0 0 0 1px #6366f1;
        }

        section[data-testid="stSidebar"] {
            background-color: #1f2430;
        }

        section[data-testid="stSidebar"] h2,
        section[data-testid="stSidebar"] h3,
        section[data-testid="stSidebar"] label,
        section[data-testid="stSidebar"] p,
        section[data-testid="stSidebar"] div {
            color: white !important;
        }

        .upload-box {
            background-color: #111827;
            border: 1px dashed #4b5563;
            border-radius: 14px;
            padding: 18px;
            text-align: center;
            margin-bottom: 20px;
        }

        .upload-text {
            font-size: 16px;
            font-weight: 500;
            color: white;
        }

        .upload-subtext {
            font-size: 13px;
            color: #9ca3af;
        }
        </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2.2, 1])

    with col2:
        st.markdown('<div class="main-title">Document Q&A</div>', unsafe_allow_html=True)
        st.markdown('<div class="ask-label">Ask</div>', unsafe_allow_html=True)
        st.text_input("Ask", placeholder="Type your question here...", label_visibility="collapsed")

    with st.sidebar:
        st.subheader("Documents")

        docs = st.file_uploader("Upload", label_visibility="collapsed", accept_multiple_files = True)
        if st.button("Process"):
            st.spinner("Processing")
            raw_text = get_pdf_text(docs)
            st.write(raw_text)

if __name__ == '__main__':
    main()