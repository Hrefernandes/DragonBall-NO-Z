# fonction affichage et gestion des données

def error(err):
  print(err)

def request_input(message):
  pick = input(message)
  return pick.strip()

def show_list(elements):
  n = 1
  for element in elements:
    print(str(n) + " - " + str(element))
    n += 1

def get_heros_not_choose(heros, heros_choosen):
  remaining = []
  for hero in heros:
    if hero not in heros_choosen:
      remaining.append(hero)
  return remaining

def is_choice_valid(choice, heros_remaining):
  if not choice.isdigit():
    error("Entrez un nombre")
    return False
  numero = int(choice)
  if numero < 1 or numero > len(heros_remaining):
    error("Ce numéro n'est pas dans votre liste")
    return False
  return True

def show_team(hero_choosen):
  print("Votre équipe :")
  show_list(hero_choosen)

def get_in_life(characters):
  in_life = []
  for character in characters:
    if character.is_in_life():
      in_life.append(character)
  return in_life