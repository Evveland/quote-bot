import os, random, logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    ApplicationBuilder, MessageHandler, ContextTypes, filters
)

load_dotenv()
logging.basicConfig(level=logging.INFO)

QUOTES = [
    "Stay hungry, stay foolish.",
    "Do one thing every day that scares you.",
    "Carpe diem – seize the day!",
]

# 1️⃣  Create the Application  ➜  app ❶
app = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()

# 2️⃣  Define handlers ---------------------------------------------

async def quote_handler(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    if update.message.web_app_data and update.message.web_app_data.data == "quote":
        await update.message.reply_text(random.choice(QUOTES))

async def echo_text(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Echo: " + update.message.text)

# 3️⃣  Register handlers on app ❷ ---------------------------------
app.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, quote_handler))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo_text))

# 4️⃣  Run the bot -------------------------------------------------
if __name__ == "__main__":
    app.run_polling()
