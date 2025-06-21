import pywhatkit as kit
import datetime

# 👤 Receiver's WhatsApp number (with country code)
phone_number = "+919997241658"

# 📝 Your message
message = "Hello from PyAutomate.AI 🤖🚀 - This message is sent automatically!"

# ⏰ Send after 1 minute from now
now = datetime.datetime.now()
hour = now.hour
minute = now.minute + 1  # sends message after 1 minute

# 📤 Send the message
kit.sendwhatmsg(phone_number, message, hour, minute) # type: ignore

print("✅ WhatsApp message scheduled successfully!")
