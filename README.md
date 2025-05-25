# 🚀 Askora - AI Pair Programmer

![Demo Screenshot](![Screenshot 2025-05-25 130020](https://github.com/user-attachments/assets/ccc18c6b-cd55-499a-a226-22028b82ad35)
)

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
Download the DeepSeek model:

bash
ollama pull deepseek-r1:1.5b
🚀 Usage
Start the application:

bash
streamlit run app.py
Configure the model:

Select your preferred model from the sidebar

Toggle dark mode if desired

Start chatting:

Type your coding questions in the chat input

Download code snippets with the download button

Execute code directly in the app (experimental)

⚙️ Configuration
Customize the app by modifying these environment variables:

bash
# In a .env file
OLLAMA_BASE_URL=http://localhost:11434  # Change if using remote Ollama
DEFAULT_MODEL=deepseek-r1:1.5b         # Default model to use
🌟 Available Models
The app supports these Ollama models:

deepseek-r1:1.5b (default)

deepseek-r1:3b

To add more models:

Pull them with Ollama: ollama pull <model-name>

Add them to the model selection dropdown in app.py

⚠️ Limitations
Code execution is experimental and runs in a limited sandbox

Complex queries may take longer to process

Model accuracy depends on the selected LLM

🤝 Contributing
Contributions are welcome! Please follow these steps:

Fork the repository

Create a new branch (git checkout -b feature/your-feature)

Commit your changes (git commit -am 'Add some feature')

Push to the branch (git push origin feature/your-feature)

Open a Pull Request

📜 License
This project is licensed under the MIT License - see the LICENSE file for details.

🙏 Acknowledgments
Ollama team for the amazing local LLM runner

LangChain for the AI orchestration framework

DeepSeek for their specialized coding models
