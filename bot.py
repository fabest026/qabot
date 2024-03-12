## loading all the environment variables
from dotenv import load_dotenv
load_dotenv()  

# import statements
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
from typing import List


# configure google API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# load Gemini Pro model
model = genai.GenerativeModel("gemini-pro")

# function to get response from Gemini model
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

# initialize streamlit app
st.set_page_config(page_title="Farhan Q&A Bot")

# load avatars
ava_bot = Image.open("bot-ava.png")
ava_human = Image.open("human-ava.png")

# initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# bot code
def bot_response(prompt: str) -> None:
    response = get_gemini_response(prompt)
    st.session_state.messages.append({"role": "bot", "content": response})
# user code
def user_response(prompt):
    st.session_state.messages.append({"role": "user", "content": prompt})

# clear chat history
def clear_history():
    st.session_state.messages = []

# main app
st.title("Farhan GPT 🤖")
st.subheader("AI Q&A Assistant 🥷")

# chat input
if prompt := st.chat_input("Your question"):
    user_response(prompt)

    # generate bot response if last message is not from bot
    if st.session_state.messages[-1]["role"] != "bot":
        with st.chat_message("bot"):
            with st.spinner("Thinking..."):
                bot_response(prompt)


# clear chat history button
st.button("Clear History", on_click=lambda: st.session_state.messages.clear())

# display chat history
for msg in st.session_state.messages:
    if msg["role"] == "bot":
        st.image(ava_bot, width=40)
        st.markdown(f"**{msg['role']}** {msg['content']}")
    else:
        st.image(ava_human, width=40)
        st.markdown(f"**{msg['role']}** {msg['content']}")
