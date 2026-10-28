
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
# [
#   "Lancer Jeu",
#   "Afficher les scores",
#   "Quitter"
#   ]
# Menu
#   Boucle sur tous elements de menu : start_menu()
# Choix (tableau option, error)
#   While true:
#    Recupérer choix utilisateur : choose_option()
#    Verifier si choix est valide
#    Si valide
#      lancer la fonction du choix : exe_option()
#    sinon
#      lancer la fonction error : show_error()
# Process
#   JEU : start_game()
#     Création d'un joueur : create_player()
#       Récuperer un nom valide
#         Boucle infini while
#           Demander de rentrer un nom : request_input()
#             Verifier si nom valide : is_name_valid()
#               Si nom valide
#                 return le nom
#               sinon
#                 error : show_error()
#     Création de l'équipe : create_teams()
#     Afficher les heros
#       Récuperer les heros en base : get_all()
#       init [hero_choisi]
#       while [hero_choisi] < 3
#         Récuperer les heros pas encore dans [hero_choisi] : get_hero_not_choose()
#         Afficher les heros restant : format_affiche()
#         while true
#           choix du joueur : request_input()
#           Verifier si choix est valide : is_choice_valid()
#             Si choix est valide
#               copie du [Heros] choisi dans [hero_choisi]
#               ajout de la colonne mort = false [hero_choisi] : create_hero()
#               afficher l'équipe actuel : show_equipe()
#               return
#             sinon
#               error : show_error()
#   COMBAT : start_fight()
#       init vagues
#       while team en vie: is_team_in_life()
#         Creation du monstre
#           Récuperer les monstres en base : get_all()
#           tirer un monstre au hasard: choose_random_monster()
#           copie du monstre choisi + ajout de la colonne mort = false : create_monsters()
#         Affiche info monstre : format_affiche()
#         Lancer le combat: start_fight_monster()
#           while monstre vivant && équipe en vie : is_in_life() && is_team_in_life()
#             Jouer un tour : start_round()
#               tour de l'équipe : round_player()
#                 Boucle sur les heros vivants : get_heros_in_life()
#                   hero attaque monstre : attack_one()
#                     calculer atk - def : damage_counter()
#                     retirer damage - pv : damage()
#                     Si
#                       pv cible = 0, cible morte
#                   Si monstre toujours vivant : est_vivant()
#                 Tour du monstre : round_monsters()
#                   choisir un hero vivant au hasard : choose_random_hero()
#                   le monstre attaque le hero : attack_one()
#                   calculer atk - def : damage_counter()
#                   retirer damage - pv : damage()
#          Si l'équipe est toujours en vie
#           vagues + 1
#          return vagues
#   Afficher les scores : show_scores()
#     Récupérer les scores en base
#       ouvrir base
#       acceder à la collection scores
#       find
#       convertir curseur en list
#     filtrer les 3 meilleurs
#       trier le tableau sur element.waves
#       prendre les 3 derniers elements array[-3:-1]
#     affiche les scores
#   Quitter
#     sys.exit()



### Correction (algo mis à jour avec les noms du code)
# MENU = [
#   ("Lancer Jeu", start_game),
#   ("Afficher les scores", show_scores),
#   ("Quitter", quit_game)
#   ]

# Menu : main()
#   Boucle infini while
#     Afficher les éléments du menu (numéro auto) : start_menu()
#     Récupérer le choix de l'utilisateur : choose_option()
#       Boucle infini while
#         Demander le choix : request_input()
#         Verifier si choix est valide : is_choice_valid()
#           Si valide
#             return l'option choisie
#           sinon
#             erreur : error()
#     lancer la fonction de l'option : option[1]()

# Process
#   JEU : start_game()
#     Création d'un joueur : create_player()
#       Boucle infini while
#         Demander de rentrer un pseudo : request_input()
#         Verifier si pseudo valide : is_pseudo_valid()
#           Si pseudo valide
#             return le pseudo
#           sinon
#             erreur : error()    (dans is_pseudo_valid)

#     Création de l'équipe : create_teams()
#       Récuperer les heros en base : get_heros()
#         get_all("heros") puis création d'un Heros pour chaque document
#       init [heros_choosen] = vide
#       while [heros_choosen] < 3 (TAILLE_EQUIPE)
#         Récuperer les heros pas encore dans [heros_choosen] : get_heros_not_choose()
#         Afficher les heros restants : show_list()  (affichage par __str__ de Charactere)
#         Choisir un hero : choose_hero()
#           Boucle infini while
#             choix du joueur : request_input()
#             Verifier si choix est valide : is_choice_valid()
#               Si choix est valide
#                 return le hero choisi
#               sinon
#                 erreur : error()   (dans is_choice_valid)
#         ajout du hero dans [heros_choosen]
#         afficher l'équipe actuelle : show_team()
#       return [heros_choosen]

#     COMBAT : start_fight()
#       init vagues = 0
#       while équipe en vie : is_team_in_life()
#         Création du monstre : choose_random_monster()
#           Récuperer les monstres en base : get_all("monsters")
#           tirer un monstre au hasard
#           création d'un Monsters avec ses stats
#         Lancer le combat : fight_monster()
#           Afficher info monstre : print(monstre)
#           while monstre vivant && équipe en vie : is_in_life() && is_team_in_life()
#             Jouer un tour : start_round()
#               tour de l'équipe : round_player()
#                 Boucle sur les heros vivants : get_in_life()
#                   Si monstre vivant : is_in_life()
#                     hero attaque monstre : attack_one()
#                       calculer atk - def (minimum 0) : damage_counter()
#                       retirer dégâts aux pv (minimum 0) : damage()
#                     afficher l'attaque
#               Si monstre toujours vivant : is_in_life()
#                 tour du monstre : round_monsters()
#                   choisir un hero vivant au hasard : choose_random_hero()
#                   le monstre attaque le hero : attack_one()
#                   afficher l'attaque
#         Si l'équipe est toujours en vie : is_team_in_life()
#           vagues + 1
#       return vagues

#     Sauvegarde du score : insert_score()
#       Verifier pseudo non vide et vagues est un entier
#       insert en base {"name", "waves"}
#     Affichage du résultat : show_result()
#       afficher pseudo + vagues survécues
#       Afficher les scores : show_scores()

#   Afficher les scores : show_scores()
#     Récupérer les scores en base : get_all("scores")
#     filtrer les 3 meilleurs : get_best_scores()
#       trier le tableau sur element.waves du plus grand au plus petit : get_waves()
#       prendre les 3 premiers elements array[:3]
#     afficher les scores
#   Quitter : quit_game()
#     sys.exit()


# is_pseudo_valid
# pseudo >= 3 (NOM_MIN)
# pseudo <= 50 (NOM_MAX)
# pseudo est pas déjà dans la db (collection scores)

# is_choice_valid
# choix est un nombre
# choix entre 1 et le nombre d'éléments de la liste