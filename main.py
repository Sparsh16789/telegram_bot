from dotenv import load_dotenv
import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import google.generativeai as genai
import sys

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

genai.configure(api_key=GEMINI_API_KEY)
        
model = genai.GenerativeModel("gemini-2.5-flash")

bot= Bot(token=TELEGRAM_BOT_TOKEN)
dispatcher= Dispatcher()

@dispatcher.message(Command(commands=["start"]))
async def handle_start(message: types.Message):
    await message.answer("👋 Hi!\nI am a chatbot built by sparsh and can answer your queries.")
    
@dispatcher.message(Command(commands=["help"]))
async def handle_help(message: types.Message):
    help_text = """
Hi there, I'm a Telegram bot created by Sparsh! 🤖

Here are the available commands:
/start - Start the conversation.
/help - Show this help menu.

I hope this helps! 😊
"""
    await message.answer(help_text)
    
@dispatcher.message()
async def gemini(message: types.Message):
    response = model.generate_content(message.text)
    await message.reply(response.text)
    
async def main():
    await dispatcher.start_polling(bot)

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())