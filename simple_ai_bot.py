##  init_chat_model =  langchain se ek helpful function initialize kiya jo correct  LLM ko load karega 
## environmental varialble ko load kiya gemini api ke liye
## operating system ko import kiya
## model choodse kiya aur provider ka naam diya 
## simple chatbot function define kiya jo user se input leke response deta hai
## stop nahi karenge to model infinite loop pe chalta rahega so while loop jb user quit,stop dega tab chatbot stop ho jaayega
## function ko call kiya wo user se input leke ai ke reply ko print karrha hai
 #### this model is unable to remember memory .we will ask to it clear cut questions

from langchain.chat_models import init_chat_model

from dotenv import load_dotenv
import os           ## env ko,file path ko handle karne ke liye os

load_dotenv()  # Yeh .env file load karega from system ke environment se so  os use here


# Initialize Gemini model
model = init_chat_model(model="gemini-2.0-flash", model_provider="google_genai")

# Simple chatbot function
def simple_chatbot(user_input):
    response = model.invoke(user_input)    ## LangChain mein invoke() ek simple method hai jo model (ya chain, ya tool) ko call karta hai ek single input ke liye.
    return response.content                      ### response return krdiya

if __name__ == "__main__":           ## [Python mein har file ka ek special variable hota hai __name__. 
                                     ##   # ye code sirf tab chalega jab file ko direct run karoge
                                    ## agar hmm isko dusri file mein import karenge to ye bilkul nahi chalega]
    print(" Chatbot started! Type 'exit' to quit.\n")
    while True:                    ## jab tak nahi rokenge ye infinitely loop mein chalta rahega
        user_msg = input("You: ")    ## you == means user koi bhi input dega isko
        if user_msg.lower() in ["quit", "exit"]:     ##   input ko lowercase mein convert kardo (agar exit or quit likha to model stop ho jaayega)
            print("Chatbot stopped.")
            break                       ## loop break ho jaayega 

        ai_reply = simple_chatbot(user_msg)          ## Jab user input deta hai (user_msg), ye line us input ko AI model ke paas bhejti hai.
                                                     ## simple_chatbot() function Gemini model ko call karega → uska answer milega → answer ai_reply variable mein store ho jaayega.
        print(f"AI: {ai_reply}\n")
