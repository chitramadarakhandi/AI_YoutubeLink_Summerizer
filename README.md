# 🎥 YouTube Video Summarizer AI

An AI-powered web application that summarizes YouTube videos using **Transformer-based NLP models**.  
The app extracts video metadata (title & description) and generates concise summaries through a **chatbot-style interface**.


## 🖼️ Project Preview

### 🔐 Login Page
![Login Page](screenshots/login.png)

### 📝 Register Page
![Register Page](screenshots/register.png)

### 🤖 Chatbot-Style Summarizer
![Summarizer UI](screenshots/summarizer.png)

### 🛠️ Tech Stack Section
![Tech Stack](screenshots/techstack.png)

---

## ✨ Features

- 🤖 AI-powered YouTube video summarization  
- 💬 Chatbot-style interactive UI  
- 🔐 Login & Register pages (UI-level authentication)  
- 🎨 Clean and modern interface  
- ⚡ Fast and CPU-safe inference  
- 🌍 Deployable on Hugging Face Spaces  

---

## 🧠 How It Works

1. User provides a **YouTube video URL**
2. The app extracts:
   - Video title
   - Video description
3. Text is chunked to handle long inputs
4. A **Transformer-based model (BART)** generates summaries
5. The final output is displayed in a **chat-style response**

---

## 🛠️ Tech Stack

### 👨‍💻 Languages
- Python

### 🤗 AI / ML
- Hugging Face Transformers
- BART / DistilBART (Abstractive Summarization)

### 🎨 Frontend
- Gradio (Blocks UI)

### 📦 Libraries & Tools
- yt-dlp (YouTube metadata extraction)
- Torch
- Hugging Face Hub

### ☁️ Deployment
- Hugging Face Spaces

---

## 📁 Project Structure
summerizer_youtube/
│
├── app.py
├── requirements.txt
├── README.md
└── screenshots/
├── home.png
├── login.png
├── register.png
├── summarizer.png
└── techstack.png


## ⚙️ Installation & Local Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd summerizer_youtube

2️⃣ Create virtual environment

python -m venv venv
venv\Scripts\activate

3️⃣ Install dependencies

pip install -r requirements.txt

4️⃣ Run the app

python app.py

----Open in browser----
http://127.0.0.1:7860

*************************************



