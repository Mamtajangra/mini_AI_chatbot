import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from dotenv import load_dotenv
import os

# Load env
load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)
memory = ConversationBufferMemory(return_messages=True)
conversation = ConversationChain(llm=model, memory=memory, verbose=False)

# Streamlit UI
st.title("AI Q&A Chatbot")       ## give the title to chatbot

user_input = st.text_input("Ask me anything:")      ## a box where user will type his/her query

if st.button("Send"):                               ## a send button to send input to the model 
    response = conversation.run(user_input)          ## get response
    st.write("AI:", response)                       ## ai response will appear on the display
