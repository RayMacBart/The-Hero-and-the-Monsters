import pygame
import pool
from pool import Var
import other_functions
import random
import math


## class Fight
## ... __init__(hero, enemy)
## ... check_action_time()
## ... battlestart()
## ... switch_enemy()
## ... choose_enemies_defense()
## ... handle_hero_attack()
## ... handle_hero_defense()
## ... choose_next_battle_symbols()
## ... choose_weak_shields_false_behavior()
## ... calculate_enemys_defense()
## ... check_enemys_flow()
## ... check_flow_symbols()
## ... clear_and_reset_by_turn()
## ... handle_turns()
## ... handle_hero_permission()
## ... calculate_heros_hp_loss()
## ... check_enemies_attack_consequences()
## ... calculate_enemys_hp_loss()
## ... handle_the_battle()
## ... automatic_align_opponents()
## ... handle_knockback()
## ... check_fightfeel_and_distress(unit)


class Fight(object):     # Wird in self.heros Funktion "check_attention" erschaffen.
    def __init__(self, hero, enemy):
        self.hero = hero
        
        self.enemies = []
        self.enemy = enemy
        self.CAE = 1  # Current Active Enemy
        self.next_target = None
        self.enemies.append(self.enemy)
        self.start_time = pygame.time.get_ticks()
        self.LAT = 0 # Last Action Time
        self.align_LPT = 0
        self.align_TPP = 70
        self.start_knockback = False
        self.knockback_done = True
        self.knockbacking = False
        self.knockback_TPP = 12
        self.knockback_LPT = 0
        self.knockback_CPN = 0
        self.knockback_dir = ""
        self.knockback_typ = ""
        self.knockback_power = 0
        self.last_feelcheck = 0
        self.kb_beater = None
        self.kb_victim = None
        self.check_action_time()
        self.current_turn = ""
        self.CTACD = False  # Current Turn Attack Command Done
        self.enemy_attack_consequence_happened = False
        self.hero.first_attack = False
        self.enemy_flowing = False
        self.pass_die_check = True
        self.hero.defense_typ = ""
        self.hero.attack_typ = ""
        self.enemy.defense_typ = ""
        self.enemy.attack_typ = ""
        
        if enemy.tactic == "offensive":
            self.starting = False # betrifft die Zeit, bis irgendjemand zuschlägt.
            enemy.start_attack = True
            self.current_turn = "enemy"
            self.LAT = pygame.time.get_ticks()
        elif enemy.tactic == "defensive":
            self.starting = True # betrifft die Zeit, bis irgendjemand zuschlägt.
            hero.attack_permission = True

        self.choose_next_battle_symbols()

        self.W_pressed = False
        self.A_pressed = False
        self.S_pressed = False
        self.D_pressed = False

        self.sounds = {}
        self.last_sound_played = 0
        self.sounds["tsching_L_sound"] = pygame.mixer.Sound(Var.path+"\\sound\\tsching_L.wav")   # diese tsching-Sounds sind geschickter bei Der Fight-Klasse aufgehoben
        self.sounds["tsching_L_sound"].set_volume(0.9)
        self.sounds["tsching_R_sound"] = pygame.mixer.Sound(Var.path+"\\sound\\tsching_R.wav")
        self.sounds["tsching_R_sound"].set_volume(0.9)
        self.sounds["tsching_O_sound"] = pygame.mixer.Sound(Var.path+"\\sound\\tsching_O.wav")
        self.sounds["tsching_O_sound"].set_volume(0.9)
        self.sounds["tsching_U_sound"] = pygame.mixer.Sound(Var.path+"\\sound\\tsching_U.wav")
        self.sounds["tsching_U_sound"].set_volume(1.0)

        
    def check_action_time(self):
        atc = [] # "Action Time Candidates"
        atc.append(self.hero.slash_TPP*12)
        atc.append(self.hero.defend_TPP*(8+3))  # Hier sind die Defense und Block TPPs noch vereinheitlicht zusammengelegt
        for e in self.enemies:
            atc.append(e.slash_TPP*12)
            atc.append(e.defend_TPP*(8+3)) # Ist hier noch zu verändern/erweitern bei Separierung von Block bzw. Hit.
        self.action_time = max(atc) + 10 # Quasi Buffer


    def battlestart(self):
        if not self.hero.attack_pressed and not (self.hero.start_attack or self.hero.attacking):
            if self.start_time + 1500 < pygame.time.get_ticks(): # Wartezeit des Enemys wäre allerdings 
                self.enemy.start_attack = True                   # auch noch als variierendes Monster-Attribut festlegbar.
                self.current_turn = "enemy"
                self.hero.attack_permission = False
                self.LAT = pygame.time.get_ticks()
                self.starting = False
        else:
            #print("Hero Attacks first!")
            self.current_turn = "hero"
            self.handle_hero_attack()
            self.hero.start_attack = True
            self.LAT = pygame.time.get_ticks()
            self.starting = False
            self.hero.first_attack = True
            self.hero.attack_pressed = False



    def switch_enemy(self):  # hier gleichberechtigtes Zufallsprinzip einbauen (nicht nur abwechselnd = unberechenbarer!)
        if self.CAE >= len(self.enemies):
            self.CAE = 1
        else:
            self.CAE += 1
        #print(str(pygame.time.get_ticks())+":", "enemy switched!")
        self.enemy = self.enemies[self.CAE-1]
        self.hero.focussed_enemy = self.enemy
        


    def handle_hero_attack(self):
        if not self.starting:
            if self.W_pressed:
                self.hero.next_attack_typ = "O"
            elif self.A_pressed:
                self.hero.next_attack_typ = "L"
            elif self.S_pressed:
                self.hero.next_attack_typ = "U"
            elif self.D_pressed:
                self.hero.next_attack_typ = "R"
            self.hero.attack_permission = False   ### vvv
            self.CTACD = True  # nur bei Attack, weil Verteidigen darf man immer (vorerst beschlossen...)
        else:
            if self.W_pressed:
                self.hero.attack_typ = "O"
            elif self.A_pressed:
                self.hero.attack_typ = "L"
            elif self.S_pressed:
                self.hero.attack_typ = "U"
            elif self.D_pressed:
                self.hero.attack_typ = "R"

        #self.W_pressed = False; self.A_pressed = False; self.S_pressed = False; self.D_pressed = False
        
        if len(self.enemies) > 1:
            for e in self.enemies:
                if (e.ID == self.hero.attack_focus):
                    self.next_target = e
                    e.attackmarker_alpha = 80
                    e.marker_alpha = 0
        elif self.hero.attack_focus == self.enemy.ID:
            self.enemy.attackmarker_alpha = 80
            self.enemy.marker_alpha = 0

        #print(str(pygame.time.get_ticks())+":", "Hero's Attack Intention Activation. Typ:", self.hero.next_attack_typ, "CTACD="+str(self.CTACD))
            


    def handle_hero_defense(self):
        if self.W_pressed:
            self.hero.defense_typ = "O"
        elif self.A_pressed:
            self.hero.defense_typ = "L"
        elif self.D_pressed:
            self.hero.defense_typ = "R"
        self.hero.start_defending = True # Nur bei Defense, weil bei Attack erst mit Anfang des nächsten Turns
        if self.hero.defense_focus == self.enemy.ID:
            self.enemy.defmarker_alpha = 80
            self.enemy.marker_alpha = 0



    def choose_next_battle_symbols(self):
        for e in self.enemies:
            e.current_active_up_CBS = e.next_up_CBS;  e.current_active_right_CBS = e.next_right_CBS  # turn-switch of Shield-Symbols
            e.current_active_down_CBS = e.next_down_CBS;  e.current_active_left_CBS = e.next_left_CBS
            e.next_up_CBS = 0; e.next_right_CBS = 0; e.next_down_CBS = 0; e.next_left_CBS = 0   # Next Shield-Battle-Symbols
            DC = (e.defense_dexterity/2.5)+10    # DC = chance of every single defense-symbol
            result = None
            progress = 0
            while not progress == 12:
                progress += 1
                result = True if ((random.randint(1,100) - DC) < 0) else False
                if result:
                    if (progress in [1,5,9]) and not e.next_up_CBS:
                        if progress == 1:
                            e.next_up_CBS = 3
                        elif progress == 5:
                            e.next_up_CBS = 2
                        elif progress == 9:
                            e.next_up_CBS = 1
                    elif (progress in [2,6,10]) and not e.next_right_CBS:
                        if progress == 2:
                            e.next_right_CBS = 3
                        elif progress == 6:
                            e.next_right_CBS = 2
                        elif progress == 10:
                            e.next_right_CBS = 1
                    elif (progress in [3,7,11]) and not e.next_down_CBS:
                        if progress == 3:
                            e.next_down_CBS = 3
                        elif progress == 7:
                            e.next_down_CBS = 2
                        elif progress == 11:
                            e.next_down_CBS = 1
                    elif (progress in [4,8,12]) and not e.next_left_CBS:
                        if progress == 4:
                            e.next_left_CBS = 3
                        elif progress == 8:
                            e.next_left_CBS = 2
                        elif progress == 12:
                            e.next_left_CBS = 1



    def choose_weak_shields_false_behavior(self):  # nix tun oder falsch verteidigen?  ... wird von calculate_enemys_defense() aufgerufen
        badmove_chance = 0
        if self.hero.attack_typ == "O":
            badmove_chance = self.enemy.current_active_up_CBS*33
        elif self.hero.attack_typ == "R":
            badmove_chance = self.enemy.current_active_right_CBS*33
        elif self.hero.attack_typ == "U":
            badmove_chance = self.enemy.current_active_down_CBS*33
        elif self.hero.attack_typ == "L":
            badmove_chance = self.enemy.current_active_left_CBS*33
        i = random.randint(1,100)
        if i <= badmove_chance:  #  "badmove_chance", dass Enemy FALSCH verteidigt und Rest, dass er nix tut.
            if self.hero.attack_typ == "O":
                self.enemy.defense_typ = random.choice(["R","L","U"])
            elif self.hero.attack_typ == "U":
                self.enemy.defense_typ = random.choice(["R","L","O"])
            elif self.hero.attack_typ == "L":
                self.enemy.defense_typ = random.choice(["U","L","O"])  # L ist gleich, weil blickwinkel-verdreht!
            elif self.hero.attack_typ == "R":
                self.enemy.defense_typ = random.choice(["R","U","O"])  # R ist gleich, weil blickwinkel-verdreht!
            if not self.enemy.defense_typ == "U":
                self.enemy.start_defending = True
            else:
                self.enemy.start_defblocking = True
            #print(str(pygame.time.get_ticks())+":", "enemy blocks wrong:", self.enemy.defense_typ)
            
            
    def calculate_enemys_defense(self):
        self.enemy.defense_calculated = True
        
        if ((self.hero.attack_typ == "O") and self.enemy.current_active_up_CBS) or ((self.hero.attack_typ == "R") and self.enemy.current_active_right_CBS) or \
           ((self.hero.attack_typ == "U") and self.enemy.current_active_down_CBS) or ((self.hero.attack_typ == "L") and self.enemy.current_active_left_CBS):
            # (Wenn wohin geschlagen wird, wo irgendein Shield-Symbol war...)
            defchance = 0
            if (self.hero.attack_typ == "O"):
                if self.enemy.current_active_up_CBS == 1:
                    defchance = 10+(self.enemy.defense_power*0.4)
                elif self.enemy.current_active_up_CBS == 2:
                    defchance = 50+(self.enemy.defense_power*0.3)
                elif self.enemy.current_active_up_CBS == 3:
                    defchance = 80+(self.enemy.defense_power*0.2)
            elif (self.hero.attack_typ == "R"):
                if self.enemy.current_active_right_CBS == 1:
                    defchance = 10+(self.enemy.defense_power*0.4)
                elif self.enemy.current_active_right_CBS == 2:
                    defchance = 50+(self.enemy.defense_power*0.3)
                elif self.enemy.current_active_right_CBS == 3:
                    defchance = 80+(self.enemy.defense_power*0.2)
            elif (self.hero.attack_typ == "U"):
                if self.enemy.current_active_down_CBS == 1:
                    defchance = 10+(self.enemy.defense_power*0.4)
                elif self.enemy.current_active_down_CBS == 2:
                    defchance = 50+(self.enemy.defense_power*0.3)
                elif self.enemy.current_active_down_CBS == 3:
                    defchance = 80+(self.enemy.defense_power*0.2)
            elif (self.hero.attack_typ == "L"):
                if self.enemy.current_active_left_CBS == 1:
                    defchance = 10+(self.enemy.defense_power*0.4)
                elif self.enemy.current_active_left_CBS == 2:
                    defchance = 50+(self.enemy.defense_power*0.3)
                elif self.enemy.current_active_left_CBS == 3:
                    defchance = 80+(self.enemy.defense_power*0.2)

            i = random.randint(1,100)
            if defchance - i >= 0:  # Verteidigung wirkt - richtiges Blocken erfolgt!
                if self.hero.attack_typ in ["O", "U"]:
                    self.enemy.defense_typ = self.hero.attack_typ
                elif self.hero.attack_typ == "R":
                    self.enemy.defense_typ = "L"
                elif self.hero.attack_typ == "L":
                    self.enemy.defense_typ = "R"
                if not self.enemy.defense_typ == "U":
                    self.enemy.start_defending = True
                else:
                    self.enemy.start_defblocking = True
                #print(str(pygame.time.get_ticks())+":", "enemy blocks", self.enemy.defense_typ)
            else:  # Verteidigung greift NICHT.
                self.choose_weak_shields_false_behavior()
                    
        else: # Wenn Enemy sicher nicht verteidigt (auch sicher kein falscher Def-move)
            pass
            
                
            

    def check_enemys_flow(self):
        AC = self.enemy.attack_dexterity*0.7   # Attack-Chance (Flow-Chance)
        result = True if ((random.randint(1,100) - AC) < 0) else False
        self.enemy.flow = True if result else False



    def check_flow_symbols(self):
        self.enemy.sword_up_BS = False; self.enemy.sword_right_BS = False; self.enemy.sword_down_BS = False; self.enemy.sword_left_BS = False
        AC = self.hero.attack_dexterity*0.3   # Attack-Chance (Flow-Chance) of every single direction!
        result = None
        progress = 0
        while not progress == 4:
            progress += 1
            result = True if ((random.randint(1,100) - AC) < 0) else False
            if result:
                if progress == 1:
                    self.enemy.sword_up_BS = True
                elif progress == 2:
                    self.enemy.sword_right_BS = True
                elif progress == 3:
                    self.enemy.sword_down_BS = True
                elif progress == 4:
                    self.enemy.sword_left_BS = True

                    

    def clear_and_reset_by_turn(self):
        self.check_action_time()
        self.LAT = pygame.time.get_ticks()
        self.enemy.defense_calculated = False
        self.enemy_attack_consequence_happened = False
        self.hero.attack_done = False
        self.hero.start_defending = False
        self.hero.start_release_defending = False
        self.hero.start_attack = False
        self.hero.attacking = False; self.hero.attack_CPN = 0
        self.hero.start_being_hitted = False
        self.hero.start_blocking = False
        self.hero.blocking=False; self.hero.block_CPN = 0
        self.hero.start_defblocking = False
        self.hero.defblocking=False; self.hero.defblock_CPN = 0

        #NEU:
        self.hero.ready_to_block = False
        self.hero.defending = False
        self.hero.release_defending = False
        self.hero.defend_CPN = 0
        self.hero.image = pygame.image.load(Var.path+"\\pics\\Hero\\Fight\\Hero_"+self.hero.dir+"_Fight_1.png").convert_alpha()
        self.hero.being_hitted=False
        self.hero.hit_CPN = 0
        
##        #ALT:
##        if self.hero.defending or self.hero.release_defending:
##            self.hero.ready_to_block = False
##        if self.hero.being_hitted:
##            self.hero.release_defending=False; self.hero.defending=False
##        if self.hero.defending:
##            self.hero.release_defending=False; self.hero.being_hitted=False; self.hero.hit_CPN = 0
##        elif self.hero.release_defending:
##            self.hero.defending=False; self.hero.being_hitted=False; self.hero.hit_CPN = 0
##
##        if not (self.hero.defending or self.hero.release_defending or self.hero.ready_to_block or self.hero.being_hitted):
##            self.hero.image = pygame.image.load(Var.path+"\\pics\\Hero\\Fight\\Hero_"+self.hero.dir+"_Fight_1.png").convert_alpha()

            


    def handle_turns(self):
        
        if self.current_turn == "hero":
            if ((pygame.time.get_ticks() > self.LAT + self.action_time) and not \
               (self.hero.attacking or self.enemy.release_defending or self.enemy.blocking or self.enemy.defblocking or self.enemy.being_hitted \
               or self.enemy.attacking)) or (self.hero.first_attack and (pygame.time.get_ticks() > self.LAT + self.action_time)):
                #print("\n"+str(pygame.time.get_ticks())+":", "TURN")
                if self.hero.first_attack:
                    self.hero.first_attack = False
                self.clear_and_reset_by_turn()
                if not (self.hero.flow and self.CTACD):

                    self.current_turn = "enemy"

                    if len(self.enemies) > 1:
                        self.switch_enemy()
                    elif (len(self.enemies) == 1) and not (self.enemies[0].ID == self.enemy.ID):
                        #print(str(pygame.time.get_ticks())+":", "1 enemy but other ID that had to be changed!")
                        self.enemy = self.enemies[0]

                    #print("------------------------------\n"+str(pygame.time.get_ticks())+":", "New Turn:  Enemy", self.CAE)
                    
                    self.hero.focussed_enemy = self.enemy
                    self.enemy.attack_typ = random.choice(self.enemy.attacks)
                    self.enemy.start_attack = True
                    #print(str(pygame.time.get_ticks())+":", "enemy attacks", self.enemy.attack_typ)
                    self.CTACD = False
                    self.hero.defense_focus = None
                    self.hero.attack_focus = None
                    self.hero.flow = False
                    self.hero.preflow = False
                    self.check_enemys_flow()
                    if not self.enemy.flow:
                        self.check_flow_symbols()
                        self.choose_next_battle_symbols()
                    #else:
                        #print(str(pygame.time.get_ticks())+":", "enemy flow activated")

                    self.enemy_flowing = False
                    for e in self.enemies:
                        if e.flow:
                            self.enemy_flowing = True
                            
                else:
                    self.pass_die_check = True
                    if self.enemy.dead or self.enemy.dying or (self.enemy.hitpoints <= 0):
                        self.pass_die_check = False
                        self.LAT -= (self.action_time//3)*2
                        self.switch_enemy()
                        #print(str(pygame.time.get_ticks())+":", "Attack_focus on dying Enemy! Turn skipped!")
                        self.hero.attack_focus = self.enemy.ID
                        #self.CTACD = False
                        #self.hero.flow = False
                        
                    if self.pass_die_check:
                        #print("-------------------------------------\n"+str(pygame.time.get_ticks())+":", "Flow Turn:  Hero")
                        if not self.hero.slash_CPN == 0:
                            self.hero.slash_CPN = 0
                            print(str(pygame.time.get_ticks())+":", "Hero Slash_CPN manual set to 0!")
                        self.hero.flow = False
                        self.check_flow_symbols()
                        self.choose_next_battle_symbols()
                        self.CTACD = False
                        self.hero.defense_focus = None # - attack_focus bleibt!
                        if self.next_target:
                            self.enemy = self.next_target
                            self.hero.focussed_enemy = self.next_target
                        self.next_target = None
                        self.hero.attack_typ = self.hero.next_attack_typ
                        self.hero.next_attack_typ = ""
                        self.hero.start_attack = True
                        #print(str(pygame.time.get_ticks())+":", "Hero Attacks", self.hero.attack_typ, "@", str(self.hero.attack_focus)+"=attack_focus")
                        self.enemy.defend_CPN = 0
                        
                        if self.hero.preflow:
                            self.hero.flow = True
                            self.hero.preflow = False
                            #print(str(pygame.time.get_ticks())+":", "Hero.FLOW = True")


                #print(str(pygame.time.get_ticks())+":", "enemies:", len(self.enemies), "CAE:", self.CAE, "current_enemy_ID:", self.enemy.ID)
                
                    
        elif (self.current_turn == "enemy"):
            if (pygame.time.get_ticks() > (self.LAT + self.action_time + 500)) and not \
               (self.hero.attacking or self.enemy.release_defending or self.enemy.blocking or self.enemy.defblocking or self.enemy.being_hitted \
               or self.enemy.attacking):
                #print("\n"+str(pygame.time.get_ticks())+":", "TURN")
                self.clear_and_reset_by_turn()
                if self.CTACD and not self.enemy.flow:
                    #print("-------------------------------------\n"+str(pygame.time.get_ticks())+":", "New Turn:  Hero")
                    self.current_turn = "hero"
                    if not self.hero.slash_CPN == 0:
                        self.hero.slash_CPN = 0
                        print(str(pygame.time.get_ticks())+":", "Hero Slash_CPN manual set to 0!")
                    self.check_flow_symbols()
                    self.choose_next_battle_symbols()
                    self.CTACD = False
                    self.hero.defense_focus = None # - attack_focus bleibt!
                    if self.next_target:
                        self.enemy = self.next_target
                        self.hero.focussed_enemy = self.next_target
##                        self.new_focus = True
##                        self.hero.focus()
                    self.next_target = None
                    self.hero.attack_typ = self.hero.next_attack_typ
                    self.hero.next_attack_typ = ""
                    self.hero.start_attack = True
                    #print(str(pygame.time.get_ticks())+":", "Hero Attacks", self.hero.attack_typ, "@", str(self.hero.attack_focus)+"=attack_focus")
                    self.enemy.defend_CPN = 0

                    if self.hero.preflow:
                        self.hero.flow = True
                        self.hero.preflow = False
                        #print(str(pygame.time.get_ticks())+":", "Hero.FLOW = True")
                else:
                    if not self.enemy.flow:
                        if len(self.enemies) > 1:
                            self.switch_enemy()
                            #print("-------------------------------------\n"+str(pygame.time.get_ticks())+":", "Other Enemy NON-flow Turn:  Enemy", self.CAE)
                        #else:
                            #print("-------------------------------------\n"+str(pygame.time.get_ticks())+":", "Same Enemy NON-flow Turn (single).")
                    #else:
                        #print("-------------------------------------\n"+str(pygame.time.get_ticks())+":", "Flow Turn:  Enemy", self.CAE)
                    self.enemy.attack_typ = random.choice(self.enemy.attacks)
                    self.enemy.start_attack = True
                    #print(str(pygame.time.get_ticks())+":", "enemy attacks", self.enemy.attack_typ)
                    self.hero.defense_focus = None
                    self.hero.attack_focus = None
                    self.check_enemys_flow()
                    if not self.enemy.flow:
                        self.check_flow_symbols()
                        self.choose_next_battle_symbols()
                    #else:
                        #print(str(pygame.time.get_ticks())+":", "enemy flow activated")
                    self.CTACD = False


                    self.enemy_flowing = False
                    for e in self.enemies:
                        if e.flow:
                            self.enemy_flowing = True
        
                #print(str(pygame.time.get_ticks())+":", "enemies:", len(self.enemies), "CAE:", self.CAE, "current_enemy_ID:", self.enemy.ID)






        
    def handle_hero_permission(self):    # ...and hero flow-"controller"
        if self.hero.attack_pressed:
            if self.current_turn == "hero":
                if self.hero.flow:
                    self.hero.attack_permission = True
                    #print(str(pygame.time.get_ticks())+":", "Hero Attack Permission due to Flow")
                    for e in self.enemies:
                        if e == self.hero.focussed_enemy:
                            if (self.W_pressed and e.sword_up_BS) or (self.D_pressed and e.sword_right_BS) or \
                               (self.S_pressed and e.sword_down_BS) or (self.A_pressed and e.sword_left_BS):
                                self.hero.preflow = True
                                #print(str(pygame.time.get_ticks())+":", "Hero preflow activated (click on sword) AGAIN")
                else:
                    self.hero.attack_permission = False
                    #print(str(pygame.time.get_ticks())+":", "NO Attack Permission for Hero during Hero-Turn!")
                
            elif self.current_turn == "enemy":
                if not self.CTACD:   # and (pygame.time.get_ticks() > self.LAT + (((self.action_time+500)//3)*2)):
                    self.hero.attack_permission = True
                    #print(str(pygame.time.get_ticks())+":", "Hero Attack Permission while Enemy-Turn!")
                    for e in self.enemies:
                        if e == self.hero.focussed_enemy:
                            if (self.W_pressed and e.sword_up_BS) or (self.D_pressed and e.sword_right_BS) or \
                               (self.S_pressed and e.sword_down_BS) or (self.A_pressed and e.sword_left_BS):
                                self.hero.preflow = True
                                #print(str(pygame.time.get_ticks())+":", "Hero preflow activated (click on sword)")

##                elif not (pygame.time.get_ticks() > self.LAT + (((self.action_time+500)//3)*2)):
##                    print("No Hero Attack permission due to OUT OF TIME!")
                    
##                    print("True:\nTime:", pygame.time.get_ticks(), "\nLAT:", self.LAT, "\naction_time:", self.action_time,\
##                          "\nSLASH_TPP*12:", self.hero.slash_TPP*12, "current turn:", self.current_turn, "\n.....")
##                else:
##                    print("False:\nTime:", pygame.time.get_ticks(), "\nLAT:", self.LAT, "\naction_time:", self.action_time,\
##                          "\nSLASH_TPP*12:", self.hero.slash_TPP*12, "current turn:", self.current_turn, "\nCTACD:", self.CTACD, "\n.....")



    def calculate_heros_hp_loss(self):
        self.hero.hitpoints -= self.enemy.damage
        Var.start_redframe = True
        #print(str(pygame.time.get_ticks())+":", "hero takes damage")

        

    def check_enemies_attack_consequences(self):
        self.enemy_attack_consequence_happened = True
        if ((self.hero.ready_to_block) and (self.hero.defense_focus == self.enemy.ID)) and \
           (((self.hero.defense_typ  == "O") and (self.enemy.attack_typ == "O")) or \
           ((self.hero.defense_typ  == "L") and (self.enemy.attack_typ == "R")) or \
            ((self.hero.defense_typ  == "R") and (self.enemy.attack_typ == "L"))): 
            self.hero.start_blocking = True
            self.start_knockback = True; self.kb_victim = self.hero; self.kb_beater = self.enemy; self.knockback_typ = "Block"
            if pygame.time.get_ticks() > self.last_sound_played + 150:
                self.sounds["tsching_"+self.hero.defense_typ+"_sound"].play()
                self.last_sound_played = pygame.time.get_ticks()
                #print(str(pygame.time.get_ticks())+":", "Hero blocks", self.hero.defense_typ)
        elif ((self.hero.defense_typ  == "U") and (self.enemy.attack_typ == "U")) and \
             (self.hero.defblock_CPN in [4,5,6,7]) and (self.hero.defense_focus == self.enemy.ID):
            self.start_knockback = True; self.kb_victim = self.hero; self.kb_beater = self.enemy; self.knockback_typ = "Block"
            if pygame.time.get_ticks() > self.last_sound_played + 150:
                self.sounds["tsching_U_sound"].play()   # Nur das ergibt Verhinderung des Hits
                self.last_sound_played = pygame.time.get_ticks()
                #print(str(pygame.time.get_ticks())+":", "Hero blocks U")
        elif not (self.hero.start_being_hitted or self.hero.being_hitted):
            if self.enemy.attack_typ in ["O", "U"]:
                self.hero.hit_typ = self.enemy.attack_typ
            elif self.enemy.attack_typ == "L":
                self.hero.hit_typ = "R"
            elif self.enemy.attack_typ == "R":
                self.hero.hit_typ = "L"
            self.hero.start_being_hitted = True
            self.start_knockback = True; self.kb_victim = self.hero; self.kb_beater = self.enemy; self.knockback_typ = "Hit"

            self.calculate_heros_hp_loss()
            
            if not self.hero.hitpoints <= 0:
                self.hero.lifebar = pygame.image.load(Var.path+"\\pics\\Hero_Lifebars\\Hero_Lifebar_"+\
                                               str(int(round(((self.hero.hitpoints/self.hero.maxhealth)*36), 0)))+".png").convert()
                self.hero.lifebar.set_colorkey([0,0,0], pygame.RLEACCEL)
                self.hero.lifebar.set_alpha(180, pygame.RLEACCEL)
            else:
                self.hero.lifebar = pygame.image.load(Var.path+"\\pics\\Hero_Lifebars\\Hero_Lifebar_0.png").convert()
                self.hero.lifebar.set_colorkey([0,0,0], pygame.RLEACCEL)
                self.hero.lifebar.set_alpha(200, pygame.RLEACCEL)



    def calculate_enemys_hp_loss(self):
        self.enemy.hitpoints -= self.hero.damage
        #print(str(pygame.time.get_ticks())+":", "Enemy", self.enemy.ID, "takes damage")
















#####################################################################################################################################
    def handle_the_battle(self):
        if self.starting:
            self.battlestart()
        else:
            if self.hero.defense_pressed:
                if not (self.W_pressed or self.A_pressed or self.D_pressed):
                    self.hero.start_release_defending = True
                    self.hero.defense_pressed = False
                elif not (self.hero.attacking or self.hero.start_attack or self.hero.defending or self.hero.start_defending or \
                          self.hero.blocking or self.hero.start_blocking or self.hero.being_hitted or self.hero.start_being_hitted or \
                          self.hero.defblocking or self.hero.start_defblocking or self.hero.start_release_defending or \
                          self.hero.release_defending or self.hero.ready_to_block):
                    self.handle_hero_defense()
            elif self.hero.defblock_pressed:  # hier ist ein separater "Defblock-Handler"
                self.hero.defense_typ = "U"
                if not (self.hero.attacking or self.hero.start_attack or self.hero.defending or self.hero.start_defending or \
                        self.hero.blocking or self.hero.start_blocking or self.hero.being_hitted or self.hero.start_being_hitted or \
                        self.hero.defblocking or self.hero.start_defblocking or self.hero.start_release_defending or \
                        self.hero.release_defending or self.hero.ready_to_block):
                    self.hero.start_defblocking = True
                self.hero.defblock_pressed = False
                if self.hero.defense_focus == self.enemy.ID:
                    self.enemy.defmarker_alpha = 60
                    self.enemy.marker_alpha = 0


##            if not self.hero.first_attack:
##                self.handle_hero_permission()
##                if self.hero.attack_permission:
##                    self.handle_hero_attack()
##                    
##            if self.hero.attack_pressed:
##                self.hero.attack_pressed = False

            self.handle_turns()

                
        if pygame.time.get_ticks() > self.last_feelcheck+300:
            self.last_feelcheck = pygame.time.get_ticks()
            self.check_fightfeel_and_distress(self.hero)
            self.check_fightfeel_and_distress(self.enemy)

        

        if self.current_turn == "enemy": # später mal hier schon Feststellung richtigen Gegners!
            if (not (self.enemy.slash_CPN > 2)) and (pygame.time.get_ticks() > (self.LAT  + 700)):
                self.handle_turns()
            if self.enemy.attacking and (self.enemy.slash_CPN == 9) and not self.enemy_attack_consequence_happened:
                self.check_enemies_attack_consequences()



        if self.current_turn == "hero":  # folgend Verteidigungsmaßnahmen von Enemy
            
            if self.hero.attacking and (self.hero.slash_CPN in range(5,7)) and not \
               (self.enemy.start_defending or self.enemy.defending or self.enemy.ready_to_block or \
                self.enemy.start_release_defending or self.enemy.release_defending or self.enemy.start_defblocking or self.enemy.defblocking or \
                self.enemy.start_blocking or self.enemy.blocking or self.enemy.start_being_hitted or self.enemy.being_hitted):
                if not self.enemy.defense_calculated:
                    self.calculate_enemys_defense()

            
                    
            elif self.hero.attacking and (self.hero.slash_CPN == 9) and not self.hero.attack_done: # and (self.hero.attack_focus == self.enemy.ID) 
                if (self.enemy.ready_to_block and (((self.enemy.defense_typ == self.hero.attack_typ) and (self.enemy.defense_typ == "O")) or \
                                                   (self.enemy.defense_typ == "R" and self.hero.attack_typ == "L") or \
                                                   (self.enemy.defense_typ == "L" and self.hero.attack_typ == "R"))) and not \
                   (self.enemy.start_blocking or self.enemy.blocking or self.enemy.start_being_hitted or self.enemy.being_hitted or \
                   self.enemy.start_defending or self.enemy.defending or self.enemy.start_defblocking or self.enemy.defblocking):
                    self.enemy.start_blocking = True
                    self.start_knockback = True; self.kb_victim = self.enemy; self.kb_beater = self.hero; self.knockback_typ = "Block"
                    if pygame.time.get_ticks() > self.last_sound_played + 150:
                        self.sounds["tsching_"+self.enemy.defense_typ+"_sound"].play()
                        self.last_sound_played = pygame.time.get_ticks()
                        
                    else:
                        print("if - Error @ 1st COL 20")
                        
                    self.hero.attack_done = True
                    
                elif not (self.enemy.start_blocking or self.enemy.blocking):
                    if (self.enemy.defense_typ == self.hero.attack_typ) and (self.enemy.defense_typ == "U") and self.enemy.defblocking:
                        self.start_knockback = True; self.kb_victim = self.enemy; self.kb_beater = self.hero; self.knockback_typ = "Block"
                        if pygame.time.get_ticks() > self.last_sound_played + 150:
                            self.sounds["tsching_U_sound"].play()
                            self.last_sound_played = pygame.time.get_ticks()
                            
##                    elif (((s.dyingelf.enemy.defense_typ != self.hero.attack_typ) and (self.enemy.defense_typ in ["U", "O"])) or \
##                       (self.enemy.defense_typ == "R" and self.hero.attack_typ != "L") or (self.enemy.defense_typ == "L" and self.hero.attack_typ != "R")) and \
##                       not (self.enemy.start_being_hitted or self.enemy.being_hitted):
                    elif not (self.enemy.start_being_hitted or self.enemy.being_hitted):
                        if self.hero.attack_typ in ["O", "U"]:
                            self.enemy.hit_typ = self.hero.attack_typ
                        elif self.hero.attack_typ == "L":
                            self.enemy.hit_typ = "R"
                        elif self.hero.attack_typ == "R":
                            self.enemy.hit_typ = "L"
                        self.enemy.start_being_hitted = True
                        self.start_knockback = True; self.kb_victim = self.enemy; self.kb_beater = self.hero; self.knockback_typ = "Hit"

                        self.calculate_enemys_hp_loss() #############################
                        
                        if not self.enemy.hitpoints <= 0:
                            self.enemy.lifebar = pygame.image.load(Var.path+"\\pics\\Lifebars\\Lifebar_"+\
                                                           str(int(round(((self.enemy.hitpoints/self.enemy.maxhealth)*24), 0)))+".png").convert()
                            self.enemy.lifebar.set_colorkey([0,0,0], pygame.RLEACCEL)
                            self.enemy.lifebar.set_alpha(180, pygame.RLEACCEL)
                        else:
                            self.enemy.lifebar = pygame.image.load(Var.path+"\\pics\\Lifebars\\Lifebar_0.png").convert()
                            self.enemy.lifebar.set_colorkey([0,0,0], pygame.RLEACCEL)
                            self.enemy.lifebar.set_alpha(180, pygame.RLEACCEL)
                        self.enemy.ready_to_block = False

                    else:
                        print("if - Error @ 2nd COL 20")
                    self.hero.attack_done = True

                else:
                    print("if - Error @ COL 16")

            elif self.enemy.ready_to_block and ((self.hero.slash_CPN == 0) or (self.hero.slash_CPN >= 11)) and not \
                 (self.enemy.start_blocking or self.enemy.blocking or self.enemy.start_being_hitted or self.enemy.being_hitted or \
                  self.enemy.start_release_defending or self.enemy.release_defending or self.enemy.start_defending or \
                  self.enemy.defending or self.enemy.start_defblocking or self.enemy.defblocking):
                self.enemy.start_release_defending = True

        
                                                     
                                                     
                
        for e in self.enemies:  #NEU
            if e.dead or e.start_dying or e.dying or (e.hitpoints <= 0):
                if e in self.enemies:
                    self.enemies.remove(e)
                    #print(str(pygame.time.get_ticks())+":", "dying enemy removed from enemies!")
                    Var.screen_scrolling_happened = True  # = Nur, damit des versterbenden Feindes Battlesymbols weggehen,
                                                          # falls diese in den Background ragen.
            if (len(self.enemies) > 1) and not e.fighting:
                self.enemies.remove(e)
                if e == self.enemy:
                    self.switch_enemy()
                    #print(str(pygame.time.get_ticks())+":", "self.enemy removed from enemies, enemy switched during Turn!")
                Var.screen_scrolling_happened = True # für's Ausblenden der Battle-Symbole
                
                    




            
            
    def automatic_align_opponents(self):  # in Calculator aufgerufen
        
        self.hero.frameway = [0,0] # (sicherheitshalber nochmal frameway "resetet")

        for e in self.enemies:
            
            e.frameway = [0,0] # (sicherheitshalber nochmal frameways "resetet")
            
            if pygame.time.get_ticks() > self.align_LPT + self.align_TPP:
                self.align_LPT = pygame.time.get_ticks()
                if (not (-2 < (e.realpos[0]-self.hero.realpos[0]) <= 2)) and (not (-2 < (e.realpos[1]-self.hero.realpos[1]) <= 2)) \
                   and (not (-2 < (abs(e.realpos[0]-self.hero.realpos[0])) - (abs(e.realpos[1]-self.hero.realpos[1])) <= 2)):   # NICHT gerade oben, unten, links oder rechts
                                                                                                                                                            # und wenn Enemy NICHT in irgendeinem 45° Winkel steht...
                    if (e.realpos[0]-self.hero.realpos[0] < 0) and (e.realpos[1]-self.hero.realpos[1] < 0):  # Wenn Enemy links oben ist...
                        if ((e.realpos[0]-self.hero.realpos[0]) - abs(e.realpos[1]-self.hero.realpos[1])) > 0:  # Wenn Enemy im linken Bereich links oben ist...
                            if (abs(e.realpos[0]-self.hero.realpos[0])*5 - abs(e.realpos[1]-self.hero.realpos[1])*14) > 0:  # Wenn Enemy dort im linken Bereich ist...
                                self.hero.align_typ = "ROROR"
                            elif (abs(e.realpos[0]-self.hero.realpos[0])*5 - abs(e.realpos[1]-self.hero.realpos[1])*14) <= 0:  # Wenn Enemy dort im rechten Bereich ist...
                                self.hero.align_typ = "U"
                        elif (abs(e.realpos[0]-self.hero.realpos[0]) - abs(e.realpos[1]-self.hero.realpos[1])) <= 0:  # Wenn Enemy im rechten Bereich links oben ist...
                            if (abs(e.realpos[0]-self.hero.realpos[0])*14 - abs(e.realpos[1]-self.hero.realpos[1])*5) > 0:  # Wenn Enemy dort im linken Bereich ist...
                                self.hero.align_typ = "R"
                            elif (abs(e.realpos[0]-self.hero.realpos[0])*14 - abs(e.realpos[1]-self.hero.realpos[1])*5) <= 0:  # Wenn Enemy dort im rechten Bereich ist...
                                self.hero.align_typ = "LULLUL"
                                
                    elif (e.realpos[0]-self.hero.realpos[0] >= 0) and (e.realpos[1]-self.hero.realpos[1] < 0):  # Wenn Enemy rechts oben ist...
                        if (abs(e.realpos[0]-self.hero.realpos[0]) - abs(e.realpos[1]-self.hero.realpos[1])) <= 0:  # Wenn Enemy im linken Bereich rechts oben ist...
                            if (abs(e.realpos[0]-self.hero.realpos[0])*14 - abs(e.realpos[1]-self.hero.realpos[1])*5) <= 0:  # Wenn Enemy dort im linken Bereich ist...
                                self.hero.align_typ = "RURRUR"
                            elif (abs(e.realpos[0]-self.hero.realpos[0])*14 - abs(e.realpos[1]-self.hero.realpos[1])*5) > 0:  # Wenn Enemy dort im rechten Bereich ist...
                                self.hero.align_typ = "L"
                        elif (abs(e.realpos[0]-self.hero.realpos[0]) - abs(e.realpos[1]-self.hero.realpos[1])) > 0:  # Wenn Enemy im rechten Bereich rechts oben ist...
                            if (abs(e.realpos[0]-self.hero.realpos[0])*5 - abs(e.realpos[1]-self.hero.realpos[1])*14) <= 0:  # Wenn Enemy dort im linken Bereich ist...
                                self.hero.align_typ = "U"
                            elif (abs(e.realpos[0]-self.hero.realpos[0])*5 - abs(e.realpos[1]-self.hero.realpos[1])*14) > 0:  # Wenn Enemy dort im rechten Bereich ist...
                                self.hero.align_typ = "LOLOL"

                    elif (e.realpos[0]-self.hero.realpos[0] < 0) and (e.realpos[1]-self.hero.realpos[1] >= 0):  # Wenn Enemy links unten ist...
                        if (abs(e.realpos[0]-self.hero.realpos[0]) - abs(e.realpos[1]-self.hero.realpos[1])) > 0:  # Wenn Enemy im linken Bereich links unten ist...
                            if (abs(e.realpos[0]-self.hero.realpos[0])*5 - abs(e.realpos[1]-self.hero.realpos[1])*14) > 0:  # Wenn Enemy dort im linken Bereich ist...
                                self.hero.align_typ = "RURUR"
                            elif (abs(e.realpos[0]-self.hero.realpos[0])*5 - abs(e.realpos[1]-self.hero.realpos[1])*14) <= 0:  # Wenn Enemy dort im rechten Bereich ist...
                                self.hero.align_typ = "O"
                        elif (abs(e.realpos[0]-self.hero.realpos[0]) - abs(e.realpos[1]-self.hero.realpos[1])) <= 0:  # Wenn Enemy im rechten Bereich links unten ist...
                            if (abs(e.realpos[0]-self.hero.realpos[0])*14 - abs(e.realpos[1]-self.hero.realpos[1])*5) > 0:  # Wenn Enemy dort im linken Bereich ist...
                                self.hero.align_typ = "R"
                            elif (abs(e.realpos[0]-self.hero.realpos[0])*14 - abs(e.realpos[1]-self.hero.realpos[1])*5) <= 0:  # Wenn Enemy dort im rechten Bereich ist...
                                self.hero.align_typ = "LOLLOL"

                    elif (e.realpos[0]-self.hero.realpos[0] >= 0) and (e.realpos[1]-self.hero.realpos[1] >= 0):  # Wenn Enemy rechts unten ist...
                        if (abs(e.realpos[0]-self.hero.realpos[0]) - abs(e.realpos[1]-self.hero.realpos[1])) <= 0:  # Wenn Enemy im linken Bereich rechts unten ist...
                            if (abs(e.realpos[0]-self.hero.realpos[0])*14 - abs(e.realpos[1]-self.hero.realpos[1])*5) <= 0:  # Wenn Enemy dort im linken Bereich ist...
                                self.hero.align_typ = "RORROR"
                            elif (abs(e.realpos[0]-self.hero.realpos[0])*14 - abs(e.realpos[1]-self.hero.realpos[1])*5) > 0:  # Wenn Enemy dort im rechten Bereich ist...
                                self.hero.align_typ = "L"
                        elif (abs(e.realpos[0]-self.hero.realpos[0]) - abs(e.realpos[1]-self.hero.realpos[1])) > 0:  # Wenn Enemy im rechten Bereich rechts oben ist...
                            if (abs(e.realpos[0]-self.hero.realpos[0])*5 - abs(e.realpos[1]-self.hero.realpos[1])*14) <= 0:  # Wenn Enemy dort im linken Bereich ist...
                                self.hero.align_typ = "O"
                            elif (abs(e.realpos[0]-self.hero.realpos[0])*5 - abs(e.realpos[1]-self.hero.realpos[1])*14) > 0:  # Wenn Enemy dort im rechten Bereich ist...
                                self.hero.align_typ = "LULUL"

                    if self.hero.align_typ == "O":
                        e.frameway[1] += 1
                        ## if len(self.enemies) == 1:
                        self.hero.frameway[1] -= 1
                    elif self.hero.align_typ == "U":
                        e.frameway[1] -= 1
                        ## if len(self.enemies) == 1:
                        self.hero.frameway[1] += 1
                    elif self.hero.align_typ == "L":
                        e.frameway[0] += 1
                        ## if len(self.enemies) == 1:
                        self.hero.frameway[0] -= 1
                    elif self.hero.align_typ == "R":
                        e.frameway[0] -= 1
                        ## if len(self.enemies) == 1:
                        self.hero.frameway[0] += 1
                    if self.hero.align_typ in ["ROROR", "LOLOL", "RURUR", "LULUL", "LULLUL", "RURRUR", "LOLLOL", "RORROR"]:
                        self.hero.align_step += 1
                    if self.hero.align_typ == "ROROR":
                        if self.hero.align_step in [1,3,5]: # R
                            e.frameway[0] -= 1
                            ## if len(self.enemies) == 1:
                            self.hero.frameway[0] += 1
                        elif self.hero.align_step in [2,4]: # O
                            e.frameway[1] += 1
                            ## if len(self.enemies) == 1:
                            self.hero.frameway[1] -= 1
                    elif self.hero.align_typ == "LULLUL":
                        if self.hero.align_step in [1,3,4,6]: # L
                            e.frameway[0] += 1
                            ## if len(self.enemies) == 1:
                            self.hero.frameway[0] -= 1
                        elif self.hero.align_step in [2,5]: # U
                            e.frameway[1] -= 1
                            ## if len(self.enemies) == 1:
                            self.hero.frameway[1] += 1
                    elif self.hero.align_typ == "RURRUR":
                        if self.hero.align_step in [1,3,4,6]: # R
                            e.frameway[0] -= 1
                            ## if len(self.enemies) == 1:
                            self.hero.frameway[0] += 1
                        elif self.hero.align_step in [2,5]: # U
                            e.frameway[1] -= 1
                            ## if len(self.enemies) == 1:
                            self.hero.frameway[1] += 1
                    elif self.hero.align_typ == "LOLOL":
                        if self.hero.align_step in [1,3,5]: # L
                            e.frameway[0] += 1
                            ## if len(self.enemies) == 1:
                            self.hero.frameway[0] -= 1
                        elif self.hero.align_step in [2,4]: # O
                            e.frameway[1] += 1
                            ## if len(self.enemies) == 1:
                            self.hero.frameway[1] -= 1
                    elif self.hero.align_typ == "RURUR":
                        if self.hero.align_step in [1,3,5]: # R
                            e.frameway[0] -= 1
                            ## if len(self.enemies) == 1:
                            self.hero.frameway[0] += 1
                        elif self.hero.align_step in [2,4]: # U
                            e.frameway[1] -= 1
                            ## if len(self.enemies) == 1:
                            self.hero.frameway[1] += 1
                    elif self.hero.align_typ == "LOLLOL":
                        if self.hero.align_step in [1,3,4,6]: # L
                            e.frameway[0] += 1
                            ## if len(self.enemies) == 1:
                            self.hero.frameway[0] -= 1
                        elif self.hero.align_step in [2,5]: # O
                            e.frameway[1] += 1
                            ## if len(self.enemies) == 1:
                            self.hero.frameway[1] -= 1
                    elif self.hero.align_typ == "RORROR":
                        if self.hero.align_step in [1,3,4,6]: # R
                            e.frameway[0] -= 1
                            ## if len(self.enemies) == 1:
                            self.hero.frameway[0] += 1
                        elif self.hero.align_step in [2,5]: # O
                            e.frameway[1] += 1
                            ## if len(self.enemies) == 1:
                            self.hero.frameway[1] -= 1
                    elif self.hero.align_typ == "LULUL":
                        if self.hero.align_step in [1,3,5]: # L
                            e.frameway[0] += 1
                            ## if len(self.enemies) == 1:
                            self.hero.frameway[0] -= 1
                        elif self.hero.align_step in [2,4]: # U
                            e.frameway[1] -= 1
                            ## if len(self.enemies) == 1:
                            self.hero.frameway[1] += 1
                    if self.hero.align_typ in ["ROROR", "LOLOL", "RURUR", "LULUL"]:
                        if self.hero.align_step == 5:
                            self.hero.align_step = 0
                    elif self.hero.align_typ in ["LULLUL", "RURRUR", "LOLLOL", "RORROR"]:
                        if self.hero.align_step == 6:
                            self.hero.align_step = 0

                        
                elif self.hero.align_typ:
                    self.hero.align_typ = ""
                    self.hero.align_step = 0


                if not int(math.sqrt((((abs((e.realpos[0]+e.frameway[0])-(self.hero.realpos[0]+self.hero.frameway[0]))**2)//4)*3)+\
                                     (abs((e.realpos[1]+e.frameway[1])-(self.hero.realpos[1]+self.hero.frameway[1]))**2))) <= 66:
                    other_functions.magnet(self.hero, e)

                
                elif int(math.sqrt((((abs((e.realpos[0]+e.frameway[0])-(self.hero.realpos[0]+self.hero.frameway[0]))**2)//4)*3)+\
                                   (abs((e.realpos[1]+e.frameway[1])-(self.hero.realpos[1]+self.hero.frameway[1]))**2))) < 60:
                    other_functions.drift_apart(self.hero, e)



                
    def handle_knockback(self):  # in Calculator aufgerufen
        if self.start_knockback:
            self.start_knockback = False
            self.knockback_done = False
            self.knockbacking = True
            self.knockback_power = self.kb_beater.knockback - self.kb_victim.sturdiness
            if (self.knockback_typ == "Hit") and (self.knockback_power == 0):
                self.knockback_power = 1
            if (-3 <= self.kb_victim.realpos[0]-self.kb_beater.realpos[0] <= 3) and (self.kb_victim.realpos[1]-self.kb_beater.realpos[1] < 0):
                self.knockback_dir = "N"
            elif (-3 <= self.kb_victim.realpos[0]-self.kb_beater.realpos[0] <= 3) and (self.kb_victim.realpos[1]-self.kb_beater.realpos[1] > 0):
                self.knockback_dir = "S"
            elif (-3 <= self.kb_victim.realpos[1]-self.kb_beater.realpos[1] <= 3) and (self.kb_victim.realpos[0]-self.kb_beater.realpos[0] < 0):
                self.knockback_dir = "W"
            elif (-3 <= self.kb_victim.realpos[1]-self.kb_beater.realpos[1] <= 3) and (self.kb_victim.realpos[0]-self.kb_beater.realpos[0] > 0):
                self.knockback_dir = "E"
            elif -3 <= (abs(self.kb_victim.realpos[0]-self.kb_beater.realpos[0]) - abs(self.kb_victim.realpos[1]-self.kb_beater.realpos[1])) <= 3: # 45° Stellung
                if (self.kb_victim.realpos[0]-self.kb_beater.realpos[0] < 0) and (self.kb_victim.realpos[1]-self.kb_beater.realpos[1] < 0):
                    self.knockback_dir = "NW"
                elif (self.kb_victim.realpos[0]-self.kb_beater.realpos[0] > 0) and (self.kb_victim.realpos[1]-self.kb_beater.realpos[1] < 0):
                    self.knockback_dir = "NE"
                elif (self.kb_victim.realpos[0]-self.kb_beater.realpos[0] < 0) and (self.kb_victim.realpos[1]-self.kb_beater.realpos[1] > 0):
                    self.knockback_dir = "SW"
                elif (self.kb_victim.realpos[0]-self.kb_beater.realpos[0] > 0) and (self.kb_victim.realpos[1]-self.kb_beater.realpos[1] > 0):
                    self.knockback_dir = "SE"
            elif (abs(self.kb_victim.realpos[0]-self.kb_beater.realpos[0]) - abs(self.kb_victim.realpos[1]-self.kb_beater.realpos[1])) < -3: # X-schwache & Y-starke Stellung
                if (self.kb_victim.realpos[0]-self.kb_beater.realpos[0] < 0) and (self.kb_victim.realpos[1]-self.kb_beater.realpos[1] < 0):
                    self.knockback_dir = "NNW"
                elif (self.kb_victim.realpos[0]-self.kb_beater.realpos[0] > 0) and (self.kb_victim.realpos[1]-self.kb_beater.realpos[1] < 0):
                    self.knockback_dir = "NNE"
                elif (self.kb_victim.realpos[0]-self.kb_beater.realpos[0] < 0) and (self.kb_victim.realpos[1]-self.kb_beater.realpos[1] > 0):
                    self.knockback_dir = "SSW"
                elif (self.kb_victim.realpos[0]-self.kb_beater.realpos[0] > 0) and (self.kb_victim.realpos[1]-self.kb_beater.realpos[1] > 0):
                    self.knockback_dir = "SSE"
            elif (abs(self.kb_victim.realpos[0]-self.kb_beater.realpos[0]) - abs(self.kb_victim.realpos[1]-self.kb_beater.realpos[1])) > 3: # X-starke & Y-schwache Stellung
                if (self.kb_victim.realpos[0]-self.kb_beater.realpos[0] < 0) and (self.kb_victim.realpos[1]-self.kb_beater.realpos[1] < 0):
                    self.knockback_dir = "NWW"
                elif (self.kb_victim.realpos[0]-self.kb_beater.realpos[0] > 0) and (self.kb_victim.realpos[1]-self.kb_beater.realpos[1] < 0):
                    self.knockback_dir = "NEE"
                elif (self.kb_victim.realpos[0]-self.kb_beater.realpos[0] < 0) and (self.kb_victim.realpos[1]-self.kb_beater.realpos[1] > 0):
                    self.knockback_dir = "SWW"
                elif (self.kb_victim.realpos[0]-self.kb_beater.realpos[0] > 0) and (self.kb_victim.realpos[1]-self.kb_beater.realpos[1] > 0):
                    self.knockback_dir = "SEE"
            
        elif self.knockbacking:
            if not self.knockback_done and (( not ((self.hero.stressed) and (self.current_turn == "enemy"))) or ( not ((self.enemy.stressed) and (self.current_turn == "hero")))):
                
                if pygame.time.get_ticks() > self.knockback_LPT + self.knockback_TPP:
                    self.knockback_LPT = pygame.time.get_ticks()
                    self.knockback_CPN += 1
                    if self.knockback_dir in ["N","E","W","S"]:
                        if self.knockback_power >= 0:
                            if self.knockback_dir == "N":
                                self.kb_victim.frameway[1] -= 1
                                self.kb_beater.frameway[1] -= 1
                            elif self.knockback_dir == "E":
                                self.kb_victim.frameway[0] += 1
                                self.kb_beater.frameway[0] += 1
                            elif self.knockback_dir == "W":
                                self.kb_victim.frameway[0] -= 1
                                self.kb_beater.frameway[0] -= 1
                            elif self.knockback_dir == "S":
                                self.kb_victim.frameway[1] += 1
                                self.kb_beater.frameway[1] += 1
                        if ((self.knockback_typ == "Block") or ((self.knockback_typ == "Hit") and (self.knockback_power == 0))) and \
                           (self.knockback_CPN >= (3*self.knockback_power)//2):
                            self.knockback_done = True
                        elif (self.knockback_typ == "Hit") and (self.knockback_CPN >= 3*self.knockback_power):
                            self.knockback_done = True
                        elif self.knockback_power <= 0:
                            self.knockback_done = True
                        
       
                    elif self.knockback_dir in ["NW","NE","SW","SE"]:
                        if self.knockback_power >= 0:
                            if self.knockback_dir == "NW":
                                if self.knockback_CPN % 2: # ungerade
                                    self.kb_victim.frameway[0] -= 1
                                    self.kb_beater.frameway[1] -= 1
                                else: # gerade
                                    self.kb_victim.frameway[1] -= 1
                                    self.kb_beater.frameway[0] -= 1
                            elif self.knockback_dir == "NE":
                                if self.knockback_CPN % 2: # ungerade
                                    self.kb_victim.frameway[0] += 1
                                    self.kb_beater.frameway[1] -= 1
                                else: # gerade
                                    self.kb_victim.frameway[1] -= 1
                                    self.kb_beater.frameway[0] += 1
                            elif self.knockback_dir == "SW":
                                if self.knockback_CPN % 2: # ungerade
                                    self.kb_victim.frameway[1] += 1
                                    self.kb_beater.frameway[0] -= 1
                                else: # gerade
                                    self.kb_victim.frameway[0] -= 1
                                    self.kb_beater.frameway[1] += 1
                            elif self.knockback_dir == "SE":
                                if self.knockback_CPN % 2: # ungerade
                                    self.kb_victim.frameway[1] += 1
                                    self.kb_beater.frameway[0] += 1
                                else: # gerade
                                    self.kb_victim.frameway[0] += 1
                                    self.kb_beater.frameway[1] += 1
                        if ((self.knockback_typ == "Block") or ((self.knockback_typ == "Hit") and (self.knockback_power == 0))) and \
                           (self.knockback_CPN >= (4*self.knockback_power)//2):
                            self.knockback_done = True
                        elif (self.knockback_typ == "Hit") and (self.knockback_CPN >= 4*self.knockback_power):
                            self.knockback_done = True
                        elif self.knockback_power <= 0:
                            self.knockback_done = True
                        
                            
                    elif self.knockback_dir in ["NNW","NNE","SSW","SSE","NWW","NEE","SWW","SEE"]:  # interessant in Zukunft v.a. bei Fernangriffen (ohne alignment)
                        if self.knockback_power >= 0:
                            if self.knockback_dir == "NNW":
                                if not (self.knockback_CPN % 3): # jeder Dritte
                                    self.kb_victim.frameway[0] -= 1
                                    self.kb_beater.frameway[0] -= 1
                                else:
                                    self.kb_victim.frameway[1] -= 1
                                    self.kb_beater.frameway[1] -= 1
                            elif self.knockback_dir == "NNE":
                                if not (self.knockback_CPN % 3):
                                    self.kb_victim.frameway[0] += 1
                                    self.kb_beater.frameway[0] += 1
                                else:
                                    self.kb_victim.frameway[1] -= 1
                                    self.kb_beater.frameway[1] -= 1
                            elif self.knockback_dir == "SSW":
                                if not (self.knockback_CPN % 3):
                                    self.kb_victim.frameway[0] -= 1
                                    self.kb_beater.frameway[0] -= 1
                                else:
                                    self.kb_victim.frameway[1] += 1
                                    self.kb_beater.frameway[1] += 1
                            elif self.knockback_dir == "SSE":
                                if not (self.knockback_CPN % 3):
                                    self.kb_victim.frameway[0] += 1
                                    self.kb_beater.frameway[0] += 1
                                else:
                                    self.kb_victim.frameway[1] += 1
                                    self.kb_beater.frameway[1] += 1
                            elif self.knockback_dir == "NWW":
                                if not (self.knockback_CPN % 3):
                                    self.kb_victim.frameway[1] -= 1
                                    self.kb_beater.frameway[1] -= 1
                                else:
                                    self.kb_victim.frameway[0] -= 1
                                    self.kb_beater.frameway[0] -= 1
                            elif self.knockback_dir == "NEE":
                                if not (self.knockback_CPN % 3):
                                    self.kb_victim.frameway[1] -= 1
                                    self.kb_beater.frameway[1] -= 1
                                else:
                                    self.kb_victim.frameway[0] += 1
                                    self.kb_beater.frameway[0] += 1
                            elif self.knockback_dir == "SWW":
                                if not (self.knockback_CPN % 3):
                                    self.kb_victim.frameway[1] += 1
                                    self.kb_beater.frameway[1] += 1
                                else:
                                    self.kb_victim.frameway[0] -= 1
                                    self.kb_beater.frameway[0] -= 1
                            elif self.knockback_dir == "SEE":
                                if not (self.knockback_CPN % 3):
                                    self.kb_victim.frameway[1] += 1
                                    self.kb_beater.frameway[1] += 1
                                else:
                                    self.kb_victim.frameway[0] += 1
                                    self.kb_beater.frameway[0] += 1

                        if self.knockback_power < 0:
                            self.knockback_done = True
                        if (self.knockback_power == 0):
                            if (self.knockback_typ == "Hit") and (self.knockback_CPN == 2):
                                self.knockback_done = True
                            elif (self.knockback_typ == "Block"):
                                self.knockback_done = True
                                
                        elif self.knockback_power == 1:
                            if (self.knockback_typ == "Block") and (self.knockback_CPN == 2):
                                self.knockback_done = True
                            elif (self.knockback_typ == "Hit") and (self.knockback_CPN == 4):
                                self.knockback_done = True
                                
                        elif not (self.knockback_power % 2): # gerade
                            if (self.knockback_typ == "Block") and (self.knockback_CPN+2 >= ((self.knockback_power//2)*9)//2):
                                self.knockback_done = True
                            elif (self.knockback_typ == "Hit") and (self.knockback_CPN+2 >= (self.knockback_power//2)*9):
                                self.knockback_done = True
                        else: # ungerade
                            if (self.knockback_typ == "Block") and (self.knockback_CPN-3 >= (((self.knockback_power-1)//2)*9)//2):
                                self.knockback_done = True
                            elif (self.knockback_typ == "Hit") and (self.knockback_CPN-3 >= (((self.knockback_power-1)//2)*9)):
                                self.knockback_done = True

            else:
                self.knockbacking = False   # knockback_done wird erst bei start_knockback oben wieder auf False gesetzt.
                self.knockback_CPN = 0
                self.kb_victim = None
                self.kb_beater = None
                self.knockback_dir = ""
                self.knockback_typ = ""
                self.knockback_power = 0
                        


    def check_fightfeel_and_distress(self, unit):  # in handle_the_battle() aufgerufen
        
        for cc in unit.fightborder_masktypes:
            if (not (cc in Var.blitlist)) or (cc in Var.units.values()) or (cc == self.hero) or (cc == self.enemy):
                unit.fightborder_masktypes.remove(cc)
        for b in Var.blitlist:
            if not ((b == unit) or (b in unit.fightborder_masktypes) or (b in Var.units.values()) or (b == self.enemy) or (b == self.hero)):
                if (b in Var.borders.values()) or (b in Var.doors.values()) or (b in Var.obstacles.values()) or (b in Var.animated_obstacles.values()):
                    unit.fightborder_masktypes.append(b)  # im Vgl. zu get_other_blitted_masktypes (in figure_functions) KEINE Charactere mit dabei, nur feste Hindernisse.

        a = 0
        for fm in unit.fightborder_masktypes:
            if fm.mask.overlap_area(unit.fight_feelmask, [unit.pos[0]-fm.pos[0], unit.pos[1]-fm.pos[1]]):
                a += 1
        if a >= 1:
            if not unit.stressed:
                unit.stressed = True
                if unit == self.hero:
                    self.hero.defend_TPP = self.hero.faster_defend_TPP    #
                    self.enemy.slash_TPP = self.enemy.faster_slash_TPP  ##
                    self.enemy.defend_TPP = self.enemy.faster_defend_TPP
                    self.check_action_time()
                else:                                                   ### Ganz unten in fightpic_functions "calculate_fightpic_speeds" dynamisch erstellt!
                    self.hero.slash_TPP = self.hero.faster_slash_TPP    ##
                    self.enemy.slash_TPP = self.enemy.slower_slash_TPP  #
                    self.enemy.defend_TPP = self.enemy.slower_defend_TPP
                    self.check_action_time()                               #
        elif unit.stressed:                                          #
            unit.stressed = False                                  #
            self.hero.slash_TPP = self.hero.normal_slash_TPP    ##
            self.enemy.slash_TPP = self.enemy.normal_slash_TPP  ##
            self.check_action_time()
            







        

        
