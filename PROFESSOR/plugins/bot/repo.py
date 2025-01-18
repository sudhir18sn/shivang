from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from PROFESSOR import app
from config import BOT_USERNAME

start_txt = """
❥ ωєℓ¢σмє  ˹ 𝘼𝙣𝙪𝙥𝙖𝙢𝙖 ™ 𝗦𝘂𝗽𝗽𝗼𝗿𝘁 ˼

❥ ʀᴇᴘᴏ ᴄʜᴀᴀʜɪʏʀ ᴛᴏ ʙᴏᴛ ᴋᴏ 

❥ 3 ɢᴄ ᴍᴀɪ ᴀᴅᴅ ᴋᴀʀ ᴋᴇ 

❥ ᴀᴅᴍɪɴ ʙᴀɴᴏ ᴀᴜʀ sᴄʀᴇᴇɴsʜᴏᴛ 
     
❥ ᴏᴡɴᴇʀ ᴋᴏ ᴅᴏ ғɪʀ ʀᴇᴘᴏ ᴍɪʟ sᴀᴋᴛɪ ʜᴀɪ 

"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("♡ α∂∂ иσω ♡", url=f"https://t.me/{app.username}?startgroup=true")
        ],
        [
          InlineKeyboardButton("ѕυρρσɾƚ", url="https://t.me/ANUPAMA_SUPPORT"),
          InlineKeyboardButton("𝘼𝙣𝙪𝙥𝙖𝙢𝙖 𝗨𝗽𝗱𝗮𝘁𝗲 ✨ ", url="https://t.me/TeamAnupama"),
          ],
               [
                InlineKeyboardButton("ᴏᴛʜᴇʀ ʙᴏᴛs", url=f"https://t.me/TeamAnupama"),
],
[
InlineKeyboardButton("ᴄʜᴇᴄᴋ", url=f"https://telegram.me/Shivang_mishra_op"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/ltwmch.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
