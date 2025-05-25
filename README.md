# 🚀 Askora - AI Pair Programmer

![Demo Screenshot](demo.gif) <!-- Add a screenshot or GIF later -->

**Askora** is an AI-powered coding assistant with debugging superpowers, built with Ollama and LangChain. It provides real-time coding assistance, debugging help, and code documentation.

## ✨ Features

- **🧠 Smart Code Assistance**: Get AI-powered suggestions for Python code
- **🐞 Debugging Help**: Strategic print statements and error analysis
- **📝 Code Documentation**: Automatic docstring generation
- **💡 Solution Design**: Architectural guidance for complex problems
- **🌙 Dark Mode**: Developer-friendly interface
- **📥 Code Download**: Save code snippets directly from chat
- **▶️ Code Execution**: Run Python code directly in the app (experimental)

## 🛠️ Technologies Used

- **Ollama** - For running local LLMs
- **LangChain** - AI orchestration framework
- **Streamlit** - Web application framework
- **DeepSeek Models** - Specialized coding LLMs

## 📦 Installation

1. **Prerequisites**:
   - Python 3.9+
   - Ollama installed and running locally ([installation guide](https://ollama.ai/))

2. **Set up the environment**:
   ```bash
   git clone https://github.com/yourusername/askora.git
   cd askora
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
3. **Download the DeepSeek model:**
   ```bash
   ollama pull deepseek-r1:1.5b
