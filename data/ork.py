import pygame
import enemy
import pool
from pool import Var
import fightpic_functions
import random
import blaster


## class Ork
## ... __init__(name, typ, pos, transparency=255, ID=0)


class Ork(enemy.Enemy):
    def __init__(self, name, typ, pos, transparency=255, ID=0):  #noch von hero übernommen
        enemy.Enemy.__init__(self, name, typ, pos, transparency, ID) #noch von hero übernommen

        self.mask_mid = [144,126]
        self.walk_animation_delay = 5 #schon verändert: eins höher als hero
        self.walk_animation_frame_countdown = self.walk_animation_delay
        self.speed = 3  #schon verändert: drei niedriger als hero
        self.defense_dexterity = 50 # von 100  - beschreibt, wie oft wie starke Schilder in Battle-Symbols auftreten.
        self.defense_power = 50  # von 100     - beschreibt, wie wahrscheinlich jedes der Schilder ein Abblocken bewirkt.
        self.attack_dexterity = 40
        self.damage = 40
        self.standing_duration = random.randint(3000, 8000) # = wie lang er nur ganz am Anfang herumsteht.
        self.sight = 145
        self.random_stand_duration_range = [2500,5000]
        self.random_walkdistance_range_x = [-300,300]
        self.random_walkdistance_range_y = [-200,200]

        self.hitpoints = 300
        self.maxhealth = 300
        self.lifebar_pos_offset = [132,65]
        self.attacks = ["O", "U", "L", "R"]

        self.draw_TPP = 50 # länge pro bild
        self.fightwalk_TPP = 100 
        self.attackspeed = 3   # HINWEIS: die "TPP" der ganzen Kampfmoves werden anhand der jew. "speeds" dynamisch in fightpic_functions erschaffen. 
        self.defendspeed = 5
        fightpic_functions.calculate_fightpic_speeds(self)

        self.sturdiness = 2   # Widerstand gegen Knockback
        self.knockback = 7

        blaster.setup_ork_sounds(self)
        

        

        
        
    



        
