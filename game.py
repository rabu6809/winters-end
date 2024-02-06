#------------------------------------
from random import *
from math import *
#------------------------------------
# battle system
class human:
  def __init__(perk):
    self.hp = 0
    self.bleed = 0
    self.ableed = 0
    self.cripple = 0
    self.fracture = 0
    self.i4s = 0
    self.perk = perk
    self.perkcd = 0
    self.ammo = 0
    self.gundmg = 0
    self.meleedmgh = 10
    self.meleedmgl = 5
