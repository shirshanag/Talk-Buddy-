# 🤖 Talk Buddy

An AI-powered conversational chatbot built with **Python, LangChain, and Google Gemini**. The project demonstrates how to integrate a modern LLM with LangChain for prompt management, runnable chains, and interactive conversations.

## 🚀 Features

* 💬 Interactive AI-powered conversations
* 🧠 Google Gemini as the underlying LLM
* 🔗 LangChain for LLM orchestration
* 📝 System and user prompt templates
* ⚡ LangChain Runnable chains
* 🎯 Context-aware responses
* 🧩 Modular and extensible architecture

## 🛠️ Technologies Used

* **Python**
* **LangChain**
* **Google Gemini**
* **Generative AI**
* **Prompt Engineering**

## 📂 Project Structure

```text
├── qna-bot.py
├── requirements.txt
├── .env
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 🔑 API Key Configuration

Create a `.env` file in the project directory:

```env
GOOGLE_API_KEY=your_gemini_api_key
```

Make sure `.env` is included in `.gitignore` so your API key is not uploaded to GitHub.

## ▶️ Run the Chatbot

```bash
python chatbot.py
```

Enter your questions in the terminal and the chatbot will generate responses using the Gemini model through LangChain.

## 🧠 How It Works

```text
User Input
    ↓
Prompt Template
    ↓
LangChain Runnable
    ↓
Google Gemini
    ↓
AI Response
```

The project uses LangChain to structure the interaction between the user, prompt templates, and the Gemini language model.

## 🔮 Future Improvements

* Add conversation memory
* Add chat history
* Support document-based question answering (RAG)
* Add multiple Gemini model options
* Deploy the chatbot as a web application

## 👨‍💻 Author

**Shirsha Nag**

Built as a learning project to explore **LangChain, LLMs, prompt engineering, and Generative AI**.
