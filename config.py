# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID", "25933223"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH", "6ef5a426d85b7f01562a41e6416791d3")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7048745210:AAEGqNT9HhWBQzglDafW2T3g_UQTUX0aoPo")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("@Cwuplbot")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID", "8118667253"))
# ------------------X------------------------------

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "8118667253").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002825795936"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://biklriplit:efaXfv2Ps9MRfner@cluster0.4hfu8zj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS", "-1002825795936"))

