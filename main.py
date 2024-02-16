from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import os
from handlers import start, gemini_response
from dotenv import load_dotenv
import logging

# Load environment variables from .env file
load_dotenv()

# Access for telegram Bot
bot = os.getenv("TELEGRAM_BOT_TOKEN")

#Starts the BOT
def main() -> None:
  # Setup logging
  logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
  )

  #Create the Application and pass it your bot's token.
  application = Application.builder().token(bot).build()

  #How to handle each command
  application.add_handler(CommandHandler("start", start))

  application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, gemini_response))

  # Run the bot until the user presses Ctrl-C
  application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
  main()