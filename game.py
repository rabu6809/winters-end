#------------------------------------
from random import *
from math import *
#------------------------------------
# battle system
class human:
  def __init__(self,perk):
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
    if perk == "exe":
      self.hp = 130
      self.meleedmgh = 14
      self.meleedmgl = 7
    elif perk == "art":
      self.hp = 90
      self.meleedmgh = 8
      self.meleedmgl = 4
      self.deadeye = 0
    elif perk == "laz":
      self.hp = 110
      self.laz = 0
  def effect(self,id,len):
    if id = 1:
    
