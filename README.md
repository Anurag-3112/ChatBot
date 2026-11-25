# 🤖 Mood Chatbot

A personality-driven AI chatbot built with **Python**, **LangChain**, **Google Gemini**, and **Streamlit**. Choose between three distinct AI moods—**Angry**, **Funny**, or **Sad**—and watch the assistant adapt its tone and personality in real time while maintaining conversation context.

---

## About This Project & My AI Journey

This project marks **my very first step into building with AI**. Starting from a simple command-line script and evolving it into a deployed web application, this chatbot taught me the fundamentals of LLM integration, prompt engineering with system messages, conversation memory, and cloud deployment.

This is just the beginning—I am actively learning and building, with **many bigger and more advanced AI projects coming one after the other**!

---

## Features

* **Three Distinct AI Personalities:**
  * 😡 **Angry Mode:** Responds aggressively and impatiently.
  * 😂 **Funny Mode:** Responds with humor, wit, and jokes.
  * 😢 **Sad Mode:** Responds in a gloomy, melancholic tone.
* **Conversation Memory:** Retains chat history across turns within your active session.
* **Instant Mode Switching & Reset:** Switch personalities or clear the conversation anytime from the sidebar.
* **Interactive Web UI:** Clean, chat-style interface powered by Streamlit.

---

## Tech Stack

* **Frontend / UI:** [Streamlit](https://streamlit.io/)
* **LLM Orchestration:** [LangChain](https://www.langchain.com/) (`langchain`, `langchain-google-genai`)
* **Model:** Google Gemini (`gemini-3.5-flash-lite`)
* **Environment Management:** `python-dotenv`

---

## 📂 Project Structure

```text
├── chatBotStreamlit.py   # Main Streamlit web application
├── chatBot.py            # Main application without Streamlit
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
