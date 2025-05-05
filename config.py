
import os
import logging
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton




#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7870123481:AAE73L84skV7myPfbIGSwjLaZ14LKJG-Zbc")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "26341867"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "81fd4d73ae50f1d94dba355f28c10e22")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002667614225"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "7964416919"))

#Port
PORT = os.environ.get("PORT", "8043")

DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://wtflinksofficial:wtflinksofficial@cluster0.uziwt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "titubadmoshbottest")




IS_VERIFY = os.environ.get("IS_VERIFY", "True")
TUT_VID = os.environ.get("TUT_VID", "https://t.me/delight_link/2")



TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

START_PIC = os.environ.get("START_PIC", "https://envs.sh/kEh.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://envs.sh/kEh.jpg")

QR_PIC = os.environ.get("QR_PIC", "https://envs.sh/kEh.jpg")






#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b></b>")

#Collection of pics for Bot // #Optional but atleast one pic link should be replaced if you don't want predefined links
PICS = (os.environ.get("PICS", "https://envs.sh/kEh.jpg https://envs.sh/kEh.jpg https://envs.sh/kEh.jpg https://envs.sh/kEh.jpg")).split() #Required


#==========================(BUY PREMIUM)====================#

PREMIUM_BUTTON = reply_markup=InlineKeyboardMarkup(
        [[InlineKeyboardButton("Remove Ads In One Click", callback_data="buy_prem")]]
)

PREMIUM_BUTTON2 = reply_markup=InlineKeyboardMarkup(
        [[InlineKeyboardButton("Remove Ads In One Click", callback_data="buy_prem")]]
) 

OWNER_TAG = os.environ.get("OWNER_TAG", "Titubadmosh")

#UPI ID
UPI_ID = os.environ.get("UPI_ID", "@Titubadmosh")

#UPI QR CODE IMAGE
UPI_IMAGE_URL = os.environ.get("UPI_IMAGE_URL", "https://envs.sh/kEh.jpg")

#SCREENSHOT URL of ADMIN for verification of payments
SCREENSHOT_URL = os.environ.get("SCREENSHOT_URL", f"t.me/Titubadmosh")



#Time and its price

#7 Days
PRICE1 = os.environ.get("PRICE1", "169 rs")

#1 Month
PRICE2 = os.environ.get("PRICE2", "269 rs")

#3 Month
PRICE3 = os.environ.get("PRICE3", "369 rs")

#6 Month
PRICE4 = os.environ.get("PRICE4", "469 rs")

#1 Year
PRICE5 = os.environ.get("PRICE5", "669 rs")


#===================(END)========================#


#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("True", True) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "âŒDon't send me messages directly I'm only File Sharing Bot!"




LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
