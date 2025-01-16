
import os
import logging
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton




#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7615437696:AAHs0_Bu52Fr4uMGh1rYqKExzfxoU4iKXvo")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "23702904"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "e67f2061769a4d4a44dca1781f9bb619")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002399704662"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6358850593"))

#Port
PORT = os.environ.get("PORT", "6726")

DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://wtflinksofficial:wtflinksofficial@cluster0.ff5tu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "wtflinksofficial")




IS_VERIFY = os.environ.get("IS_VERIFY", "True")
TUT_VID = os.environ.get("TUT_VID", "https://t.me/delight_link/2")



TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/ec17880d61180d3312d6a.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://telegra.ph/file/e292b12890b8b4b9dcbd1.jpg")

QR_PIC = os.environ.get("QR_PIC", "https://envs.sh/NrS.jpg")






#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b></b>")

#Collection of pics for Bot // #Optional but atleast one pic link should be replaced if you don't want predefined links
PICS = (os.environ.get("PICS", "https://envs.sh/4Iq.jpg https://envs.sh/4IW.jpg https://envs.sh/4IB.jpg https://envs.sh/4In.jpg")).split() #Required


#==========================(BUY PREMIUM)====================#

PREMIUM_BUTTON = reply_markup=InlineKeyboardMarkup(
        [[InlineKeyboardButton("Remove Ads In One Click", callback_data="buy_prem")]]
)

PREMIUM_BUTTON2 = reply_markup=InlineKeyboardMarkup(
        [[InlineKeyboardButton("Remove Ads In One Click", callback_data="buy_prem")]]
) 

OWNER_TAG = os.environ.get("OWNER_TAG", "zenotty")

#UPI ID
UPI_ID = os.environ.get("UPI_ID", "@amharshu@ybl")

#UPI QR CODE IMAGE
UPI_IMAGE_URL = os.environ.get("UPI_IMAGE_URL", "https://envs.sh/NrS.jpg")

#SCREENSHOT URL of ADMIN for verification of payments
SCREENSHOT_URL = os.environ.get("SCREENSHOT_URL", f"t.me/zenotty")



#Time and its price

#7 Days
PRICE1 = os.environ.get("PRICE1", "0 rs")

#1 Month
PRICE2 = os.environ.get("PRICE2", "60 rs")

#3 Month
PRICE3 = os.environ.get("PRICE3", "150 rs")

#6 Month
PRICE4 = os.environ.get("PRICE4", "280 rs")

#1 Year
PRICE5 = os.environ.get("PRICE5", "550 rs")


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
