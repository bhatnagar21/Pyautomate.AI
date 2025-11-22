import streamlit as st
from automation.ocr_automation import extract_text_from_image
from automation.text_classifier import classify_text
from automation.sentiment_analysis import analyze_sentiment
from automation.email_automation import send_email

st.set_page_config(page_title="PyAutomate.AI Dashboard", layout="centered")
st.title("🤖 PyAutomate.AI – Smart Automation Dashboard")

# Sidebar menu
menu = st.sidebar.selectbox("📂 Select Tool", [
    "OCR – Image to Text",
    "Spam Detector",
    "Sentiment Analyzer",
    "Send Email"
])

# 🖼️ OCR Tool
if menu == "OCR – Image to Text":
    st.header("🖼️ OCR – Extract Text from Image")
    uploaded_file = st.file_uploader("📤 Upload Image", type=["png", "jpg", "jpeg"])
    if uploaded_file:
        with open("uploaded_image.png", "wb") as f:
            f.write(uploaded_file.read())
        result = extract_text_from_image("uploaded_image.png")
        st.text_area("📄 Extracted Text", result, height=200)

# 📧 Spam Detector
elif menu == "Spam Detector":
    st.header("🚫 Spam Detector")
    user_input = st.text_input("✍️ Enter a message to check:")
    if user_input:
        output = classify_text(user_input)
        st.success(f"Result: {output}")



# 😊 Sentiment Analyzer
elif menu == "Sentiment Analyzer":
    st.header("😊 Sentiment Analysis")
    text = st.text_area("✍️ Write something:")
    if st.button("Analyze"):
        polarity, sentiment = analyze_sentiment(text)
        st.write(f"📊 Polarity Score: `{polarity}`")
        st.success(f"🗣️ Sentiment Type: **{sentiment}**")

# 📤 Send Email
elif menu == "Send Email":
    st.header("📤 Email Automation")
    sender = st.text_input("📨 Your Gmail (e.g., abc@gmail.com)")
    app_pass = st.text_input("🔑 App Password", type="password")
    receiver = st.text_input("📬 Recipient Email")
    subject = st.text_input("📝 Subject")
    message = st.text_area("📨 Message")
    if st.button("Send"):
        response = send_email(sender, app_pass, receiver, subject, message)
        st.success(response)



#streamlit run app.py
