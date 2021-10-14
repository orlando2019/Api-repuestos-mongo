from pymongo import MongoClient


MONGO_URI = (
    "mongodb://localhost:27017/?readPreference=primary&directConnection=true&ssl=false"
)

client = MongoClient(MONGO_URI)

db = client.almacen

collection_repuestos = db["repuestos"]
