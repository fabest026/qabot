from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
from typing import List

# Configure Google API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load Gemini Pro model
model = genai.GenerativeModel("gemini-2.0-flash-thinking-exp-01-21")

def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

# Page Configuration
st.set_page_config(
    page_title="AppJingle AI",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Custom CSS for the entire app
st.markdown("""
    <style>
    /* Main content styling */
    .main {
        padding: 2rem;
        max-width: 1200px;
        margin: 0 auto;
    }
    
    /* Header styling */
    .header-container {
        background: linear-gradient(135deg, #6e8efb, #a777e3);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    /* Chat container styling */
    .chat-container {
        background: white;
        border-radius: 15px;
        padding: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    /* Message styling */
    .message {
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 10px;
    }
    
    .user-message {
        background: #E3F2FD;
        margin-left: 2rem;
    }
    
    .bot-message {
        background: #F5F5F5;
        margin-right: 2rem;
    }
    
    /* Input box styling */
    .stTextInput > div > div > input {
        border-radius: 25px;
        padding: 1rem;
        border: 2px solid #6e8efb;
    }
    
    /* Button styling */
    .stButton > button {
        border-radius: 25px;
        padding: 0.5rem 2rem;
        background: linear-gradient(135deg, #6e8efb, #a777e3);
        color: white;
        border: none;
        transition: transform 0.2s;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
    }
    
    /* Hide Streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Avatar styling */
    .avatar {
        border-radius: 50%;
        border: 2px solid #6e8efb;
    }
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 10px;
    }
    
    ::-webkit-scrollbar-track {
        background: #f1f1f1;
        border-radius: 5px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #888;
        border-radius: 5px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #555;
    }
    </style>
""", unsafe_allow_html=True)

# Load avatars
ava_bot = Image.open("bot-ava.png")
ava_human = Image.open("human-ava.png")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Bot and user response functions
def bot_response(prompt: str) -> None:
    history = " ".join([msg["content"] for msg in st.session_state.messages])
    response = get_gemini_response(history + " " + prompt)
    st.session_state.messages.append({"role": "bot", "content": response})

def user_response(prompt):
    st.session_state.messages.append({"role": "user", "content": prompt})

# App Header
st.markdown("""
    <div class="header-container">
        <h1 style='color: white;'>✨ AppJingle AI ✨</h1>
        <p style='color: white; font-size: 1.2rem;'>
            Developed by: Farhan Akbar 💡<br/>
            AppJingle Solutions: Empowering productivity and smarter decisions through AI!
        </p>
    </div>
""", unsafe_allow_html=True)

# Create two columns for layout
col1, col2 = st.columns([3, 1])

with col1:
    # Chat container
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    
    # Display chat history
    for msg in st.session_state.messages:
        if msg["role"] == "bot":
            with st.container():
                cols = st.columns([0.1, 4])
                with cols[0]:
                    st.image(ava_bot, width=40, output_format="PNG", clamp=True)
                with cols[1]:
                    st.markdown(f"""
                        <div class="message bot-message">
                            <b>AI Assistant:</b><br/>
                            {msg["content"]}
                        </div>
                    """, unsafe_allow_html=True)
        else:
            with st.container():
                cols = st.columns([4, 0.1])
                with cols[1]:
                    st.image(ava_human, width=40, output_format="PNG", clamp=True)
                with cols[0]:
                    st.markdown(f"""
                        <div class="message user-message">
                            <b>You:</b><br/>
                            {msg["content"]}
                        </div>
                    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    # Control panel
    st.markdown("""
        <div style="background: white; padding: 1rem; border-radius: 15px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
            <h3 style="color: #6e8efb;">Controls</h3>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("Clear Chat History", key="clear_chat"):
        st.session_state.messages = []
        st.experimental_rerun()

# Chat input at the bottom
prompt = st.text_input("Send a message", key="chat_input", 
                      help="Type your message here and press Enter to send")

if prompt:
    user_response(prompt)
    with st.spinner("Thinking..."):
        bot_response(prompt)
    st.experimental_rerun()

# Footer
st.markdown("""
    <div style="position: fixed; bottom: 0; right: 0; padding: 1rem; background: transparent;">
        <p style="color: gray; font-size: 0.8rem;">© 2024 AppJingle Solutions</p>
    </div>
""", unsafe_allow_html=True)
