class script(object):
    START_TXT = """<b>𝖧𝖾𝗒 {}, 𝖨 𝖠𝗆 <a href=https://t.me/{}>{}</a>, 𝖧𝖺𝗉𝗉𝗒 🖤 𝖳𝗈 𝖧𝖺𝗏𝖾 𝖸𝗈𝗎

𝖨𝖺𝗆 𝖯𝗈𝗐𝖾𝗋𝖥𝗎𝗅𝗅 𝖠𝗎𝗍𝗈 𝖥𝗂𝗅𝗍𝖾𝗋 + 𝖬𝗈𝗏𝗂𝖾 𝖲𝖾𝖺𝗋𝖼𝗁 + 𝖬𝖺𝗇𝗎𝖺𝗅 𝖥𝗂𝗅𝗍𝖾𝗋 𝖡𝗈𝗍 ⚙
    
Here You Can Request Movie's, Just Sent <a href='https://t.me/CinemaKalavaraMoviesBot'>Movie Name</a> With Proper <a href='https://www.google.com/'>Google</a> Spelling..!!</b>"""
    
    OLD_ALRT_TXT = """ʜᴇʏ {},
ʏᴏᴜ ᴀʀᴇ ᴜꜱɪɴɢ ᴏɴᴇ ᴏꜰ ᴍʏ ᴏʟᴅ ᴍᴇꜱꜱᴀɢᴇꜱ, 
ᴘʟᴇᴀꜱᴇ ꜱᴇɴᴅ ᴛʜᴇ ʀᴇQᴜᴇꜱᴛ ᴀɢᴀɪɴ."""
       
  
    CUSTOM_FILE_CAPTION = """<b>𝐻𝑒𝑙𝑙𝑜 👋 {mention} 😍

{file_name}
    
⚙️ Fɪʟᴇ Sɪᴢᴇ :  {file_size}

 ╔═══ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ═══╗
 ♻️ 𝑱𝑶𝑰𝑵 :- <a href=https://t.me/Cinemakalavara_Group> 𝐆𝐑𝐎𝐔𝐏 </a>
 ♻️ 𝑱𝑶𝑰𝑵 :- <a href=https://t.me/+EcKqKBOrLHE3YTZl> 𝐎𝐓𝐓 𝐔𝐏𝐃𝐀𝐓𝐄𝐒 </a>
 ♻️ 𝑱𝑶𝑰𝑵 :- <a href=https://t.me/CinemaKalavaraTG> 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 </a>
 ╚═══ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ═══╝</b>""" 
    
    STATUS_TXT = """📂 𝖳𝗈𝗍𝖺𝗅 𝖥𝗂𝗅𝖾𝗌     - <code>{}</code>

𒆜  𝗗𝗕 1️⃣
╭ ▸ 𝖴𝗌𝖾𝗋𝗌 : <code>{}</code>
├ ▸ 𝖢𝗁𝖺𝗍𝗌  : <code>{}</code>
╰ ▸ 𝖴𝗌𝖾𝖽 𝖲𝗍𝗈𝗋𝖺𝗀𝖾: <code>{}</code>MB

 𒆜 𝗗𝗕 2️⃣
╭ ▸ 𝖳𝗈𝗍𝖺𝗅 𝖥𝗂𝗅𝖾𝗌 : <code>{}</code>
╰ ▸ 𝖴𝗌𝖾𝖽 𝖲𝗍𝗈𝗋𝖺𝗀𝖾: <code>{}</code>MB

 𒆜 𝗗𝗕 3️⃣ 
╭ ▸ 𝖳𝗈𝗍𝖺𝗅 𝖥𝗂𝗅𝖾𝗌 : <code>{}</code>
╰ ▸ 𝖴𝗌𝖾𝖽 𝖲𝗍𝗈𝗋𝖺𝗀𝖾: <code>{}</code>MB

𒆜  𝗗𝗕 4️⃣
╭ ▸ 𝖳𝗈𝗍𝖺𝗅 𝖥𝗂𝗅𝖾𝗌 : <code>{}</code>
╰ ▸ 𝖴𝗌𝖾𝖽 𝖲𝗍𝗈𝗋𝖺𝗀𝖾: <code>{}</code>MB

𒆜 𝗗𝗕 5️⃣
╭ ▸ 𝖳𝗈𝗍𝖺𝗅 𝖥𝗂𝗅𝖾𝗌 : <code>{}</code>
╰ ▸ 𝖴𝗌𝖾𝖽 𝖲𝗍𝗈𝗋𝖺𝗀𝖾: <code>{}</code>MB"""
    
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
    
    SEARCH_TXT = """<b>📨 Sᴇɴᴅ Mᴏᴠɪᴇ Nᴀᴍᴇ ᴀɴᴅ Yᴇᴀʀ Aꜱ Pᴇʀ Gᴏᴏɢʟᴇ Sᴘᴇʟʟɪɴɢ..!! 👍

📨 നിങ്ങൾക്ക് ആവശ്യമുള്ള മൂവിയുടെ പേര്, വർഷം Google ഉളളത് പോലെ അയക്കുക..!! 👍

⚠️ Exᴀᴍᴘʟᴇ 👇

👉 Jailer
👉 Jailer 2023

⚠️ ᴅᴏɴ'ᴛ ᴀᴅᴅ ᴇᴍᴏᴊɪꜱ ᴀɴᴅ ꜱʏᴍʙᴏʟꜱ ɪɴ ᴍᴏᴠɪᴇ ɴᴀᴍᴇ, ᴜꜱᴇ ʟᴇᴛᴛᴇʀꜱ ᴏɴʟʏ..!! ❌</b>"""
    
