import streamlit as st
from dotenv import load_dotenv

from rag.pdf import get_pdf_text
from rag.text_splitter import get_text_chunks
from rag.vectorstore import get_vectorstore
from rag.chain import get_conversation_chain
from handlers.chat import handle_userinput

from htmlTemplates import css

def main():
    load_dotenv()

    st.set_page_config(
        page_title="Document Q&A",
        page_icon="📄",
        layout="wide"
    )

    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None

    st.header("Chat with PDFs")

    user_question = st.text_input(
        "Ask",
        placeholder="Type your question here...",
        label_visibility="collapsed"
    )

    if user_question:
        handle_userinput(user_question)

    with st.sidebar:
        st.subheader("Documents")

        docs = st.file_uploader(
            "Upload",
            label_visibility="collapsed",
            accept_multiple_files=True
        )

        if st.button("Process"):
            if docs:
                with st.spinner("Processing..."):
                    raw_text = get_pdf_text(docs)
                    text_chunks = get_text_chunks(raw_text)

                    vector_store = get_vectorstore(text_chunks)
                    conversation = get_conversation_chain(vector_store)

                    st.session_state.conversation = conversation
            else:
                st.warning("Please upload at least one PDF.")

if __name__ == '__main__':
    main()