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
model = genai.GenerativeModel("gemini-2.0-flash-exp")

# function to get response from Gemini model
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

# Navbar
st.set_page_config(
    page_title="AppJingle AI",
    page_icon="🥷",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# load avatars
ava_bot = Image.open("bot-ava.png")
ava_human = Image.open("human-ava.png")

# initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# bot code
def bot_response(prompt: str) -> None:
    history = " ".join([msg["content"] for msg in st.session_state.messages])
    response = get_gemini_response(history + " " + prompt)
    st.session_state.messages.append({"role": "bot", "content": response})
# user code
def user_response(prompt):
    st.session_state.messages.append({"role": "user", "content": prompt})

# clear chat history
def clear_history():
    st.session_state.messages = []


# Add the Title
st.markdown(
    "<h1 style='text-align: center; color: black;'>"
    "✨ AppJingle AI ✨"
    "</h1>",
    unsafe_allow_html=True
)


# create a subheader
st.markdown('''
<style>
h3 {
    font-family: 'Open Sans', sans-serif;
    font-size: 16px;
    line-height: 24px;
    margin-top: 0;
    margin-bottom: 24px;
}
</style>
<h3 style="text-align: center; color: black;">Developed by: Farhan Akbar!!💡<br />AppJingle Solutions: Empowering productivity and smarter decisions through AI!</h3>
''', unsafe_allow_html=True)  

# chat input
st.markdown(
    """
    <style>
    .element-container .stChatInput,
    .element-container .stChatButton {
        background-color: #f0f8ff !important;
        border-color: #000000 !important;
        color: white !important;
    }
    .element-container .stChatInput {
        caret-color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)




# chat input
if prompt := st.chat_input("Your question"):
    user_response(prompt)

    # generate bot response if last message is not from bot
    if st.session_state.messages[-1]["role"] != "bot":
            with st.spinner("Thinking..."):
                bot_response(prompt)


# clear chat history button
st.markdown(
    """
    <style>
    .element-container .stButton.stBtn { 
        background-color: #ffc107 !important;
        border-color: #ffc107 !important;
    }
    .stButton.stBtn:nth-last-child(2) {display: none;}
    </style>
    """,
    unsafe_allow_html=True,
)
st.button("Clear History", on_click=lambda: st.session_state.messages.clear())

# display chat history
for msg in st.session_state.messages:
    if msg["role"] == "bot":
        st.image(ava_bot, width=40)
        st.markdown("**Bot:**", unsafe_allow_html=True)
        st.write(" ")
        st.markdown(msg["content"], unsafe_allow_html=True)
    else:
        st.image(ava_human, width=40)
        st.markdown("**User:**", unsafe_allow_html=True)
        st.write(" ")
        st.markdown(msg["content"], unsafe_allow_html=True)
        

# Render profile footer in sidebar at the "bottom"
# Set a background image

# Set a background image for the sidebar

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Custom CSS to inject into the Streamlit app
footer_css = """
<style>
.footer {
    position: fixed;
    right: 0;
    bottom: 0;
    width: auto;
    background-color: transparent;
    color: black;
    text-align: right;
    padding-right: 10px;
}
</style>
"""
       

