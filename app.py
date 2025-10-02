import streamlit as st
from langchain.chat_models import init_chat_model
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from dotenv import load_dotenv
import os

# Load env
load_dotenv()

# Initialize model & memory
model = init_chat_model(model="gemini-2.0-flash", model_provider="google_genai")
memory = ConversationBufferMemory(return_messages=True)
conversation = ConversationChain(llm=model, memory=memory, verbose=False)

# Streamlit UI
st.title("AI Q&A Chatbot")       ## give the title to chatbot

user_input = st.text_input("Ask me anything:")      ## a box where user will type his/her query

if st.button("Send"):                               ## a send button to send input to the model 
    response = conversation.run(user_input)          ## get response
    st.write("AI:", response)                       ## ai response will appear on the display
