# menu et lancement du jeu

import sys
from game import start_game, show_scores
from utils import request_input, is_choice_valid

def quit_game():
  sys.exit()

MENU = [
  ("Lancer Jeu", start_game),
  ("Afficher les scores", show_scores),
  ("Quitter", quit_game)
]

def start_menu(menu):
  n = 1
  for option in menu:
    print(str(n) + " - " + option[0])
    n += 1

def choose_option(menu):
  while True:
    choice = request_input("Votre choix : ")
    if is_choice_valid(choice, menu):
      return menu[int(choice) - 1]

def main():
  while True:
    start_menu(MENU)
    option = choose_option(MENU)
    option[1]()

main()