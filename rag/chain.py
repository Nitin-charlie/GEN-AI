from langchain_classic.memory import ConversationBufferMemory
from langchain_classic.chains.conversational_retrieval.base import ConversationalRetrievalChain
from langchain_groq import ChatGroq
from langchain_classic.prompts import PromptTemplate

from rag.prompt import get_prompt

prompt = PromptTemplate(
    template=get_prompt(),
    input_variables=["context", "question"]
)

def get_conversation_chain(vector_store):
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0,
    )

    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True,
        output_key="answer"
    )

    return ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vector_store.as_retriever(),
        memory=memory,
        combine_docs_chain_kwargs={"prompt": prompt},
        return_source_documents=True
    )