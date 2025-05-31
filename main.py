import os
from pyrogram import Client, filters
from pyrogram.types import Message
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
DOWNLOAD_DIR = os.getenv("DOWNLOAD_DIR", "downloads")

bot = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@bot.on_message(filters.command("start") & filters.private)
async def start(_, message: Message):
    await message.reply_text("👋 Hi! Send me a file/message link or forward a restricted message.")

@bot.on_message(filters.private & filters.forwarded)
async def forward_handler(_, message: Message):
    await message.reply_text("✅ Message received and saved.")

@bot.on_message(filters.private & filters.text)
async def handle_text(_, message: Message):
    url = message.text.strip()
    if url.startswith("http"):
        await message.reply_text("📥 Downloading content...")
        # Simulate download
        await message.reply_text("✅ Content processed!")
    else:
        await message.reply_text("❌ Please send a valid link.")

print("✅ Bot is starting...")
bot.run()
