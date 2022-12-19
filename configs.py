import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 28441359))
    API_HASH = os.environ.get("API_HASH", "31a34594749d5458ab9b39a48dc24337")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5435726932:AAEtsQFePAv3-eXqueilJGJMG-p73KrgYrE")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "LinkSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "BQBOlGqmr80NfpaoorRFhhZO4P44HmSfESfPBCrPYJFABKX12W2bERFTCzrhgixCJIFUw5TqPRDCs8pvuSHObLncD304JReaPgMD9g0xoyvfTO1yP5PXQ1F4kjC9avADES1mm3reAY8OBUHCC3CjsR1u90GorE5ZL4SYqKHfQfXI-Pn1rg5_KljH4jb7iF8IZLbTsVawU2Nu_jYMETmf-x86QtWQDdlw8KhV6Ofoz0PZ6ZHwAP7kuRFO-tayz_EVevjCDakO1I9N9TDkG4uPCpZ4NSqH_6LeGvWExEPt5hBk-1V4k2y53xP_eavTMUb2nfL_UVDUumM2KoBU50cP7HU-AAAAAWJ5xDEA")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -1001858898420))
    BOT_USERNAME = os.environ.get("BOT_USERNAME"Mdiskmoviesearch26bot)
    BOT_OWNER = int(os.environ.get("BOT_OWNER"5947114545))
    DATABASE_URL = os.environ.get("DATABASE_URL"mongodb+srv://Yogi26:8059530482@@cluster0.tlutr2j.mongodb.net/?retryWrites=true&w=majority)
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    ABOUT_BOT_TEXT = """<b>This is Link Search Bot.
    
    
    
🤖 My Name: <a href='https://youtube.com/@GreyMattersBot'>Link Search Bot</a>

📝 Language : <a href='https://www.python.org'> Python V3</a>

📚 Library: <a href='https://docs.pyrogram.org'> Pyrogram</a>

📡 Server: <a href='koyeb.com'>Koyeb</a>

👨‍💻 Created By: <a href='https://t.me/GreyMatter_Bot'>GreyMatter's Bot</a></b>
"""

    ABOUT_HELP_TEXT = """<b>👨‍💻 Creator : <a href='https://t.me/GreyMatter_Bot'>GreyMatter's Bot</a>
If You Want Your Own Bot Like This Then You Can Contact Our Creator.</b>
"""

    HOME_TEXT = """
<b>Hey! {}😅,

I'm Link Search Bot.🤖

I Can Search 🔍 What You Want❗

<a>Made With ❤ By @GreyMatter_Bots</a></b>
"""


    START_MSG = """
<b>Hey! {}😅,

I'm Link Search Bot.🤖

I Can Search 🔍 What You Want❗

<a>Made With ❤ By @GreyMatter_Bots</a></b>
"""

