# logique de combat

import random
from db import get_all, insert_score
from utils import *
from models import Heros, Monsters

# constantes
NOM_MIN = 3
NOM_MAX = 50
TAILLE_EQUIPE = 3
NB_MEILLEURS_SCORES = 3

def is_pseudo_valid(pseudo):
  if len(pseudo) < NOM_MIN or len(pseudo) > NOM_MAX:
    error("Le pseudo doit faire entre 3 et 50 caractères")
    return False
  for score in get_all("scores"):
    if score["name"] == pseudo:
      error("Pseudo déjà utilisé")
      return False
  return True

def get_heros():
  heros = []
  for h in get_all("heros"):
    heros.append(Heros(h["name"], h["attack"], h["defense"], h["hp"]))
  return heros

def create_player():
  while True:
    pseudo = request_input("Pseudo : ")
    if is_pseudo_valid(pseudo):
      return pseudo

def choose_hero(heros_remaining):
  while True:
    choice = request_input("Votre choix : ")
    if is_choice_valid(choice, heros_remaining):
      return heros_remaining[int(choice) - 1]

def create_teams():
  heros = get_heros()
  heros_choosen = []
  while len(heros_choosen) < TAILLE_EQUIPE:
    heros_remaining = get_heros_not_choose(heros, heros_choosen)
    show_list(heros_remaining)
    heros_choosen.append(choose_hero(heros_remaining))
    show_team(heros_choosen)
  return heros_choosen

def get_waves(score):
  return score["waves"]

def get_best_scores(scores):
  scores.sort(key=get_waves, reverse=True)
  return scores[:NB_MEILLEURS_SCORES]

def show_scores():
  print("Meilleurs scores :")
  n = 1
  for score in get_best_scores(get_all("scores")):
    print(str(n) + " - " + score["name"] + " - " + str(score["waves"]) + " vagues")
    n += 1
    
def round_player(team, monsters):
  heros_alive = get_in_life(team)
  for hero in heros_alive:
    if monsters.is_in_life():
      hero.attack_one(monsters)
      print(hero.name + " attaque " + monsters.name + " : il lui reste " + str(monsters.hp) + " PV")
  
def choose_random_hero(team):
  return random.choice(get_in_life(team))

def round_monsters(team, monsters):
  cible = choose_random_hero(team)
  monsters.attack_one(cible)
  print(monsters.name + " attaque " + cible.name + " : il lui reste " + str(cible.hp) + " PV")
  
def start_round(team, monsters):
  round_player(team, monsters)
  if monsters.is_in_life():
    round_monsters(team, monsters)

def fight_monster(team, monsters):
  print("Un " + monsters.name + " apparaît !")
  print(monsters)
  while monsters.is_in_life() and len(get_in_life(team)) > 0:
    start_round(team, monsters)

def choose_random_monster():
  m = random.choice(get_all("monsters"))
  return Monsters(m["name"], m["attack"], m["defense"], m["hp"])

def is_team_in_life(team):
  return len(get_in_life(team)) > 0

def start_fight(team):
  waves = 0
  while is_team_in_life(team):
    monsters = choose_random_monster()
    fight_monster(team, monsters)
    if is_team_in_life(team):
      waves += 1
      print("Vague " + str(waves) + " réussie !")
  return waves

def show_result(pseudo, waves):
  print("Fin de partie " + pseudo + " : " + str(waves) + " vagues survécues")
  show_scores()

def start_game():
  pseudo = create_player()
  team = create_teams()
  waves = start_fight(team)
  insert_score(pseudo, waves)
  show_result(pseudo, waves)