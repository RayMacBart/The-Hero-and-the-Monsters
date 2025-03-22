#import pygame_sdl2
#pygame_sdl2.import_as_pygame()
import pygame
import basic_types
import pool
from pool import Var
import math
import fightpic_functions
import fight
import blaster


## class Hero
## ... __init__(name, typ, pos, transparency=255, ID=0)
## ... handle_fightwalk_animation()
## ... reload_fightwalk_pics()
## ... focus()
## ... check_attention()


class Hero(basic_types.Character):
    def __init__(self, name, typ, pos, transparency=255, ID=0):
        basic_types.Character.__init__(self, name, typ, pos, transparency, ID)

        self.mask_mid = [144,111]
        self.walk_animation_delay = 4
        self.walk_animation_frame_countdown = self.walk_animation_delay

        self.hitpoints = 300
        self.maxhealth = 300
        self.lifebar = pygame.image.load(Var.path+"\\pics\\Hero_Lifebars\\Hero_Lifebar_36.png").convert()
        self.lifebar.set_colorkey([0,0,0], pygame.RLEACCEL)
        self.lifebar.set_alpha(200, pygame.RLEACCEL)
        self.speed = 5
        self.attackspeed = 5
        self.defendspeed = 5
        self.attack_dexterity = 40
        self.damage = 60
        self.sturdiness = 4 # Widerstand gegen Knockback
        self.knockback = 10
        self.sight = 105
        self.drawn = False
        self.draw_pressed = False
        self.drawing = False
        self.emergency_drawn = False
        self.putting_away = False
        self.LPT = 0  # last pictime (Universal!)
        self.draw_CPN = 0 # Current Pic Number
        self.draw_TPP = 50 # länge pro bild
        self.fightwalk_CPN = 0 # Current Pic Number
        self.fightwalk_TPP = 100 # länge pro bild
        self.attention = False
        fightpic_functions.calculate_fightpic_speeds(self)
        self.min_one_detected = False
        self.min_one_in_fightrange = False
        self.min_one_in_keep_fighting_range = False
        self.focussed_enemy = None
        self.last_focus_checktime = 0
        self.new_focus = False
        self.preflow = False
        self.flow = False
        self.attack_done = False
        self.attacks = ["O", "U", "L", "R"]
        self.attack_permission = False  # Permission = Erlaubnis (Timing)
        self.attack_pressed = False
        self.attack_typ = ""
        self.next_attack_typ = ""
        self.start_attack = False
        self.attacking = False
        self.slash_CPN = 0
        self.defense_pressed = False
        self.defense_typ = "" # wird auch für block verwendet
        self.ready_to_block = False
        self.start_defending = False
        self.defending = False
        self.start_release_defending = False
        self.release_defending = False
        self.defend_CPN = 0
        self.start_blocking = False
        self.blocking = False
        self.block_CPN = 0
        self.defblock_pressed = False
        self.start_defblocking = False
        self.defblocking = False
        self.defblock_CPN = 0
        self.hit_typ = "O"
        self.start_being_hitted = False
        self.being_hitted = False
        self.hit_CPN = 0
        self.start_dying = False
        self.dying = False
        self.die_CPN = 0
        self.defense_focus = None
        self.attack_focus = None
        self.stressed = False
        self.fightborder_masktypes = [] # used in check_fightfeel_and_distress @ fight

        self.align_typ = ""
        self.align_step = 0
        blaster.setup_hero_sounds(self)


                
    def handle_fightwalk_animation(self):
        if self.LPT + self.fightwalk_TPP < pygame.time.get_ticks():
            self.LPT = pygame.time.get_ticks()
            if not self.fightwalk_CPN == 7:
                self.fightwalk_CPN += 1
                try:
                    self.image = self.current_pics["Fight_"+str(self.fightwalk_CPN)]
                except KeyError:
                    self.image = pygame.image.load(Var.path+"\\pics\\"+self.name.split('_')[0]+'\\Fight\\'+self.name+"_"+self.dir+"_Fight_"+str(self.fightwalk_CPN)+".png").convert_alpha()
            else:
                try:
                    self.image = self.current_pics["Fight_7"]
                except KeyError:
                    self.image = pygame.image.load(Var.path+"\\pics\\"+self.name.split('_')[0]+'\\Fight\\'+self.name+"_"+self.dir+"_Fight_7.png").convert_alpha()
                self.fightwalk_CPN = 0

    def reload_fightwalk_pics(self):
        self.current_pics["Fight_1"] = pygame.image.load(Var.path+"\\pics\\"+self.name.split('_')[0]+'\\Fight\\'+self.name+"_"+self.dir+"_Fight_1.png").convert_alpha()
        self.current_pics["Fight_2"] = pygame.image.load(Var.path+"\\pics\\"+self.name.split('_')[0]+'\\Fight\\'+self.name+"_"+self.dir+"_Fight_2.png").convert_alpha()
        self.current_pics["Fight_3"] = pygame.image.load(Var.path+"\\pics\\"+self.name.split('_')[0]+'\\Fight\\'+self.name+"_"+self.dir+"_Fight_3.png").convert_alpha()
        self.current_pics["Fight_4"] = pygame.image.load(Var.path+"\\pics\\"+self.name.split('_')[0]+'\\Fight\\'+self.name+"_"+self.dir+"_Fight_4.png").convert_alpha()
        self.current_pics["Fight_5"] = pygame.image.load(Var.path+"\\pics\\"+self.name.split('_')[0]+'\\Fight\\'+self.name+"_"+self.dir+"_Fight_5.png").convert_alpha()
        self.current_pics["Fight_6"] = pygame.image.load(Var.path+"\\pics\\"+self.name.split('_')[0]+'\\Fight\\'+self.name+"_"+self.dir+"_Fight_6.png").convert_alpha()
        self.current_pics["Fight_7"] = pygame.image.load(Var.path+"\\pics\\"+self.name.split('_')[0]+'\\Fight\\'+self.name+"_"+self.dir+"_Fight_7.png").convert_alpha()
        
    def focus(self):
        if (pygame.time.get_ticks() > self.last_focus_checktime + 1000) or self.new_focus:
            self.last_focus_checktime = pygame.time.get_ticks()
            if self.new_focus:
                self.new_focus = False
            enemy_dir = [(self.focussed_enemy.realpos[0]-Var.ref_point[0]) - self.current_absolute_pos[0], (self.focussed_enemy.realpos[1]-Var.ref_point[1]) - self.current_absolute_pos[1]]
            if abs(enemy_dir[0])*3.7 <= enemy_dir[1]*(-1):
                if not self.dir == "N":
                    self.dir = "N"
                    self.reload_fightwalk_pics()
            elif enemy_dir[0]*3.7 > enemy_dir[1]*(-1) and enemy_dir[0] < (enemy_dir[1]*3.7)*(-1):
                if not self.dir == "NE":
                    self.dir = "NE"
                    self.reload_fightwalk_pics()
            elif abs(enemy_dir[1])*3.7 <= enemy_dir[0]:
                if not self.dir == "E":
                    self.dir = "E"
                    self.reload_fightwalk_pics()
            elif enemy_dir[0] < enemy_dir[1]*3.7 and enemy_dir[0]*3.7 > enemy_dir[1]:
                if not self.dir == "SE":
                    self.dir = "SE"
                    self.reload_fightwalk_pics()
            elif abs(enemy_dir[0])*3.7 <= enemy_dir[1]:
                if not self.dir == "S":
                    self.dir = "S"
                    self.reload_fightwalk_pics()
            elif (enemy_dir[0]*(-1))*3.7 > enemy_dir[1] and enemy_dir[1]*3.7 > enemy_dir[0]*(-1):
                if not self.dir == "SW":
                    self.dir = "SW"
                    self.reload_fightwalk_pics()
            elif abs(enemy_dir[1])*3.7 <= enemy_dir[0]*(-1):
                if not self.dir == "W":
                    self.dir = "W"
                    self.reload_fightwalk_pics()
            elif (enemy_dir[1]*(-1))*3.7 > enemy_dir[0]*(-1) and (enemy_dir[0]*(-1))*3.7 > enemy_dir[1]*(-1):
                if not self.dir == "NW":
                    self.dir = "NW"
                    self.reload_fightwalk_pics()
                    

    def check_attention(self):
        for u in Var.units.values():
            if u.typ == "Monster":                                  # AUFMERKSAMKEITSBEREICH (ZIEHEN)
                if int(math.sqrt((((abs(u.realpos[0]-self.realpos[0])//3)*2)**2)+(abs(u.realpos[1]-self.realpos[1])**2))) <= self.sight: # Satz des Pythagoras
                    self.min_one_detected = True
                    if not self.focussed_enemy:
                        self.focussed_enemy = u
        if self.min_one_detected:
            if not self.attention:
                self.attention = True
##                if not (self.drawn or self.drawing):
##                    self.draw_pressed = True
        else:
            if self.focussed_enemy:
                self.focussed_enemy = None
            if self.attention:
                self.attention = False
                if self.drawn or self.drawing:
                    self.draw_pressed = True
        self.min_one_detected = False
        
        for u in Var.units.values():
            if u.typ == "Monster":     # KAMPFBEREICH
                if not (u.dead or u.start_dying or u.dying):

                    distance = int(math.sqrt((((abs(u.realpos[0]-self.realpos[0])**2)//4)*3)+(abs(u.realpos[1]-self.realpos[1])**2)))
                    
                    if distance <= 74: # Satz des Pythagoras
                        self.min_one_in_fightrange = True
                        if not self.fighting:
                            #print("\n\n"+str(pygame.time.get_ticks())+":", "\n!!!!!!!!!!!!\nNEW FIGHT!!!\n!!!!!!!!!!!!\n")
                            Var.fight = fight.Fight(self, u)
                            if not self.min_one_in_keep_fighting_range:
                                self.min_one_in_keep_fighting_range = True
                        elif not u in Var.fight.enemies:
                            Var.fight.enemies.append(u)
                                                                          # ist mehr mit zusätzl. "keep_fighting_range",
                                                                          # damit beim alignen
                    elif distance <= 79:                                  # nicht versehentlich der fighting-
                        if not self.min_one_in_keep_fighting_range:       # status aufgehoben wird.
                            self.min_one_in_keep_fighting_range = True                                                                  
                            
                    elif distance <= 95:
                        if not (self.drawn or self.drawing) and not self.emergency_drawn:
                            self.emergency_drawn = True
                            self.draw_pressed = True
                    else:
                        self.emergency_drawn = False
                        
                    
                            
        if self.min_one_in_fightrange:
            if not self.fighting and self.drawn:
                self.fighting = True
                if self.go:
                    self.go = False
        elif not self.min_one_in_keep_fighting_range:                                                                                     
            if self.fighting:
                #print("\n"+str(pygame.time.get_ticks())+":", "Nobody in min_one_keep_fighting_range: hero.fighting set to False.")
                self.fighting = False                                                                                      
                Var.fight = None
            
        self.min_one_in_keep_fighting_range = False
        self.min_one_in_fightrange = False
                
