from typing import Union

from pyrogram.types import InlineKeyboardButton

import config
from AarohiX import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🦋ᴀᴅᴅ ᴍᴇ ɪɴ ɢʀᴘ ʙᴀʙᴜ🧸",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="❤️⃡˓⃝˓⃝˓⃝˓⃝˓⃝   ʜᴇʟᴩ   ˓⃝˓⃝˓⃝˓⃝˓⃝❤️",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="❤‍🔥sᴇᴛᴛɪɴɢs❤‍🔥", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="💖 ғᴇᴇʟɪɴɢs 💖", url=f"https://t.me/Zidd_Bot"),
            InlineKeyboardButton(
                text="🥰 ᴍʏ ʟɪғᴇʟɪɴᴇ[❣️] 🥰", url=f"https://t.me/MUSICBOT_OWNER"
            ),
        ],
        [
            InlineKeyboardButton(
                text="👑ᴏᴡɴᴇʀ👑", user_id=OWNER),
            InlineKeyboardButton(
                text="🍒̵̶⃰͟˶֟፝͟͝sᴜᴩᴩᴏʀᴛ⏎͟🝛꯭", url=config.SUPPORT_GROUP
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🦋ᴀᴅᴅ ᴍᴇ ɪɴ ɢʀᴘ ʙᴀʙᴜ🧸",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="❤️⃡˓⃝˓⃝˓⃝˓⃝˓⃝   ʜᴇʟᴩ   ˓⃝˓⃝˓⃝˓⃝˓⃝❤️", callback_data="settings_back_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="💖 ғᴇᴇʟɪɴɢs 💖", url=f"https://t.me/Zidd_Bot"),
            InlineKeyboardButton(
                text="🥰 ᴍʏ ʟɪғᴇʟɪɴᴇ[❣️] 🥰", url=f"https://t.me/MUSICBOT_OWNER"
            ),
        ],
        [
            InlineKeyboardButton(text="👑ᴏᴡɴᴇʀ👑", user_id=OWNER),
            InlineKeyboardButton(
                text="🍒̵̶⃰͟˶֟፝͟͝sᴜᴩᴩᴏʀᴛ⏎͟🝛꯭", url=config.SUPPORT_GROUP
            ),
        ],
        [
            InlineKeyboardButton(
                    text="👑ᴏᴡɴᴇʀ👑", url=f"https://t.me/L2R_KING0"
                )
        ],
     ]
    return buttons
