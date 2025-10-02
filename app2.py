import streamlit as st
from langchain_community.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from dotenv import load_dotenv
import os

load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")
openai_base = os.getenv("OPENAI_API_BASE")

model = ChatOpenAI(
    model_name="openrouter/auto",
    temperature=0,
    openai_api_key=openai_key,
    openai_api_base=openai_base
)

memory = ConversationBufferMemory(return_messages=True)
conversation = ConversationChain(llm=model, memory=memory, verbose=False)

st.title("AI Q&A Chatbot (OpenRouter)")
user_input = st.text_input("Ask me anything:")

if st.button("Send") and user_input:
    response = conversation.run(user_input)
    st.write("AI:", response)
