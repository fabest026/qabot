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

# Navbar
st.set_page_config(
    page_title="Q&A Bot",
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
    response = get_gemini_response(prompt)
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
    "✨ AI Q&A Assistant"
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
<h3 style="text-align: center; color: black;">Unlock Answers in a Snap with Assistant!💡<br />Generate response for blogs, social media, content marketing, and more!</h3>
''', unsafe_allow_html=True)  

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

# Adding the HTML footer
# Profile footer HTML for sidebar


# Render profile footer in sidebar at the "bottom"
# Set a background image
def set_background_image():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://images.pexels.com/photos/4097159/pexels-photo-4097159.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1);
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

set_background_image()

# Set a background image for the sidebar
sidebar_background_image = '''
<style>
[data-testid="stSidebar"] {
    background-image: url("https://www.pexels.com/photo/abstract-background-with-green-smear-of-paint-6423446/");
    background-size: cover;
}
</style>
'''

st.sidebar.markdown(sidebar_background_image, unsafe_allow_html=True)

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


# HTML for the footer - replace your credit information here
footer_html = f"""
<div class="footer">
    <p style="font-size: 12px; font-style: italic; color: gray; margin-bottom: 0px; opacity: 0.7; line-height: 1.2; text-align: center;">
        <span style="display: block; font-weight: 800; letter-spacing: 1.5px; text-transform: uppercase; margin-bottom: 8px; font-family: 'Open Sans', sans-serif;">Developed by::</span>
        <span style="font-size: 20px; font-weight: 800; text-transform: uppercase; font-family: 'Open Sans', sans-serif;">Farhan Akbar</span>
    </p>
    <a href="https://www.linkedin.com/in/farhan-akbar-ai/"><img src="https://img.shields.io/badge/LinkedIn-Profile-blue?style=for-the-badge&logo=linkedin" alt="LinkedIn"/></a>
    <a href="https://api.whatsapp.com/send?phone=923114202358"><img src="https://img.shields.io/badge/WhatsApp-Chat%20Me-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp"/></a>
    <a href="mailto:rasolehri@gmail.com"><img src="https://img.shields.io/badge/Email-Contact%20Me-red?style=for-the-badge&logo=email" alt="Email"/></a>
</div>
"""

# Combine CSS and HTML for the footer
st.markdown(footer_css, unsafe_allow_html=True)
st.markdown(footer_html, unsafe_allow_html=True)



