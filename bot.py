/* Global Styles */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Inter', sans-serif;
}

/* Hide Streamlit Components */
#MainMenu, header, footer {
    display: none !important;
}

/* Chat Header */
.chat-header {
    background: linear-gradient(135deg, #6366F1 0%, #4F46E5 100%);
    padding: 1.5rem;
    border-radius: 16px;
    margin-bottom: 2rem;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
}

.header-content {
    text-align: center;
    color: white;
}

.header-content h1 {
    font-size: 2.5rem;
    font-weight: 600;
    margin-bottom: 0.5rem;
}

.subtitle {
    font-size: 1rem;
    opacity: 0.9;
}

/* Chat Messages */
.chat-message {
    display: flex;
    flex-direction: column;
    margin-bottom: 1.5rem;
    max-width: 80%;
    animation: fadeIn 0.3s ease-in;
}

.user-message {
    margin-left: auto;
    align-items: flex-end;
}

.bot-message {
    margin-right: auto;
    align-items: flex-start;
}

.message-content {
    padding: 1rem 1.5rem;
    border-radius: 16px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.user-message .message-content {
    background: #4F46E5;
    color: white;
    border-bottom-right-radius: 4px;
}

.bot-message .message-content {
    background: #F3F4F6;
    color: #1F2937;
    border-bottom-left-radius: 4px;
}

.message-timestamp {
    font-size: 0.75rem;
    color: #6B7280;
    margin-top: 0.25rem;
}

/* Input Area */
.input-area {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    background: white;
    padding: 1rem 2rem;
    box-shadow: 0 -4px 6px -1px rgba(0, 0, 0, 0.1);
}

.stTextInput {
    background: #F3F4F6;
    border-radius: 12px;
    border: 2px solid #E5E7EB;
    padding: 0.75rem 1rem;
    transition: all 0.3s ease;
}

.stTextInput:focus {
    border-color: #4F46E5;
    box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.1);
}

/* Button Styles */
.stButton button {
    background: #4F46E5 !important;
    color: white !important;
    border-radius: 12px !important;
    padding: 0.75rem 1.5rem !important;
    border: none !important;
    transition: all 0.3s ease !important;
}

.stButton button:hover {
    background: #4338CA !important;
    transform: translateY(-1px);
}

/* Animations */
@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(10px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* Footer */
.footer {
    position: fixed;
    bottom: 80px;
    left: 0;
    right: 0;
    text-align: center;
    padding: 1rem;
    color: #6B7280;
    font-size: 0.875rem;
}

/* Responsive Design */
@media (max-width: 768px) {
    .chat-message {
        max-width: 90%;
    }
    
    .header-content h1 {
        font-size: 2rem;
    }
    
    .input-area {
        padding: 1rem;
    }
}
