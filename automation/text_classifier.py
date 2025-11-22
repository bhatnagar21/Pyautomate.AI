import pandas as pd
import string
import os
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

model_path = "automation/spam_model.pkl"
vectorizer_path = "automation/vectorizer.pkl"


# -----------------------------
# TRAIN MODEL (only 1st time)
# -----------------------------
def train_model():
    data = {
        'text': [
            "Win ₹1000 cashback now!!!",
            "Your OTP is 456789",
            "Apply now for free laptop",
            "Meeting at 10 AM tomorrow",
            "Congrats! You've won a prize",
            "Can we reschedule?",
            "You have won a FREE lottery of ₹5,00,000",
            "Claim your prize now!",
            "Limited time offer, click the link",
            "Urgent! Verify your bank account"
        ],
        'label': [1, 0, 1, 0, 1, 0, 1, 1, 1, 1]
    }

    df = pd.DataFrame(data)

    # Clean text
    df["clean"] = df["text"].apply(lambda x:
        x.lower().translate(str.maketrans('', '', string.punctuation))
    )

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(df["clean"])
    y = df["label"]

    model = MultinomialNB()
    model.fit(X, y)

    joblib.dump(model, model_path)
    joblib.dump(vectorizer, vectorizer_path)

    print("Model trained and saved!")


# -----------------------------
# CLASSIFY TEXT
# -----------------------------
def classify_text(user_text):

    # Train model if missing
    if not os.path.exists(model_path) or not os.path.exists(vectorizer_path):
        train_model()

    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)

    cleaned = user_text.lower().translate(str.maketrans('', '', string.punctuation))
    vector = vectorizer.transform([cleaned])
    prediction = model.predict(vector)[0]

    return "Spam 🚫" if prediction == 1 else "Not Spam ✅"
