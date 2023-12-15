from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup
)
from telegram.ext import (
    ApplicationBuilder, 
    CommandHandler, 
    ContextTypes, 
    MessageHandler, 
    filters
)
import logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


KEY = '6473376751:AAE9QINuPLnEdOgTlzDeX2fSZ67o_2GEcNo'


async def start(update:Update, context:ContextTypes) -> None:
 return await update.message.reply_text('Hello World! ')

async def help(update:Update, context:ContextTypes) -> None:
 return await update.message.reply_text("""
/help - Show This message
/start - Start the bot 
""")


# Response
async def handle_responses(update:Update, context:ContextTypes) -> str:
    text: str = update.message.text.lower()     

    response = ""

    if 'hello' in text:
        response = 'Hello there! How can i help you? \n'

    if 'how are you' in text:
        response = response + "I`m fine, thank you, And you? \n"
    
    return await update.message.reply_text(response)


if name == "main":
    app = ApplicationBuilder().token(KEY).build()
    print("Bot is running...")

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help))
    
    app.add_handler(MessageHandler(filters.TEXT, handle_responses))

    # Run the bot
    print("Polling")
    app.run_polling(poll_interval=1)