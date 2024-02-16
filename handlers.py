from telegram import Update
from telegram.ext import ContextTypes
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Access for Gemini Bot
GEMINI_API_TOKEN = os.getenv("GEMINI_API_TOKEN")
genai.configure(api_key=GEMINI_API_TOKEN)
model = genai.GenerativeModel('gemini-pro')


#Handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  """Send a message when the command /start is issued."""
  await update.message.reply_text("Hi I am a bot!")

async def gemini_response(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  """Gemini generates a response on whatever the user says"""
  user_message = update.message.text
  response = model.generate_content(user_message)
  await update.message.reply_text(response.text)


