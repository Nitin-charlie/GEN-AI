import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_classic.memory import ConversationBufferMemory
from langchain_classic.chains.conversational_retrieval.base import ConversationalRetrievalChain
from htmlTemplates import css, bot_template, user_template

def get_pdf_text(docs):
    text = ""
    for pdf in docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
            #print("page text:",text);
    return text

def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", " ", ""], 
        chunk_size = 1000, chunk_overlap = 200, length_function = len)
    chunks = text_splitter.split_text(text)
    return chunks

def get_vectorstore(text_chunks):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_texts(texts = text_chunks, embedding = embeddings)
    return vectorstore
    
def get_conversation_chain(vector_store):
    llm = ChatOpenAI()
    memory = ConversationBufferMemory(memory_key = "chat_history", return_message = True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm = llm,
        retriever = vector_store.as_retriever(),
        memory = memory
    )
    return conversation_chain

def main():
    load_dotenv()
    st.set_page_config(
        page_title="Document Q&A",
        page_icon="📄",
        layout="wide"
    )
    st.write(css, unsafe_allow_html= True)
        
    if("conversation" not in st.session_state):
        st.session_state.conversation = None

    st.header("Chat with PDFs")
    st.text_input("Ask", placeholder="Type your question here...", label_visibility="collapsed")

    st.write(user_template.replace("{{MSG}}", "Hello Robot"), unsafe_allow_html= True)
    st.write(bot_template.replace("{{MSG}}", "Hello Human"), unsafe_allow_html= True)

    with st.sidebar:
        st.subheader("Documents")
        
        docs = st.file_uploader("Upload", label_visibility="collapsed", accept_multiple_files = True)
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