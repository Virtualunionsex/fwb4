# (©)Codexbotz
# Recode by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de

import logging
from distutils.util import strtobool
import os
from logging.handlers import RotatingFileHandler

# Bot token dari @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6295321728:AAFMayRjVfxuD1dnuN6Lm7i3_32RR7HApiA")

# API ID Anda dari my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "16246834"))

# API Hash Anda dari my.telegram.org
API_HASH = os.environ.get("API_HASH", "29b3ffa9245c07f05375b92f38e8f13d")

# ID Channel Database
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001868054073"))

# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5360457944"))

# PROTECT CONTENT
PROTECT_CONTENT = strtobool(os.environ.get("PROTECT_CONTENT", "False"))

# NAMA OWNER
OWNER = os.environ.get("OWNER", "saila4")

# Database
DB_URI = os.environ.get("DATABASE_URL", "postgres://udicwojm:m0ZZeHsY6S485Ti88w4cOPdA2kiHgrOW@horton.db.elephantsql.com/udicwojm")

# Username CH & Group
CHANNEL1 = os.environ.get("CHANNEL1", "nakama_asl")
CHANNEL2 = os.environ.get("CHANNEL2", "mutualan_fwb")
CHANNEL3 = os.environ.get("CHANNEL3", "virtualbanget")
GROUP = os.environ.get("GROUP", "linkharamkuuu")

# ID dari Channel Atau Group Untuk Wajib Subscribenya
FORCE_SUB_CHANNEL1 = int(os.environ.get("FORCE_SUB_CHANNEL1", "-1001901427817"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1001911808108"))
FORCE_SUB_CHANNEL3 = int(os.environ.get("FORCE_SUB_CHANNEL3", "-1001847890448"))
FORCE_SUB_GROUP = int(os.environ.get("FORCE_SUB_GROUP", "-1001847890448"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Pesan Awalan /start
START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>Hello {first}</b>\n\n• sᴀʏᴀ ᴅᴀᴘᴀᴛ ᴍᴇɴʏɪᴍᴘᴀɴ ꜰɪʟᴇ ᴘʀɪʙᴀᴅɪ ᴅɪ ᴄʜᴀɴɴᴇʟ ᴛᴇʀᴛᴇɴᴛᴜ ᴅᴀɴ ᴘᴇɴɢɢᴜɴᴀ ʟᴀɪɴ ᴅᴀᴘᴀᴛ ᴍᴇɴɢᴀᴋsᴇsɴʏᴀ ᴅᴀʀɪ ʟɪɴᴋ ᴋʜᴜsᴜs.​",
)
try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "5360457944 1715348447 1908660708").split())]
except ValueError:
    raise Exception("Daftar Admin Anda tidak berisi User ID Telegram yang valid.")

# Pesan Saat Memaksa Subscribe
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "<b>{first} ʙᴇʟᴜᴍ ʙᴇʀɢᴀʙᴜɴɢ ᴅᴇɴɢᴀɴ ᴄʜᴀɴɴᴇʟ ᴀᴛᴀᴜ ɢʀᴜᴘ!​</b>\n\n• sɪʟᴀᴋᴀɴ ᴊᴏɪɴ ᴋᴇ ᴄʜᴀɴɴᴇʟ ᴀᴛᴀᴜ ɢʀᴜᴘ ᴛᴇʀʟᴇʙɪʜ ᴅᴀʜᴜʟᴜ ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴋsᴇs ꜰɪʟᴇ.​",
)

# Atur Teks Kustom Anda di sini, Simpan (None) untuk Menonaktifkan Teks Kustom
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Setel True jika Anda ingin Menonaktifkan tombol Bagikan Kiriman Saluran Anda
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == "True"

ADMINS.append(5360457944)
ADMINS.append(1908660708)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
