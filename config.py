# devgaganin
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "29091972"))
API_HASH = getenv("API_HASH", "b12b66034ad60391a27aafa5cbc47f30")
BOT_TOKEN = getenv("BOT_TOKEN", "7510574909:AAHgqp_Kl4P-j0fzjZWvhplun0IlY7gh8z8")
OWNER_ID = int(getenv("OWNER_ID", "7929753755"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "mongodb+srv://sonamex12:DAjDM7LHtIRANcYl@cluster0.tuppn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = int(getenv("LOG_GROUP", "2377102536"))
FORCESUB = getenv("FORCESUB", "fukkcy")
DEFAULT_SESSION = getenv("DEFAULT_SESSION", "") # this is jkust to help if you dont want to force your bot user to login or if they not interested
