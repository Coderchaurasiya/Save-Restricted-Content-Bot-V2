# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "29107607"))
API_HASH = getenv("API_HASH", "9141f8bd7cb56ecbf580970869741448")
BOT_TOKEN = getenv("BOT_TOKEN", "7214328741:AAHI8lBhkWLe3Mah9rrNblalJ1rqpeS57Nc")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5410788146").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://coderchaurasiya:13512825@Sonammeenaa@cluster0.qfdnmik.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "1727909739")
CHANNEL_ID = int(getenv("CHANNEL_ID", "2243728954"))
