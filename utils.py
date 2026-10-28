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

def choose_option(options, message="Votre choix : "):
  while True:
    choice = request_input(message)
    if is_choice_valid(choice, options):
      return int(choice)

def create_hero_choice_message(heros_remaining):
    return "Choisissez votre héros (1-" + str(len(heros_remaining)) + ") : "