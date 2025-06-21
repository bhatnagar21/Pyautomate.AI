import speech_recognition as sr
import pyttsx3
import webbrowser

# 🔊 Voice engine setup
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech
engine.say("Voice Assistant Activated")
engine.runAndWait()

# 🎤 Speech recognizer
recognizer = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as source:
            print("🎙️ Speak now...")
            audio = recognizer.listen(source)
            query = recognizer.recognize_google(audio)

            print(f"🔈 You said: {query}")

            # 🔁 Command Handling
            if "hello" in query.lower():
                response = "Hello didi ji! How can I help you?"
            elif "open google" in query.lower():
                webbrowser.open("https://www.google.com")
                response = "Opening Google"
            elif "your name" in query.lower():
                response = "I am your PyAutomate voice assistant!"
            elif "stop" in query.lower():
                response = "Goodbye didi ji!"
                engine.say(response)
                engine.runAndWait()
                break
            else:
                response = "Sorry, I didn't understand that."

            engine.say(response)
            engine.runAndWait()

    except Exception as e:
        print("⚠️ Error:", e)
