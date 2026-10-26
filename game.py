from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["gameMongo"]

def menu_principal():
  print(" [1] Jouer \n")
  print(" [2] Classement \n")
  print(" [3] Quitter")
  
menuChoice = 0
  
while menuChoice < 1 or menuChoice > 3:
  menu_principal()
  menuChoice = int(input("*** : "))



# lancement du script
# menu avec choix
#   jouer
#     lance le jeux avec la saisie
#   classement
#     affiche table des scores
#   quitter

# saisie :
#   saisie nom
#   saisie nb heros ( max 3 )
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
