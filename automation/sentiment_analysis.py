from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity # type: ignore
    sentiment = "Positive" if polarity > 0 else "Negative" if polarity < 0 else "Neutral"
    return polarity, sentiment
