import pygame
import basic_types
import pool
import random
from pool import Var
import math


## class Enemy
## ... __init__(name, typ, pos, transparency=255, ID=0)
## ... handle_fightwalk_animation()
## ... advance()
## ... focus()
## ... random_walking()
## ... check_attention()
## ... behavior()


class Enemy(basic_types.Character):
    def __init__(self, name, typ, pos, transparency=255, ID=0):  #noch von hero übernommen
        basic_types.Character.__init__(self, name, typ, pos, transparency, ID) #noch von hero übernommen
        
        if name in ["Ork"]: # Hier kommen alle rein mit Bildgröße die NICHT 290x200 ist, wie eben z.B. Ork.
            self.maskpic = pygame.image.load(Var.path+'\\pics\\Monsters\\'+name+'\\Masks\\'+name+'_Mask.png').convert()
            self.maskpic.set_colorkey([0,0,0], pygame.RLEACCEL)
            self.mask = pygame.mask.from_surface(self.maskpic, 10)
            self.straight_maskpic = pygame.image.load(Var.path+'\\pics\\Monsters\\'+name+'\\Masks\\Straight_'+name+'_Mask.png').convert()
            self.straight_maskpic.set_colorkey([0,0,0], pygame.RLEACCEL)
            self.straight_mask = pygame.mask.from_surface(self.straight_maskpic, 10)
            self.x_maskpic = pygame.image.load(Var.path+'\\pics\\Monsters\\'+name+'\\Masks\\X-'+name+'_Mask.png').convert()
            self.x_maskpic.set_colorkey([0,0,0], pygame.RLEACCEL)
            self.x_mask = pygame.mask.from_surface(self.x_maskpic, 10)
            self.click_maskpic = pygame.image.load(Var.path+'\\pics\\Monsters\\'+name+'\\Masks\\'+name+'_Clickmask.png').convert()
            self.click_maskpic.set_colorkey([0,0,0], pygame.RLEACCEL)
            self.click_mask = pygame.mask.from_surface(self.click_maskpic, 10)
            self.marker = pygame.image.load(Var.path+'\\pics\\Monsters\\'+name+'\\Markers\\'+name+'_Marker.png').convert()
            self.marker.set_colorkey([0,0,0], pygame.RLEACCEL)
            self.defmarker = pygame.image.load(Var.path+'\\pics\\Monsters\\'+name+'\\Markers\\'+name+'_Defmarker.png').convert()
            self.defmarker.set_colorkey([0,0,0], pygame.RLEACCEL)
            self.attackmarker = pygame.image.load(Var.path+'\\pics\\Monsters\\'+name+'\\Markers\\'+name+'_Attackmarker.png').convert()
            self.attackmarker.set_colorkey([0,0,0], pygame.RLEACCEL)
            self.fight_feelmask_pic = pygame.image.load(Var.path+'\\pics\\Monsters\\'+name+'\\Masks\\'+name+'_Fightfeel_Mask.png').convert()
            self.fight_feelmask_pic.set_colorkey([0,0,0], pygame.RLEACCEL)
            self.fight_feelmask = pygame.mask.from_surface(self.fight_feelmask_pic, 10)
            self.bigmask_pic = pygame.image.load(Var.path+'\\pics\\Monsters\\'+name+'\\Masks\\'+name+'_Big_Mask.png').convert()
            self.bigmask_pic.set_colorkey([0,0,0], pygame.RLEACCEL)
            self.bigmask = pygame.mask.from_surface(self.bigmask_pic, 10)
            
        self.lifebar = pygame.image.load(Var.path+"\\pics\\Lifebars\\Lifebar_24.png").convert()
        self.lifebar.set_colorkey([0,0,0], pygame.RLEACCEL)
        self.lifebar.set_alpha(180, pygame.RLEACCEL)
        
        self.fighting = False
        self.attention = False
        self.start_standing = False
        self.stressed = False
        self.fightborder_masktypes = [] # used in check_fightfeel_and_distress @ fight
        self.standing_starttime = 0
        self.standing_duration = 0
        self.last_collision_time = 0
        self.behavior_choice = "Turn"
        self.last_heropos_checktime = 0
        self.last_focus_checktime = 0

        self.tactic = random.choice(["defensive", "offensive"])
        self.flow = False
        self.current_active_up_CBS = 0     # Current calculated/active Shield-Battle-Symbols (invisible)
        self.current_active_right_CBS = 0
        self.current_active_down_CBS = 0
        self.current_active_left_CBS = 0
        self.next_up_CBS = 0     # Next Shield-Battle-Symbols (drawn!)
        self.next_right_CBS = 0
        self.next_down_CBS = 0
        self.next_left_CBS = 0
        self.sword_up_BS = False   # drawn Flow-Chances
        self.sword_right_BS = False
        self.sword_down_BS = False
        self.sword_left_BS = False

        # HINWEIS: Die "TPP" (=Time Per Pic) der ganzen Kampfbewegungen werden anhand der jew. "speeds" DYNAMISCH in fightpic_functions erschaffen.
        self.LPT = 0  # last pictime (Universal!)
        self.draw_pressed = False  # kommt hier bei KI vor, weil hier noch nicht draw_pressed von start_drawing (gibts hier noch nicht) unterschieden wird.
        self.drawing = False
        self.putting_away = False
        self.drawn = False
        self.draw_CPN = 0 # Current Pic Number
        self.fightwalk_CPN = 0 # Current Pic Number
        self.attack_typ = ""
        self.start_attack = False
        self.attacking = False
        self.slash_CPN = 0
        self.defense_typ = "" # wird auch für block verwendet
        self.ready_to_block = False
        self.defense_calculated = False
        self.start_defending = False
        self.defending = False
        self.start_release_defending = False
        self.release_defending = False
        self.defend_CPN = 0
        self.start_blocking = False
        self.blocking = False
        self.block_CPN = 0
        self.start_defblocking = False
        self.defblocking = False
        self.defblock_CPN = 0
        self.hit_typ = ""
        self.start_being_hitted = False
        self.being_hitted = False
        self.hit_CPN = 0
        self.start_dying = False
        self.dying = False
        self.die_CPN = 0

        self.marker_alpha = 0
        self.marker_active = False
        self.defmarker_alpha = 0
        self.defmarker_active = False
        self.attackmarker_alpha = 0
        self.attackmarker_active = False
            

                
    def handle_fightwalk_animation(self):
        if self.LPT + self.fightwalk_TPP < pygame.time.get_ticks():
            self.LPT = pygame.time.get_ticks()
            if not self.fightwalk_CPN == 7:
                self.fightwalk_CPN += 1
                try:
                    self.image = self.current_pics["Fight_"+str(self.fightwalk_CPN)]
                except KeyError:
                    self.image = pygame.image.load(Var.path+"\\pics\\Monsters\\"+self.name.split('_')[0]+'\\Fight\\'+self.name+"_"+self.dir+"_Fight_"+str(self.fightwalk_CPN)+".png").convert_alpha()

            else:
                try:
                    self.image = self.current_pics["Fight_"+str(self.fightwalk_CPN)]
                except KeyError:
                    self.image = pygame.image.load(Var.path+"\\pics\\Monsters\\"+self.name.split('_')[0]+'\\Fight\\'+self.name+"_"+self.dir+"_Fight_"+str(self.fightwalk_CPN)+".png").convert_alpha()
                self.fightwalk_CPN = 0
                
    def advance(self):
        if pygame.time.get_ticks() > self.last_heropos_checktime + 300:
            self.go = True
            self.start_going = True
            self.sounds["footsteps_sound"].stop()  # wird in blaster wieder geplayed, ist hier um mehrfach Soundüberlagerungen zu verhindern
            self.absolute_destination = [Var.hero.realpos[0]-Var.ref_point[0], Var.hero.realpos[1]-Var.ref_point[1]]
            self.last_heropos_checktime = pygame.time.get_ticks()

    def focus(self):  # ohne reloader da eh schon mitten im Kampf (mit ständigen Fight-Reloadern)
        if pygame.time.get_ticks() > self.last_focus_checktime + 500:
            self.last_focus_checktime = pygame.time.get_ticks()
            enemy_dir = [(Var.hero.realpos[0]-Var.ref_point[0]) - self.current_absolute_pos[0], (Var.hero.realpos[1]-Var.ref_point[1]) - self.current_absolute_pos[1]]
            if abs(enemy_dir[0])*3.7 <= enemy_dir[1]*(-1):
                if not self.dir == "N":
                    self.dir = "N"
            elif enemy_dir[0]*3.7 > enemy_dir[1]*(-1) and enemy_dir[0] < (enemy_dir[1]*3.7)*(-1):
                if not self.dir == "NE":
                    self.dir = "NE"
            elif abs(enemy_dir[1])*3.7 <= enemy_dir[0]:
                if not self.dir == "E":
                    self.dir = "E"
            elif enemy_dir[0] < enemy_dir[1]*3.7 and enemy_dir[0]*3.7 > enemy_dir[1]:
                if not self.dir == "SE":
                    self.dir = "SE"
            elif abs(enemy_dir[0])*3.7 <= enemy_dir[1]:
                if not self.dir == "S":
                    self.dir = "S"
            elif (enemy_dir[0]*(-1))*3.7 > enemy_dir[1] and enemy_dir[1]*3.7 > enemy_dir[0]*(-1):
                if not self.dir == "SW":
                    self.dir = "SW"
            elif abs(enemy_dir[1])*3.7 <= enemy_dir[0]*(-1):
                if not self.dir == "W":
                    self.dir = "W"
            elif (enemy_dir[1]*(-1))*3.7 > enemy_dir[0]*(-1) and (enemy_dir[0]*(-1))*3.7 > enemy_dir[1]*(-1):
                if not self.dir == "NW":
                    self.dir = "NW"
    
    def random_walking(self):
            
        if pygame.time.get_ticks() > self.standing_starttime + self.standing_duration:
            
            if self.start_standing:
                self.start_standing = False
                self.standing_starttime = pygame.time.get_ticks()
                self.standing_duration = random.randint(self.random_stand_duration_range[0], self.random_stand_duration_range[1])
                
            self.behavior_choice = random.choice(["Move", "Turn"])
            if self.behavior_choice == "Move":
                self.go = True
                self.start_going = True
                self.sounds["footsteps_sound"].stop()  # wird in blaster wieder geplayed, ist hier um mehrfach Soundüberlagerungen zu verhindern
                self.absolute_destination = [(self.realpos[0]+random.randint(self.random_walkdistance_range_x[0],self.random_walkdistance_range_x[1]))-Var.ref_point[0],\
                                                 (self.realpos[1]+random.randint(self.random_walkdistance_range_y[0],self.random_walkdistance_range_y[1]))-Var.ref_point[1]]
            elif self.behavior_choice == "Turn":
                self.standing_starttime = pygame.time.get_ticks()
                self.standing_duration = random.randint(self.random_stand_duration_range[0], self.random_stand_duration_range[1])
                turndir = random.choice(["left","right"])
                if turndir == "left":
                    if self.dir == "N":
                        self.dir = "NW"
                    elif self.dir == "NE":
                        self.dir = "N"
                    elif self.dir == "E":
                        self.dir = "NE"
                    elif self.dir == "SE":
                        self.dir = "E"
                    elif self.dir == "S":
                        self.dir = "SE"
                    elif self.dir == "SW":
                        self.dir = "S"
                    elif self.dir == "W":
                        self.dir = "SW"
                    elif self.dir == "NW":
                        self.dir = "W"
                elif turndir == "right":
                    if self.dir == "N":
                        self.dir = "NE"
                    elif self.dir == "NE":
                        self.dir = "E"
                    elif self.dir == "E":
                        self.dir = "SE"
                    elif self.dir == "SE":
                        self.dir = "S"
                    elif self.dir == "S":
                        self.dir = "SW"
                    elif self.dir == "SW":
                        self.dir = "W"
                    elif self.dir == "W":
                        self.dir = "NW"
                    elif self.dir == "NW":
                        self.dir = "N"
                self.image = pygame.image.load(Var.path+"\\pics\\Monsters\\"+self.name.split('_')[0]+'\\'+self.name+"_"+self.dir+"_Stand.png").convert_alpha()
    
    def check_attention(self):
        if int(math.sqrt((((abs(Var.hero.realpos[0]-self.realpos[0])//3)*2)**2)+(abs(Var.hero.realpos[1]-self.realpos[1])**2))) <= self.sight: #Satz des Pythagoras
            if not (self.attention or self.putting_away or self.drawing):
                self.attention = True
                if pygame.time.get_ticks() > self.last_sound_played + 150:
                    self.sounds["attention_sound"].play()
                    self.last_sound_played = pygame.time.get_ticks()
                if not (self.drawn or self.drawing):
                    self.draw_pressed = True
        elif self.attention and self.drawn:
            self.attention = False
            self.draw_pressed = True
        elif self.drawn and (int(math.sqrt((((abs(Var.hero.realpos[0]-self.realpos[0])//3)*2)**2)+(abs(Var.hero.realpos[1]-self.realpos[1])**2)))-15 > self.sight):
            self.draw_pressed = True

    def behavior(self):
        if not (self.fighting or self.drawing or self.putting_away or self.drawn or self.attention or self.go):
            self.random_walking()
        if not self.fighting:
            self.check_attention()
            if self.attention:
                self.advance()

        distance = int(math.sqrt((((abs(Var.hero.realpos[0]-self.realpos[0])**2)//4)*3)+(abs(Var.hero.realpos[1]-self.realpos[1])**2)))
        
        if distance <= 74: #Satz des Pythagoras
            if Var.hero.drawn and not self.fighting:
                if self.go:
                    self.go = False
                self.fighting = True
                
        elif distance > 90:     # ist mehr, damit beim alignen nicht versehentlich der fighting-Status aufgehoben wird.
            if self.fighting:
                self.fighting = False
                #print(str(pygame.time.get_ticks())+":", "enemy", self.ID, "unfought by out of range!")
            
                
        if self.fighting:
            self.focus()


    

    
