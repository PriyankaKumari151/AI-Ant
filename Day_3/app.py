import os
from dotenv import load_dotenv
from openai import OpenAI
import streamlit as st

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    try:
        api_key = st.secrets["GROQ_API_KEY"]
    except:
        api_key = None
        
st.set_page_config(page_title="Groq AI Chatbot",page_icon="🦕")
st.title("🦕 Groq AI Assistant with Memory")

#1. Initialise OpenAI Client
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=api_key,
)

#2. Use Streamlit Session State for Conversational Memory
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant. Keep answers concise.",
        }
    ]

#3. Render previous messages in the chat UI
for message in st.session_state.messages:
    if message["role"]!="system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

#4. Handle user input
if prompt := st.chat_input("Ask a question..."):
    #Display user input in UI
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    #Call LLM API with full conversational history
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="openai/gpt-oss-120b",
                temperature=0.0,
                messages=st.session_state.messages,
            )
            reply = response.choices[0].message.content
            st.markdown(reply)

    
    #Save assistant response back to memory
    st.session_state.messages.append({"role":"assistant", "content": reply})