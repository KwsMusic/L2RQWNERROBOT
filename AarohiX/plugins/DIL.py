from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from AarohiX import app
import string
from strings import get_command

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

DIL = [" **◈ ━━━━━━━ ⸙ ♡ ⸙ ━━━━━━━ ◈** \n\n🍃**ʀᴇʟᴀᴛɪᴏɴsʜɪᴘ ᴅᴏsᴇɴ'ᴛ ɴᴇᴇᴅ ᴄᴜᴛᴇ ᴠᴏɪᴄᴇ ᴀɴᴅ ʟᴏᴠᴇʟʏ ғᴀᴄᴇ...**🍃 \n\n**🥺ʀᴇʟᴀᴛɪᴏɴsʜɪᴘ ɴᴇᴇᴅs ᴘᴜʀᴇ ʜᴇᴀʀᴛ ᴡɪᴛʜ ᴜɴʙʀᴇᴀᴋᴀʙʟᴇ ᴛʀᴜsᴛ🥺** \n\n**◈ ━━━━━━━ ⸙ ♡ ⸙ ━━━━━━━ ◈** ",
       " **◈ ━━━━━━━ ⸙ ♡ ⸙ ━━━━━━━ ◈** \n\n🍃**🌹❝◂ 𝐈 𝐏ʀᴏᴍɪsᴇ ▸**🍃 \n\n**◂𝐘ᴏᴜ 𝐇ᴀᴠᴇ 𝐌ᴇ,𝐔ɴᴛɪʟ 𝐌ʏ 𝐋ᴀsᴛ 𝐁ʀᴇᴀᴛʜ▸❞🌹** \n\n**◈ ━━━━━━━ ⸙ ♡ ⸙ ━━━━━━━ ◈** ",
       " **◈ ━━━━━━━ ⸙ ♡ ⸙ ━━━━━━━ ◈** \n\n 🍃**Koyi Aaye Na Jaye Na, Aao Na Aisi Jagah Pe Le Chalun**🍃 \n\n**✨❤️ Jahaan Waqt Humara Ruka Ho,Aur Main Apne Dil Ki Kahun ♥️✨** \n\n**◈ ━━━━━━━ ⸙ ♡ ⸙ ━━━━━━━ ◈** "]

# Command of DILxAAROHI
DIL_COMMAND = get_command("Ashish_COMMAND")

@app.on_message(
    filters.command(DIL_COMMAND)
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        text = random.choice(DIL),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🍒̵̶⃰͟˶֟፝͟͝sᴜᴩᴩᴏʀᴛ⏎͟🝛꯭", url=f"https://t.me/BWF_MUSIC1"),
                    InlineKeyboardButton(
                        "💝ᴍᴀɪɴᴛᴀɪɴᴇʀ[ᴀsʜɪsʜ]💝", url=f"https://t.me/II_ASHISH_GUPTA_IIl")
                    
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(DIL_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        text = random.choice(DIL),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🍒̵̶⃰͟˶֟፝͟͝sᴜᴩᴩᴏʀᴛ⏎͟🝛꯭", url=f"https://t.me/BWF_MUSIC1"),
                    InlineKeyboardButton(
                        "💝ᴍᴀɪɴᴛᴀɪɴᴇʀ[ᴀsʜɪsʜ]💝", url=f"https://t.me/II_ASHISH_GUPTA_IIl")
                    
                ]
            ]
        ),
    )
