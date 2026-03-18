# 📄 GenAI Project: PDF Question Answering System

## 1. Introduction
This project presents a Generative AI-based system that allows users to upload a PDF document and ask questions related to its content. The system processes the document and provides accurate answers using modern AI techniques.

---

## 2. Objective
The main objective is to build an intelligent system that can understand and extract information from documents and respond to user queries effectively.

---

## 3. Methodology
The project uses **Retrieval-Augmented Generation (RAG)**. The workflow includes:

- Uploading a PDF  
- Extracting text  
- Splitting text into chunks  
- Converting text into embeddings  
- Storing embeddings in a vector database  
- Retrieving relevant information  
- Generating answers using a language model  

---

## 4. Tools and Technologies Used

- Python  
- Streamlit (Frontend)  
- LangChain (Framework)  
- FAISS (Vector Database)  
- Llama 3 via Ollama (LLM)  

---

## 5. System Architecture


User → Streamlit UI → PDF Loader → Text Splitter → Embeddings → FAISS → Retriever → LLM → Answer


---

## 6. Working of the System

1. The user uploads a PDF through the interface.  
2. The system processes the document and converts it into vector embeddings.  
3. When a user asks a question, the system retrieves relevant information.  
4. The LLM generates an answer based on the retrieved data.  

---

## 7. Advantages

- Works offline (using Llama)  
- Fast document search  
- Accurate answers  
- Easy to use interface  

---

## 8. Conclusion

This project demonstrates how Generative AI can be used to build intelligent document-based question answering systems. It highlights the power of RAG and LLMs in real-world applications.