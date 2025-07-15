import os
import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize Bot and Dispatcher (v3 style)
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher()

# /start and /help command handler
@dp.message(Command(commands=["start", "help"]))
async def handle_start_help(message: types.Message):
    await message.answer("👋 Hi!\nI am a chatbot built by sparsh and can answer your queries.")
    
@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)

# Main function to run the bot
async def main():
    await dp.start_polling(bot)

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())
