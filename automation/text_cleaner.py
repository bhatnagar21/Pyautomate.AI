import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    words = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    cleaned_words = [word for word in words if word not in stop_words]
    return ' '.join(cleaned_words)

# 📄 Example input
raw_text = "Hello! My name is Bot I’m working on PyAutomate.AI."

cleaned = clean_text(raw_text)

# ✅ Save to file
with open("automation/cleaned_output.txt", "w", encoding="utf-8") as file:
    file.write(cleaned)

print("💾 Cleaned text saved successfully to cleaned_output.txt!")
