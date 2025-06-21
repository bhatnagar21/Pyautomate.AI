from transformers import pipeline # type: ignore

# 🧠 Load pre-trained model
generator = pipeline("text-generation", model="gpt2")

# 📝 User input
user_input = input("💬 Enter your message: ")

# 🤖 Generate smart response
response = generator(user_input, max_length=50, num_return_sequences=1)

# 📊 Output
print("\n🧠 AI Response:")
print(response[0]['generated_text']) # type: ignore
