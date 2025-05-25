import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    AIMessagePromptTemplate,
    ChatPromptTemplate,
)
import re
import base64
import os

# Load the custom CSS
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# App title and description
st.title("🚀 Askora")
st.caption("✨ Your AI Pair Programmer with Debugging Superpowers")

# Dark Mode Toggle
dark_mode = st.sidebar.checkbox("🌙 Dark Mode", value=False)
if dark_mode:
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #1e1e1e;
            color: #ffffff;
        }
        .stChatMessage {
            background-color: #2d2d2d;
            color: #ffffff;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Sidebar configuration
with st.sidebar:
    st.markdown("### ⚙️ Configuration")
    selected_model = st.selectbox(
        "Choose Model",
        ["deepseek-r1:1.5b", "deepseek-r1:3b"],
        index=0
    )
    st.divider()
    st.markdown("### 🛠️ Model Capabilities")
    st.markdown("""
    - 🐍 **Python Expert**
    - 🐞 **Debugging Assistant**
    - 📝 **Code Documentation**
    - 💡 **Solution Design**
    """)
    st.divider()
    st.markdown("### 📂 Quick Actions")
    if st.button("🧹 Clear Chat", use_container_width=True):
        st.session_state.message_log = [{"role": "ai", "content": "👋 Hi! I'm DeepSeek. How can I help you code today? 💻"}]
        st.rerun()
    if st.button("🔄 Regenerate Last Response", use_container_width=True):
        if len(st.session_state.message_log) > 1 and st.session_state.message_log[-1]["role"] == "ai":
            st.session_state.message_log.pop()  # Remove the last AI response
            st.rerun()
    st.divider()
    st.markdown("Built with [Ollama](https://ollama.ai/) | [LangChain](https://python.langchain.com/)")

# Initialize the chat engine
llm_engine = ChatOllama(
    model=selected_model,
    base_url="http://localhost:11434",
    temperature=0.3
)

# System prompt configuration
system_prompt = SystemMessagePromptTemplate.from_template(
    "You are an expert AI coding assistant. Provide concise, correct solutions "
    "with strategic print statements for debugging. Always respond in English."
)

# Session state management
if "message_log" not in st.session_state:
    st.session_state.message_log = [{"role": "ai", "content": "👋 Hi! I'm DeepSeek. How can I help you code today? 💻"}]

# Chat container
chat_container = st.container()

# Function to extract code blocks from messages
def extract_code_blocks(text):
    code_blocks = re.findall(r"```(.*?)```", text, re.DOTALL)
    return code_blocks

# Function to create a downloadable file
def create_downloadable_file(code, filename="code.py"):
    b64 = base64.b64encode(code.encode()).decode()
    href = f'<a href="data:file/txt;base64,{b64}" download="{filename}">📥 Download {filename}</a>'
    return href

# Display chat messages
with chat_container:
    for message in st.session_state.message_log:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            # Syntax highlighting for code blocks
            code_blocks = extract_code_blocks(message["content"])
            if code_blocks:
                for code in code_blocks:
                    st.code(code, language="python")
                    # Add a download button for code snippets
                    st.markdown(create_downloadable_file(code), unsafe_allow_html=True)
                    # Add a button to execute code
                    if st.button("▶️ Run Code", key=f"run_{code[:10]}"):
                        try:
                            exec(code)
                            st.success("Code executed successfully!")
                        except Exception as e:
                            st.error(f"Error executing code: {str(e)}")

# Chat input and processing
user_query = st.chat_input("Type your coding question here...", max_chars=500)

def generate_ai_response(prompt_chain):
    try:
        processing_pipeline = prompt_chain | llm_engine | StrOutputParser()
        return processing_pipeline.invoke({})
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        return "❌ Sorry, I couldn't process your request. Please try again."

def build_prompt_chain():
    prompt_sequence = [system_prompt]
    for msg in st.session_state.message_log:
        if msg["role"] == "user":
            prompt_sequence.append(HumanMessagePromptTemplate.from_template(msg["content"]))
        elif msg["role"] == "ai":
            prompt_sequence.append(AIMessagePromptTemplate.from_template(msg["content"]))
    return ChatPromptTemplate.from_messages(prompt_sequence)

if user_query:
    # Add user message to log
    st.session_state.message_log.append({"role": "user", "content": user_query})
    
    # Generate AI response
    with st.spinner("🤖 Processing your request..."):
        prompt_chain = build_prompt_chain()
        ai_response = generate_ai_response(prompt_chain)
    
    # Add AI response to log
    st.session_state.message_log.append({"role": "ai", "content": ai_response})
    
    # Rerun to update chat display
    st.rerun()