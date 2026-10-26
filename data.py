from pymongo import MongoClient
from bson import ObjectId

client = MongoClient('mongodb://localhost:27017/')

db = client.gameMongo
collection = db.monsters

collection.drop()

collection.insert_many([{
  "_id": ObjectId("678ede35e38b86e326b876b7"),
  "name": "Gobelin",
  "attack": 10,
  "defense": 6,
  "hp": 150
},
{
  "_id": ObjectId("678ede35e38b86e326b876b8"),
  "name": "Orc",
  "attack": 10,
  "defense": 8,
  "hp": 180
},
{
  "_id": ObjectId("678ede35e38b86e326b876b9"),
  "name": "Dragon",
  "attack": 10,
  "defense": 12,
  "hp": 200
},
{
  "_id": ObjectId("678ede35e38b86e326b876ba"),
  "name": "Zombie",
  "attack": 10,
  "defense": 7,
  "hp": 160
},
{
  "_id": ObjectId("678ede35e38b86e326b876bb"),
  "name": "Troll",
  "attack": 10,
  "defense": 10,
  "hp": 190
},
{
  "_id": ObjectId("678ede35e38b86e326b876bc"),
  "name": "Spectre",
  "attack": 24,
  "defense": 6,
  "hp": 170
},
{
  "_id": ObjectId("678ede35e38b86e326b876bd"),
  "name": "Golem",
  "attack": 21,
  "defense": 14,
  "hp": 210
},
{
  "_id": ObjectId("678ede35e38b86e326b876be"),
  "name": "Vampire",
  "attack": 26,
  "defense": 9,
  "hp": 175
},
{
  "_id": ObjectId("678ede35e38b86e326b876bf"),
  "name": "Loup-garou",
  "attack": 24,
  "defense": 8,
  "hp": 185
},
{
  "_id": ObjectId("678ede35e38b86e326b876c0"),
  "name": "Squelette",
  "attack": 19,
  "defense": 7,
  "hp": 155
}])

collection = db.heros

collection.drop()

collection.insert_many([
    {
    "_id": ObjectId("678ede35e38b86e326b876ad"),
    "name": "Paladin",
    "attack": 20,
    "defense": 12,
    "hp": 120
    },
    {
    "_id": ObjectId("678ede35e38b86e326b876ae"),
    "name": "Chevalier",
    "attack": 22,
    "defense": 10,
    "hp": 110
    },
    {
    "_id": ObjectId("678ede35e38b86e326b876af"),
    "name": "Berserker",
    "attack": 29,
    "defense": 6,
    "hp": 90
    },
    {
    "_id": ObjectId("678ede35e38b86e326b876b0"),
    "name": "Archer",
    "attack": 26,
    "defense": 7,
    "hp": 85
    },
    {
    "_id": ObjectId("678ede35e38b86e326b876b1"),
    "name": "Sorcier",
    "attack": 32,
    "defense": 4,
    "hp": 75
    },
    {
    "_id": ObjectId("678ede35e38b86e326b876b2"),
    "name": "Guerrier",
    "attack": 24,
    "defense": 8,
    "hp": 100
    },
    {
    "_id": ObjectId("678ede35e38b86e326b876b3"),
    "name": "Moine",
    "attack": 22,
    "defense": 9,
    "hp": 95
    },
    {
    "_id": ObjectId("678ede35e38b86e326b876b4"),
    "name": "Voleur",
    "attack": 28,
    "defense": 5,
    "hp": 80
    },
    {
    "_id": ObjectId("678ede35e38b86e326b876b5"),
    "name": "Chasseur",
    "attack": 23,
    "defense": 8,
    "hp": 90
    },
    {
    "_id": ObjectId("678ede35e38b86e326b876b6"),
    "name": "Druide",
    "attack": 21,
    "defense": 9,
    "hp": 100
    }
])
