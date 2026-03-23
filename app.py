import streamlit as st

def main():
    st.set_page_config(page_title = "Document Q&A")
    st.header("Document Q&A")
    st.text_input("Ask")

    with st.sidebar:
        st.subheader("Documents")
        st.file_uploader("Upload")
        st.button("Process")

if __name__ == '__main__':
    main()