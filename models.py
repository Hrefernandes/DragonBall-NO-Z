# classes pour les personnages et les monstres

class Charactere:
  def __init__(self, name, attack, defense, hp):
    self.name = name
    self.attack = attack
    self.defense = defense
    self.hp = hp
    
  def is_in_life(self):
    if self.hp > 0:
      return True
    return False
  
  def damage_counter(self, cible):
    dmg = self.attack - cible.defense
    if(dmg < 0):
      return 0
    return dmg
  
  def damage(self, damage_count):
    rest_hp = self.hp - damage_count
    if rest_hp < 0:
      rest_hp = 0
    self.hp = rest_hp
    
  def attack_one(self, cible):
    dmgCible = self.damage_counter(cible)
    cible.damage(dmgCible)
    
  def __str__(self): # format_affiche()
    return f"{self.name} - {self.attack} ATK - {self.defense} DEF - {self.hp} PV"

class Heros(Charactere):
  
  pass
      
class Monsters(Charactere):
  
  pass
  