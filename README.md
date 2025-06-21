FOLDER STRUCTURE 
PyAutomateAI/
│
├── app.py                    # Main Streamlit app
├── modules/                  # All feature-specific scripts
│   ├── ocr.py
│   ├── email_sender.py
│   ├── sentiment_analyzer.py
│   └── ...
├── model/                    # ML models (Spam classifier etc.)
├── assets/                   # Sample images, icons
├── .env                      # Environment variables (email)
├── requirements.txt          # All Python dependencies
└── README.md



# 🚀 PyAutomate.AI – Smart Python Automation Dashboard

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/) 
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0%2B-brightgreen)](https://streamlit.io/)  
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 🧠 Project Overview

**PyAutomate.AI** is a powerful Python-based automation dashboard that combines multiple AI modules and automation tools into one sleek and interactive Streamlit web app.

From image-based OCR to intelligent spam filtering, sentiment analysis, voice command processing, and secure email automation — everything is handled under one roof with real-time functionality.

This project is built to **boost productivity**, **save time**, and **demonstrate professional-grade fullstack Python automation**.

---

## ✨ Features

- 🖼️ **OCR (Image to Text):** Upload scanned documents or images and extract readable text using Tesseract.
- 🛡️ **Spam Detection:** Uses a trained Naive Bayes ML model to instantly identify spam messages.
- 😊 **Sentiment Analysis:** Classifies input text as Positive, Neutral, or Negative using NLP techniques.
- 📬 **Email Automation:** Send custom emails directly via Gmail using SMTP and app passwords.
- 🎤 **Voice Assistant:** Capture voice commands using speech recognition and control the app hands-free.
- 💻 **Web & Desktop Automation:** Selenium and PyAutoGUI for seamless automation beyond the browser.

---

## 🛠️ Tech Stack

- **Backend/Logic:** Python 3.8+  
- **Dashboard UI:** Streamlit  
- **Web Automation:** Selenium  
- **Desktop Automation:** PyAutoGUI  
- **AI/NLP:** Tesseract OCR, TextBlob, Scikit-learn, TF-IDF Vectorizer  
- **Voice Interaction:** Google Speech Recognition API  
- **Email Integration:** SMTP (Gmail with App Password)

---

## ⚙️ Installation & Setup

### 📌 Prerequisites

- Python 3.8 or above  
- Tesseract OCR installed and added to PATH  
- Gmail account with App Password enabled  
- Git & pip installed

---

### 🧩 Steps to Run

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/PyAutomateAI.git
cd PyAutomateAI

# 2. (Optional but Recommended) Create a virtual environment
python -m venv venv
# Activate the environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 3. Install the dependencies
pip install -r requirements.txt

# 4. Create .env file and add your email credentials
# .env
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_APP_PASSWORD=your_gmail_app_password

# 5. Run the Streamlit app
streamlit run app.py
