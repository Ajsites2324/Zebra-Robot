import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from EmikoRobot.events import register
from EmikoRobot import telethn as tbot


PHOTO = "https://te.legra.ph/file/99d03d5f83650aa3f4afe.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**ʜɪ [{event.sender.first_name}](tg://user?id={event.sender.id}), ɪ'ᴍ 🆃🄿🅽 🆁ᴏʙᴏᴛ.** \n\n"
  TEXT += "⚪ **ɪ'ᴍ ᴡᴏʀᴋɪɴɢ ᴘʀᴏᴘᴇʀʟʏ** \n\n"
  TEXT += f"⚪ **ᴍʏ ᴍᴀsᴛᴇʀ : [ᴀᴊᴇᴇᴛ ɢᴏɴᴅ](https://t.me/Papa_bol_sakteho)** \n\n"
  TEXT += f"⚪ **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{telever}` \n\n"
  TEXT += f"⚪ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tlhver}` \n\n"
  TEXT += f"⚪ **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pyrover}` \n\n"
  TEXT += "**ᴛʜᴀɴᴋs ғᴏʀ ᴀᴅᴅɪɴɢ ᴍᴇ ʜᴇʀᴇ ❤️**"
  BUTTON = [[Button.url("ʜᴇʟᴘ", "https://t.me/Zebra_1Robot?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/modern_elements")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
