# initialisation de la bdd

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client.gameMongo

# Monstres
collection = db.monsters
collection.drop() # écrase et recharge les données

collection.insert_many([
    {"name": "Saibaman",   "attack": 10, "defense": 6,  "hp": 150},
    {"name": "Dodoria",    "attack": 10, "defense": 8,  "hp": 180},
    {"name": "Jiren",      "attack": 10, "defense": 12, "hp": 200},
    {"name": "Cell Junior", "attack": 10, "defense": 7, "hp": 160},
    {"name": "Cell (forme finale)",      "attack": 10, "defense": 10, "hp": 190},
    {"name": "Majin Vegeta",        "attack": 24, "defense": 6,  "hp": 170},
    {"name": "Broly",      "attack": 21, "defense": 14, "hp": 210},
    {"name": "Goku Black", "attack": 26, "defense": 9,  "hp": 175},
    {"name": "Kid buu",       "attack": 24, "defense": 8,  "hp": 185},
    {"name": "Freezer",    "attack": 19, "defense": 7,  "hp": 155},
])

# Heros
collection = db.heros
collection.drop()

collection.insert_many([
    {"name": "Piccolo",       "attack": 20, "defense": 12, "hp": 120},
    {"name": "C-17",          "attack": 22, "defense": 10, "hp": 110},
    {"name": "Vegeta",        "attack": 29, "defense": 6,  "hp": 90},
    {"name": "Trunks SSJ1",        "attack": 26, "defense": 7,  "hp": 85},
    {"name": "Goku",          "attack": 32, "defense": 4,  "hp": 75},
    {"name": "Tenshinhan",    "attack": 24, "defense": 8,  "hp": 100},
    {"name": "Krilin",        "attack": 22, "defense": 9,  "hp": 95},
    {"name": "Gohan Beast",         "attack": 28, "defense": 5,  "hp": 80},
    {"name": "C-18",          "attack": 23, "defense": 8,  "hp": 90},
    {"name": "Vegeta (Gorille geant)",  "attack": 21, "defense": 9,  "hp": 100},
])

# Scores
collection = db.scores
collection.drop()

collection.insert_many([
    {"name": "Sacha",   "waves": 7},
    {"name": "Lina",    "waves": 20},
    {"name": "Maxime",  "waves": 3},
])

print("Base créer.")