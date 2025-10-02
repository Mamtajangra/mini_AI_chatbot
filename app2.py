import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from dotenv import load_dotenv
import os

# Load env
load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI model
model = ChatOpenAI(
    model_name="gpt-3.5-turbo",
   temperature=0,
    openai_api_key=openai_key
)

# Multi-turn memory
memory = ConversationBufferMemory(return_messages=True)
conversation = ConversationChain(llm=model, memory=memory, verbose=False)

# Streamlit UI
st.title("AI Q&A Chatbot (OpenAI)")
user_input = st.text_input("Ask me anything:")

if st.button("Send") and user_input:
    response = conversation.run(user_input)
    st.write("AI:", response)
