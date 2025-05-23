from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="models/gemini-1.5-flash", temperature=0.3,api_key='apikey')
memory = ConversationBufferMemory()
chat = ConversationChain(llm=llm, memory=memory)

def run_chat():
    print("🤖 Gemini 1.5 Flash Chatbot — type 'exit' to quit")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        reply = chat.run(user_input)
        print("Bot:", reply)

run_chat()