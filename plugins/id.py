from pyrogram import Client, filters, enums
import logging
from Script import script
from pyrogram.errors import ChatAdminRequired
from database.ia_filterdb import Media2, Media3, Media4, Media5, get_file_details, get_search_results, get_bad_files, db as clientDB, db2 as clientDB2, db3 as clientDB3, db4 as clientDB4, db5 as clientDB5
from info import ADMINS, LOG_CHANNEL
from database.users_chats_db import db
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors.exceptions.bad_request_400 import MessageTooLong, PeerIdInvalid
import os, pytz, re, datetime, logging, asyncio, math, time, sys, psutil, shutil
from utils import get_size, temp, get_settings

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

@Client.on_message(filters.command('id'))
async def showid(client, message):
    chat_type = message.chat.type
    if chat_type == enums.ChatType.PRIVATE:
        user_id = message.chat.id
        mension = message.from_user.mention
        username = message.from_user.username
        dc_id = message.from_user.dc_id or ""
        await message.reply_text(f"👤 𝗨𝘀𝗲𝗿 𝗗𝗲𝘁𝗮𝗶𝗹𝘀\n○ Name : {mension} \n○ ID : <code>{user_id}</code> \n○ UserName : @{username} \n○ DC Id : <code>{dc_id}</code>")

    elif chat_type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:        
        chat_id = message.chat.id
        title = message.chat.title
        username = message.chat.username or "<b>None</b>"
        user_name = message.from_user.username or "<b>None</b>"
        user_id = message.from_user.id
        mension = message.from_user.mention
        dc_id = message.from_user.dc_id or "<b>None</b>"        
        if message.reply_to_message:
            from_dc_id = message.reply_to_message.from_user.dc_id or "<b>None</b>"
            from_user_name = message.reply_to_message.from_user.username or "<b>None</b>"
            from_mension = message.reply_to_message.from_user.mention
            from_id = message.reply_to_message.from_user.id or 'Anonymous'
            await message.reply(f"👤 𝗨𝘀𝗲𝗿 𝗗𝗲𝘁𝗮𝗶𝗹𝘀\n○ Name : {from_mension} \n○ ID : <code>{from_id}</code> \n○ UserName : @{from_user_name} \n○ DC Id : <code>{from_dc_id}</code> \n\n🔰  𝗖𝗵𝗮𝘁 𝗗𝗲𝘁𝗮𝗶𝗹𝘀\n○ Title : <code>{title}</code> \n○ ID : <code>{chat_id}</code> \n○ Type : <code>GROUP</code> \n○ UserName : @{username}")
        else:
            await message.reply(f"👤 𝗨𝘀𝗲𝗿 𝗗𝗲𝘁𝗮𝗶𝗹𝘀\n○ Name : {mension} \n○ ID : <code>{user_id}</code> \n○ UserName : @{user_name} \n○ DC Id : <code>{dc_id}</code> \n\n🔰  𝗖𝗵𝗮𝘁 𝗗𝗲𝘁𝗮𝗶𝗹𝘀\n○ Title : <code>{title}</code> \n○ ID : <code>{chat_id}</code> \n○ Type : <code>GROUP</code> \n○ UserName : @{username}")
        
    elif chat_type == enums.ChatType.CHANNEL:
        chat_id = message.chat.id
        title = message.chat.title
        username = message.chat.username or "<b>None</b>"
        await message.edit(f"➪ Title : <b>{title}</b> \n➪ ID : <code>{chat_id}</code> \n➪ Type : <b>CHANNEL</b> \n➪ UserName : @{username}")

@Client.on_message(filters.command('status') & filters.user(ADMINS))
async def get_stats(bot, message):
    rju = await message.reply('⚡')
    tot1 = await Media2.count_documents()
    tot2 = await Media3.count_documents()
    tot3 = await Media4.count_documents()
    tot4 = await Media5.count_documents()
    total = tot1 + tot2 + tot3 + tot4
    users = await db.total_users_count()
    chats = await db.total_chat_count()
    stats = await clientDB.command('dbStats')
    used_dbSize = (stats['dataSize']/(1024*1024))+(stats['indexSize']/(1024*1024))        
    stats2 = await clientDB2.command('dbStats')
    used_dbSize2 = (stats2['dataSize']/(1024*1024))+(stats2['indexSize']/(1024*1024))
    stats3 = await clientDB3.command('dbStats')
    used_dbSize3 = (stats3['dataSize']/(1024*1024))+(stats3['indexSize']/(1024*1024))  
    stats4 = await clientDB4.command('dbStats')
    used_dbSize4 = (stats4['dataSize']/(1024*1024))+(stats4['indexSize']/(1024*1024))  
    stats5 = await clientDB5.command('dbStats')
    used_dbSize5 = (stats5['dataSize']/(1024*1024))+(stats5['indexSize']/(1024*1024))  
    current = temp.CURRENT
    tz = pytz.timezone('Asia/Kolkata')
    today = datetime.date.today()
    now = datetime.datetime.now(tz)
    time = now.strftime("%I:%M:%S %p - %d %b, %Y")
    await rju.edit(
        text=script.STATUS_TXT.format(total, users, chats, round(used_dbSize, 2), tot1, round(used_dbSize2, 2), tot2, round(used_dbSize3, 2), tot3, round(used_dbSize4, 2), tot4, round(used_dbSize5, 2), time),
        parse_mode=enums.ParseMode.HTML)
