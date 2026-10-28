# récupérer les data db

from utils import error
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client.gameMongo

def get_all(nom_collection):
  if nom_collection not in db.list_collection_names():
    error("Collection introuvable : " + nom_collection)
    return []
  return list(db[nom_collection].find())

def insert_score(name, waves):
  if name is None or name == "":
    error("Nom invalide")
    return
  if not isinstance(waves, int):
    error("Nombre de vagues invalide")
    return
  db.scores.insert_one({"name": name, "waves": waves})
