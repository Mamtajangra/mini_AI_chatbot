##  init_chat_model =  langchain se ek helpful function initialize kiya jo correct  LLM ko load karega 
## Memory class import ki=  Ye chat ki history yaad rakhega — jaise "buffer" me pehle ke messages store karna.
## ConversationChain import ki = Ye LLM + Memory ko combine karke ready-to-use chatbot pipeline banata hai.
## environmental varialble ko load kiya gemini api ke liye
## operating system ko import kiya
## model choose kiya aur provider ka naam diya 
## Chat history ko store karte hai.
## phir LLM + Memory ko combine karte hai.
## stop nahi karenge to model infinite loop pe chalta rahega so while loop jb user quit,stop dega tab chatbot stop ho jaayega
## User ka message + memory (previous chat history) → AI model ko jaata hai.
## run karke output obtain karlete hai 
 #### this model is able to remember memory .




from langchain.chat_models import init_chat_model     ## helpful function import kiya langchain se to load llm
from langchain.memory import ConversationBufferMemory   ##  ye memory ko yaad rkhne ke liye hota hai 
from langchain.chains import ConversationChain         ## conversation chain import kri ye llm or memory combine karega
from dotenv import load_dotenv 
import os

# Load environment variables
load_dotenv()                       ## env load karli

# Initialize Gemini model
model = init_chat_model(model="gemini-2.0-flash", model_provider="google_genai")  ## model ka name or provider diya

# Initialize memory
memory = ConversationBufferMemory(return_messages=True)   
'''Chatbot ko pehle ki baatein yaad rakhne ke liye.
Ye basically ek “buffer” ya “notebook” jaisa hai.
Jab tum agla question puchte ho, AI pichli baatein dekh sakta hai.
Without memory → AI sirf current input dekhega aur context lose ho jaayega.'''

## return_message = true because ConversationBufferMemory me messages string format me store hote hain,ye true isko list mein convert kar deta hai 
## jisse ai ko easy ho jaaye if we use false here, to data ek string mein milega jo smjhna muskil ho jaayega


# Create a ConversationChain (LLM + Memory)
conversation = ConversationChain(
    llm=model,
    memory=memory,
    verbose=True   # Debug ke liye (chain steps print karega)
                    ## if verbose=False → sirf AI ka final reply print hota hai.(koi steps nahi dikhte)
)
'''LLM (AI model) ko memory ke saath integrate karta hai.
 input (user messages) + chat history (memory) → AI ko ek pipeline me bhejta hai.
Output me AI ka reply aata hai.
in general == Ye ek “chat engine” hai jo AI model ko + memory ko combine karke ready-to-use chatbot banata hai.
llm = chatbot ka dimag'''

# Run chatbot in terminal
if __name__ == "__main__":
    print(" Chatbot with Memory started! Type 'exit' to quit.\n")
    while True:
        user_msg = input("You: ")
        if user_msg.lower() in ["quit", "exit"]:
            print("Chatbot stopped.")
            break

##  ConversationChain (jo LLM + Memory combine karta hai)
# run(user_msg) = User ke message ko AI model ke paas bhejta hai. AI model chat history (memory) ko check karta hai
## Context-aware reply generate karta hai. Output return karta hai → ye store ho jaata hai variable response me.       
        response = conversation.run(user_msg)
        print(f"AI: {response}\n")
