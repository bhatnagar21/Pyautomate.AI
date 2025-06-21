import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
import joblib
import string
import os

# 📁 Step 1: Train and Save only once
model_path = "automation/spam_model.pkl"
vectorizer_path = "automation/vectorizer.pkl"

if not os.path.exists(model_path) or not os.path.exists(vectorizer_path):
    print("📦 Training model...")

    data = {
        'text': [
            "Win ₹1000 cashback now!!!",
            "Your OTP is 456789",
            "Apply now for free laptop",
            "Meeting at 10 AM tomorrow",
            "Congrats! You've won a prize",
            "Can we reschedule?"
        ],
        'label': [1, 0, 1, 0, 1, 0]  # 1 = spam, 0 = not spam
    }

    df = pd.DataFrame(data)
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(df['text'])
    y = df['label']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = MultinomialNB()
    model.fit(X_train, y_train)

    # Evaluation
    y_pred = model.predict(X_test)
    print("\n📊 Evaluation Report:\n", classification_report(y_test, y_pred))

    # Save the model & vectorizer
    joblib.dump(model, model_path)
    joblib.dump(vectorizer, vectorizer_path)

else:
    print("✅ Model already exists. Skipping training.")

# ✅ Step 2: Dashboard function
def classify_text(user_text):
    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)

    cleaned = user_text.lower().translate(str.maketrans('', '', string.punctuation))
    vector = vectorizer.transform([cleaned])
    result = model.predict(vector)
    
    return "Spam 🚫" if result[0] == 1 else "Not Spam ✅"

# 🧪 Optional local test
if __name__ == "__main__":
    test = "Claim your ₹5000 gift card now!"
    print("🧠 Prediction:", classify_text(test))
