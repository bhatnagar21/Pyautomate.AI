from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# ✅ Paste your actual token here
BOT_TOKEN = "8199234093:AAGq_CZBEuVuDHT4YPnbz5oo-7oXt6GYaf8"

# When user sends "/start"
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hello! I'm your PyAutomate.AI Telegram bot!made By Shreya") # type: ignore

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("✅ Telegram bot is running. Go to Telegram and type /start")
app.run_polling()
