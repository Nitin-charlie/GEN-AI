import streamlit as st
from htmlTemplates import bot_template, user_template

def handle_userinput(user_question):
    if st.session_state.conversation is None:
        st.info("Please upload your PDFs and click 'Process' to start the chat.")
        return
    
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)

    if "source_documents" in response:
        with st.expander("📄 View Sources"):
            for i, doc in enumerate(response["source_documents"]):
                st.markdown(f"**Chunk {i+1}:**")
                st.write(doc.page_content[:300])