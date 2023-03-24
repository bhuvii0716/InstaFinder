from pyrogram import Client, filters, idle
from pyrogram.errors import UserNotParticipant
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import enums
import instaloader
import os
import time
from os import listdir
import shutil
import uvicorn

model_engine = "text-davinci-003"

app = instaloader.Instaloader()

bot = Client("InstaFinder", api_id=3769190, api_hash="e125d5abf9dadd0f9b861f774f5aae6a", bot_token="5863087473:AAHvdFs954RE-AjexU5jIPnRCXN0-7mvzUM")

START_BUTTON = JOIN_BUTTON = InlineKeyboardMarkup([[InlineKeyboardButton("Channel", url="https://t.me/DumperBots")], [InlineKeyboardButton("Help", callback_data="help")], [InlineKeyboardButton("Source code", callback_data="source")], [InlineKeyboardButton("Back", callback_data="back")]])
JOIN_BUTTON = InlineKeyboardMarkup([[InlineKeyboardButton("Channel", url="https://t.me/DumperBots")], [InlineKeyboardButton("Joined", callback_data="chatgpt")]])

@bot.on_message(filters.command("start") & filters.all)
async def start_i(bot, msg):
    reply_markup = START_BUTTON
    await msg.reply_text(text="<b>𝖧𝖾𝗅𝗅𝗈 𝖶𝖾𝗅𝖼𝗈𝗆𝖾 𝗍𝗈 𝖨𝗇𝗌𝗍𝖺𝖥𝗂𝗇𝖽𝖾𝗋. 𝖳𝗁𝗂𝗌 𝖻𝗈𝗍 𝗉𝗋𝗈𝗏𝗂𝖽𝖾 𝖨𝗇𝖿𝗈𝗋𝗆𝖺𝗍𝗂𝗈𝗇 𝗈𝖿 𝖨𝗇𝗌𝗍𝖺𝗀𝗋𝖺𝗆 𝖴𝗌𝖾𝗋 𝖻𝗒 𝖴𝗌𝖾𝗋𝗇𝖺𝗆𝖾.\n\n𝖠 𝖯𝗋𝗈𝖽𝗎𝖼𝗍 𝗈𝖿 @TheDumperNetwork</b>", reply_markup=reply_markup)
    await msg.reply_text("<b>Send Instagram Account</b>")

@bot.on_callback_query()
def callback_query(bot, CallBackQuery):
    reply_markup = START_BUTTON
    if CallBackQuery.data == "help":
        text = """
        <b>𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖠𝗏𝖺𝗂𝗅𝖺𝖻𝗅𝖾 :\n/find <usernmae> - To Get Detailes of User\n\n𝖤𝗑𝖺𝗆𝗉𝗅𝖾 :\n/find eminem</b>
        """
        CallBackQuery.edit_message_text(text, reply_markup=reply_markup)
    elif CallBackQuery.data == "source":
        text = "<b>𝖨𝖿 𝗒𝗈𝗎 𝗐𝖺𝗇𝗍 𝗍𝗁𝗂𝗌 𝖻𝗈𝗍'𝗌 𝗌𝗈𝗎𝗋𝖼𝖾 𝖼𝗈𝖽𝖾\n\n𝖢𝗈𝗇𝗍𝖺𝖼𝗍 : @Walker_web</b>"
        CallBackQuery.edit_message_text(text, reply_markup=reply_markup)
    elif CallBackQuery.data == "back":
        text = "<b>𝖧𝖾𝗅𝗅𝗈 𝖶𝖾𝗅𝖼𝗈𝗆𝖾 𝗍𝗈 𝖨𝗇𝗌𝗍𝖺𝖥𝗂𝗇𝖽𝖾𝗋. 𝖳𝗁𝗂𝗌 𝖻𝗈𝗍 𝗉𝗋𝗈𝗏𝗂𝖽𝖾 𝖨𝗇𝖿𝗈𝗋𝗆𝖺𝗍𝗂𝗈𝗇 𝗈𝖿 𝖨𝗇𝗌𝗍𝖺𝗀𝗋𝖺𝗆 𝖴𝗌𝖾𝗋 𝖻𝗒 𝖴𝗌𝖾𝗋𝗇𝖺𝗆𝖾.\n\n𝖠 𝖯𝗋𝗈𝖽𝗎𝖼𝗍 𝗈𝖿 @TheDumperNetwork</b>"
        CallBackQuery.edit_message_text(text, reply_markup=reply_markup)

@bot.on_message(filters.text & filters.private)
async def insta(bot, msg):
    try:
        member = await bot.get_chat_member("DumperBots", msg.from_user.id)
        is_mem = True
    except UserNotParticipant:
        reply_markup = JOIN_BUTTON
        await msg.reply_text(text="<b>𝖸𝗈𝗎 𝗆𝗎𝗌𝗍 𝗃𝗈𝗂𝗇 𝗈𝗎𝗋 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 𝗍𝗈 𝗎𝗌𝖾 𝗍𝗁𝗂𝗌 𝗌𝖾𝗋𝗏𝗂𝖼𝖾</b>", reply_markup=reply_markup)
        return

    if is_mem:
        await msg.reply_text("<b>Processing..</b>")
        username = msg.text.replace("/find ", "")
        try:
            profile = instaloader.Profile.from_username(app.context, username)
        except:
            await msg.reply_text("<b>Kindly check the provided Username is Correct!</b>")
            return
        un = str(profile.username)
        ui = str(profile.userid)
        tp = str(profile.mediacount)
        fc = str(profile.followers)
        fp = str(profile.followees)
        bi = str(profile.biography)
        pfp = app.download_profile(username, profile_pic_only=True)
        text = "<b>𝙐𝙨𝙚𝙧𝙣𝙖𝙢𝙚 : " + un + "\n\n𝙐𝙨𝙚𝙧 𝙄𝘿 : " + ui + "\n\n𝙏𝙤𝙩𝙖𝙡 𝙋𝙤𝙨𝙩𝙨 : " + tp + "\n\n𝙁𝙤𝙡𝙡𝙤𝙬𝙚𝙧𝙨 𝘾𝙤𝙪𝙣𝙩 : " + fc + "\n\n𝙁𝙤𝙡𝙡𝙤𝙬𝙞𝙣𝙜 𝘾𝙤𝙪𝙣𝙩 : " + fp + "\n\n𝘽𝙞𝙤 :\n" + bi + "</b>"
        
        for images in os.listdir(username):
            if (images.endswith(".jpg")):
                img = images

        await msg.reply_photo(photo=username + "/" + img, caption=text)
        try:
            shutil.rmtree(username)
        except:
            time.sleep(2)

@bot.on_message(filters.command("find") & filters.all)
async def instaf(bot, msg):
    try:
        member = await bot.get_chat_member("DumperBots", msg.from_user.id)
        is_mem = True
    except UserNotParticipant:
        reply_markup = JOIN_BUTTON
        await msg.reply_text(text="<b>𝖸𝗈𝗎 𝗆𝗎𝗌𝗍 𝗃𝗈𝗂𝗇 𝗈𝗎𝗋 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 𝗍𝗈 𝗎𝗌𝖾 𝗍𝗁𝗂𝗌 𝗌𝖾𝗋𝗏𝗂𝖼𝖾</b>", reply_markup=reply_markup)
        return

    if is_mem:
        await msg.reply_text("<b>Processing..</b>")
        username = msg.text.replace("/find ", "")
        try:
            profile = instaloader.Profile.from_username(app.context, username)
        except:
            await msg.reply_text("<b>Kindly check the provided Username is Correct!</b>")
            return
        un = str(profile.username)
        ui = str(profile.userid)
        tp = str(profile.mediacount)
        fc = str(profile.followers)
        fp = str(profile.followees)
        bi = str(profile.biography)
        pfp = app.download_profile(username, profile_pic_only=True)
        text = "<b>𝙐𝙨𝙚𝙧𝙣𝙖𝙢𝙚 : " + un + "\n\n𝙐𝙨𝙚𝙧 𝙄𝘿 : " + ui + "\n\n𝙏𝙤𝙩𝙖𝙡 𝙋𝙤𝙨𝙩𝙨 : " + tp + "\n\n𝙁𝙤𝙡𝙡𝙤𝙬𝙚𝙧𝙨 𝘾𝙤𝙪𝙣𝙩 : " + fc + "\n\n𝙁𝙤𝙡𝙡𝙤𝙬𝙞𝙣𝙜 𝘾𝙤𝙪𝙣𝙩 : " + fp + "\n\n𝘽𝙞𝙤 :\n" + bi + "</b>"
        
        for images in os.listdir(username):
            if (images.endswith(".jpg")):
                img = images

        await msg.reply_photo(photo=username + "/" + img, caption=text)
        try:
            shutil.rmtree(username)
        except:
            time.sleep(2)

bot.run()
