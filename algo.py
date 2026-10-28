
# lancement du script
# menu avec choix
#   jouer
#     lance le jeux avec la saisie ->
#   classement
#     affiche table des scores
#   quitter

# saisie :
#   saisie nom (non vide)
#   affichage des infos heros
#     saisie selection des heros (non vide) (3 heros)
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


### Correction
# MENU = [
#   ("Lancer Jeu", start_game),
#   ("Afficher les scores", show_scores),
#   ("Quitter", quit_game)
#   ]
# Menu : main()
#   While true:
#    Boucle sur tous elements de menu : start_menu()
#    Recupérer choix utilisateur : choose_option()
#      While true:
#       Demander le choix : request_input()
#       Verifier si choix est valide : is_choice_valid()
#       Si valide
#         return l'option choisie
#       sinon
#         lancer la fonction error : error()
#    lancer la fonction du choix
# Process
#   JEU : start_game()
#     Création d'un joueur : create_player()
#       Récuperer un pseudo valide
#         Boucle infini while
#           Demander de rentrer un pseudo : request_input()
#             Verifier si pseudo valide : is_pseudo_valid()
#               Si pseudo valide
#                 return le pseudo
#               sinon
#                 error : error()
#     Création de l'équipe : create_teams()
#     Afficher les heros
#       Récuperer les heros en base : get_heros()
#       init [heros_choosen]
#       while [heros_choosen] < 3
#         Récuperer les heros pas encore dans [heros_choosen] : get_heros_not_choose()
#         Afficher les heros restant : show_list()
#         Choisir un hero : choose_hero()
#           while true
#             choix du joueur : request_input()
#             Verifier si choix est valide : is_choice_valid()
#               Si choix est valide
#                 return le hero choisi
#               sinon
#                 error : error()
#         ajout du hero dans [heros_choosen]
#         afficher l'équipe actuel : show_team()
#       return [heros_choosen]
#   COMBAT : start_fight()
#       init waves
#       while team en vie: is_team_in_life()
#         Creation du monstre
#           Récuperer les monstres en base
#           tirer un monstre au hasard : choose_random_monster()
#           création d'un objet Monsters
#         Lancer le combat: fight_monster()
#           Affiche info monstre
#           while monstre vivant && équipe en vie : is_in_life() && is_team_in_life()
#             Jouer un tour : start_round()
#               tour de l'équipe : round_player()
#                 Boucle sur les heros vivants : get_in_life()
#                   Si monstre vivant : is_in_life()
#                     hero attaque monstre : attack_one()
#                       atk - def : damage_counter()
#                       damage - pv : damage()
#                     afficher l'attaque
#               Si monstre toujours vivant : is_in_life()
#                 Tour du monstre : round_monsters()
#                   choisir un hero vivant au hasard : choose_random_hero()
#                   le monstre attaque le hero : attack_one()
#                   afficher l'attaque
#         Si l'équipe est toujours en vie : is_team_in_life()
#           waves + 1
#       return waves
#     Sauvegarder le score : insert_score()
#       Verifier si pseudo pas vide et vagues est un int
#       insert du pseudo et des vagues dans la collection scores
#     Afficher le résultat : show_result()
#       affiche le pseudo et les vagues
#       Afficher les scores : show_scores()
#   Afficher les scores : show_scores()
#     Récupérer les scores en base : get_all()
#       ouvrir base
#       acceder à la collection scores
#       find
#       convertir curseur en list
#     filtrer les 3 meilleurs : get_best_scores()
#       trier le tableau sur element.waves du plus grand au plus petit : get_waves()
#       prendre les 3 premiers elements array[:3]
#     affiche les scores
#   Quitter : quit_game()
#     sys.exit()


# is_pseudo_valid
# pseudo >= 3
# pseudo <= 50
# pseudo est pas déjà dans la db

# is_choice_valid
# choix est un nombre
# choix est dans la liste (entre 1 et la taille de la liste)