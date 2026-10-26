from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["testDb"]

users_collection = db["users"]

protected_users = users_collection.find({"age": {"$gt": 23}},  {"_id": 0, "name": 1})

for users in protected_users:
  print("A plus de 23 ans :", users)
  

# lancement du script
# saisie :
#   saisie nb heros
#   saisie nom
#   affichage des infos heros
#     saisie selection des heros
# debut de la partie
#   resume bataille du round
#     info hero
#     details attaque
#     info monstre
# tant que tous les heros ont pas leur vie à 0 ou en dessous saisie entré lancement d'une manche
# sinon message de fin de partie
#   detail heros
#   manche atteinte
#   ajout des données dans la table score
