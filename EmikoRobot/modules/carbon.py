from platform import python_version as y
from telegram import __version__ as o
from pyrogram import __version__ as z
from telethon import __version__ as s
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
from EmikoRobot import pbot
from EmikoRobot.utils.errors import capture_err
from EmikoRobot.utils.functions import make_carbon


@pbot.on_message(filters.command("carbon"))
@capture_err
async def carbon_func(_, message):
    if not message.reply_to_message:
        return await message.reply_text("`Reply to a text message to make carbon.`")
    if not message.reply_to_message.text:
        return await message.reply_text("`Reply to a text message to make carbon.`")
    m = await message.reply_text("`Preparing Carbon`")
    carbon = await make_carbon(message.reply_to_message.text)
    await m.edit("`Uploading`")
    await pbot.send_photo(message.chat.id, carbon)
    await m.delete()
    carbon.close()


MEMEK = "https://telegra.ph/file/4f0e3eaffec2656e1986e.jpg"

@pbot.on_message(filters.command("openbaby"))
async def repo(_, message):
    await message.reply_photo(
        photo=MEMEK,
        caption=f"""✨ **ʜᴇʏ ɪ'ᴍ 🆉ᴇʙʀᴀ 🆁ᴏʙᴏᴛ** 

**Owner repo : [sᴜᴍɪᴛ ʏᴀᴅᴀᴠ](https://t.me/Simple_Mundaa)**
**Python Version :** `{y()}`
**Library Version :** `{o}`
**Telethon Version :** `{s}`
**Pyrogram Version :** `{z}`

**Cʀᴇᴀᴛᴇ ʏᴏᴜʀ ᴏᴡɴ ᴡɪᴛʜ ᴄʟɪᴄᴋ ʙᴜᴛᴛᴏɴ ʙᴇʟʟᴏᴡ.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᴜᴘᴅᴀᴛᴇs", url="https://t.me/Demon_Creators"), 
                    InlineKeyboardButton(
                        "sᴜᴘᴘᴏʀᴛs", url="https://t.me/World_FriendShip_Zone")
                ]
            ]
        )
    )
