from pymongo import MongoClient

MONGO_URI = "mongodb+srv://ADMIN:ADMIN123@cluster0.5f40tnc.mongodb.net/?appName=Cluster0"

client = MongoClient(MONGO_URI)
db = client["imageDB"]
collection = db["images"]