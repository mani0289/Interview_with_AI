# 🤖 AI Interview Assistant

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B)
![Gemini](https://img.shields.io/badge/Google-Gemini-blueviolet)


## 👋 What is this?
Preparing for interviews is hard. Guessing what questions they will ask is even harder.

This is a smart tool I built to help with that! It takes your **Resume** and a **Job Description**, reads them both, and uses Google's **Gemini AI** to act as your personal interviewer. It finds the gaps in your experience and generates 5 custom technical questions (plus ideal answers) to help you practice.

## ✨ What can it do?
* **📄 Reads Anything:** Upload your resume in PDF, Word, or plain text. No need to convert files!
* **🧠 Smart Analysis:** It doesn't just ask random questions; it asks about *your* specific experience relative to the job.
* **💾 Study Guides:** Download your generated Q&A session as a text file or CSV to practice offline.


## 🛠️ How I built it
I wanted to move beyond simple scripts and build a real, modular application.
* **Brain:** Google Gemini 3.0 (via LangChain)
* **Body:** Streamlit (for the web interface)
* **Skeleton:** Python (with a modular `src` folder structure)
* **Security:** Production-grade secrets management for API keys.
