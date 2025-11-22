import pandas as pd
import string
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# TRAINING DATA
data = [
    ("Win ₹1000 cashback now!!!", 1),
    ("Your OTP is 456789", 0),
    ("Apply now for free laptop", 1),
    ("Meeting at 10 AM tomorrow", 0),
    ("Congrats! You've won a prize", 1),
    ("Can we reschedule?", 0),
    ("You have won a FREE lottery of ₹5,00,000", 1),
    ("Claim your prize now!", 1),
    ("Limited time offer, click the link", 1),
    ("Urgent! Verify your bank account", 1),
]

texts = [t[0] for t in data]
labels = [t[1] for t in data]

# CLEAN TEXT
cleaned_texts = [
    txt.lower().translate(str.maketrans('', '', string.punctuation))
    for txt in texts
]

# TRAIN VECTOR + MODEL
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(cleaned_texts)

model = MultinomialNB()
model.fit(X, labels)

# SAVE
joblib.dump(model, "automation/spam_model.pkl")
joblib.dump(vectorizer, "automation/vectorizer.pkl")

print("TRAINING DONE ✔")
