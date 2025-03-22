import pygame
import pool
from pool import Var
import basic_types
import random


## attack(figure)
## defend_button(figure)
## defend(figure)
## release_defend(figure)
## block(figure)
## defblock(figure)
## hit(figure)
## die(figure)
## draw_button(figure)
## draw(figure)
## put_away(figure)
## calculate_fightpic_speeds(figure)


def attack(figure):
    if not figure == Var.hero:
        folder = "Monsters\\"
    else:
        folder = ""
    if figure.start_attack:
        figure.start_attack = False
        figure.attacking = True
        figure.ready_to_block = False
        if not figure.attack_typ:
            figure.attack_typ = random.choice(figure.attacks)
            if not figure == Var.hero:
                print(str(pygame.time.get_ticks())+":", "Enemy Attack_Typ EXTRA random choosen in attack():", figure.attack_typ)
            else:
                print(str(pygame.time.get_ticks())+":", "random choosen Hero Attack_typ because it was missing:", figure.attack_typ)
        if figure.attack_typ:
            if pygame.time.get_ticks() > figure.last_sound_played + 150:
                figure.sounds["slash_"+figure.attack_typ+"_sound"].play()
                figure.last_sound_played = pygame.time.get_ticks()
        figure.current_pics.clear()
        figure.current_pics["Slash_1"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Offense\\Slash_'+figure.attack_typ+'\\'+figure.name+'_'+figure.dir+'_Slash_'+figure.attack_typ+'_1.png').convert_alpha()
        figure.current_pics["Slash_2"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Offense\\Slash_'+figure.attack_typ+'\\'+figure.name+'_'+figure.dir+'_Slash_'+figure.attack_typ+'_2.png').convert_alpha()
        figure.current_pics["Slash_3"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Offense\\Slash_'+figure.attack_typ+'\\'+figure.name+'_'+figure.dir+'_Slash_'+figure.attack_typ+'_3.png').convert_alpha()
        figure.current_pics["Slash_4"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Offense\\Slash_'+figure.attack_typ+'\\'+figure.name+'_'+figure.dir+'_Slash_'+figure.attack_typ+'_4.png').convert_alpha()
        figure.current_pics["Slash_5"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Offense\\Slash_'+figure.attack_typ+'\\'+figure.name+'_'+figure.dir+'_Slash_'+figure.attack_typ+'_5.png').convert_alpha()
        figure.current_pics["Slash_6"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Offense\\Slash_'+figure.attack_typ+'\\'+figure.name+'_'+figure.dir+'_Slash_'+figure.attack_typ+'_6.png').convert_alpha()
        figure.current_pics["Slash_7"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Offense\\Slash_'+figure.attack_typ+'\\'+figure.name+'_'+figure.dir+'_Slash_'+figure.attack_typ+'_7.png').convert_alpha()
        figure.current_pics["Slash_8"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Offense\\Slash_'+figure.attack_typ+'\\'+figure.name+'_'+figure.dir+'_Slash_'+figure.attack_typ+'_8.png').convert_alpha()
        figure.current_pics["Slash_9"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Offense\\Slash_'+figure.attack_typ+'\\'+figure.name+'_'+figure.dir+'_Slash_'+figure.attack_typ+'_9.png').convert_alpha()
        figure.current_pics["Slash_10"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Offense\\Slash_'+figure.attack_typ+'\\'+figure.name+'_'+figure.dir+'_Slash_'+figure.attack_typ+'_10.png').convert_alpha()
        figure.current_pics["Slash_11"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Offense\\Slash_'+figure.attack_typ+'\\'+figure.name+'_'+figure.dir+'_Slash_'+figure.attack_typ+'_11.png').convert_alpha()
        figure.current_pics["Slash_12"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Offense\\Slash_'+figure.attack_typ+'\\'+figure.name+'_'+figure.dir+'_Slash_'+figure.attack_typ+'_12.png').convert_alpha()
    if figure.attacking:
        if figure.LPT + figure.slash_TPP < pygame.time.get_ticks():
            figure.LPT = pygame.time.get_ticks()
            #print(str(pygame.time.get_ticks())+":", figure.name+"-Slash_CPN="+str(figure.slash_CPN))
            if not figure.slash_CPN >= 12:
                figure.slash_CPN += 1
                try:
                    figure.image = figure.current_pics["Slash_"+str(figure.slash_CPN)]
                except:
                    if figure.attack_typ:
                        figure.image = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Offense\\Slash_'+figure.attack_typ+'\\'+figure.name+'_'+figure.dir+'_Slash_'+figure.attack_typ+'_'+str(figure.slash_CPN)+'.png').convert_alpha()
            elif figure.slash_CPN == 12:
                figure.slash_CPN += 1
                try:
                    figure.image = figure.current_pics["Slash_12"]
                except:
                    if figure.attack_typ:
                        figure.image = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Offense\\Slash_'+figure.attack_typ+'\\'+figure.name+'_'+figure.dir+'_Slash_'+figure.attack_typ+'_12.png').convert_alpha()
            else:
                figure.slash_CPN = 0 # Vorbereitung fürs nächste Mal
                figure.image = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Fight\\'+figure.name+"_"+figure.dir+"_Fight_1.png").convert_alpha()
                figure.attack_typ = False
                #print(str(pygame.time.get_ticks())+":", "Attack_Typ deleted:", figure.name, figure.ID)
                figure.attacking = False


def defend_button(figure):
    if not figure == Var.hero:
        folder = "Monsters\\"
    else:
        folder = ""
    if figure.defense_typ:
        if not (figure.defense_typ == "U"):
            figure.LPT = pygame.time.get_ticks()
            if figure.start_release_defending:
                if figure.defending:
                    figure.defending = False
                if figure.ready_to_block:
                    figure.defend_CPN = 5
                else:
                    figure.defend_CPN += 1   # für schöneren "Rückgang" der Defense-Bewegung
                figure.ready_to_block = False
                figure.release_defending = True
                figure.start_release_defending = False
            elif figure.start_defending:
                if figure.release_defending:
                    figure.release_defending = False
                figure.defend_CPN = 0
                figure.defending = True
                figure.start_defending = False
            figure.current_pics.clear()
            figure.current_pics["Def_1"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Defense\\'+figure.name+"_"+figure.dir+"_Def_"+figure.defense_typ+"_1.png").convert_alpha()
            figure.current_pics["Def_2"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Defense\\'+figure.name+"_"+figure.dir+"_Def_"+figure.defense_typ+"_2.png").convert_alpha()
            figure.current_pics["Def_3"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Defense\\'+figure.name+"_"+figure.dir+"_Def_"+figure.defense_typ+"_3.png").convert_alpha()
            figure.current_pics["Def_4"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Defense\\'+figure.name+"_"+figure.dir+"_Def_"+figure.defense_typ+"_4.png").convert_alpha()
        elif (figure.defense_typ == "U"):
            figure.start_defending = False
            figure.defending = False
            
            if (figure.defend_CPN > 1) and not (figure.start_release_defending or figure.release_defending):
                figure.start_release_defending = True
            else:
                figure.start_defblocking = True
    else:
        figure.start_defending = False; figure.start_release_defending = False; figure.defend_CPN = 0
        figure.image = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Fight\\'+figure.name+"_"+figure.dir+"_Fight_1.png").convert_alpha()
    

def defend(figure):
    if not figure == Var.hero:
        folder = "Monsters\\"
    else:
        folder = ""
    if not (figure.defense_typ == "U"):
        if figure.LPT + figure.defend_TPP < pygame.time.get_ticks():
            figure.LPT = pygame.time.get_ticks()
            #print(str(pygame.time.get_ticks())+":", figure.name+"-Defend_CPN="+str(figure.defend_CPN))
            if not figure.defend_CPN >= 4:
                figure.defend_CPN += 1
                try:
                    figure.image = figure.current_pics["Def_"+str(figure.defend_CPN)]
                except:
                    figure.image = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Defense\\'+figure.name+"_"+figure.dir+"_Def_"+figure.defense_typ+"_"+str(figure.defend_CPN)+".png").convert_alpha()
            elif figure.defend_CPN == 4:
                try:
                    figure.image = figure.current_pics["Def_4"]
                except:
                    figure.current_pics["Def_4"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Defense\\'+figure.name+"_"+figure.dir+"_Def_"+figure.defense_typ+"_4.png").convert_alpha()
                figure.defending = False
                figure.ready_to_block = True
    else:
        figure.defending = False; figure.defend_CPN = 0
        figure.image = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Fight\\'+figure.name+"_"+figure.dir+"_Fight_1.png").convert_alpha()
        

def release_defend(figure):
    if not (figure.attacking or figure.being_hitted):
        if not figure == Var.hero:
            folder = "Monsters\\"
        else:
            folder = ""
        if figure.LPT + figure.defend_TPP < pygame.time.get_ticks():
            figure.LPT = pygame.time.get_ticks()
            if not figure.defend_CPN <= 1:
                figure.defend_CPN -= 1
                if not figure.defense_typ == "U":
                    if figure.defend_CPN > 4:
                        figure.defend_CPN = 4
                    try:
                        figure.image = figure.current_pics["Def_"+str(figure.defend_CPN)]
                    except:
                        figure.image = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Defense\\'+figure.name+"_"+figure.dir+"_Def_"+figure.defense_typ+"_"+str(figure.defend_CPN)+".png").convert_alpha()
            elif figure.defend_CPN == 1:
                figure.defend_CPN -= 1
                if not figure.defense_typ == "U":
                    try:
                        figure.image = figure.current_pics["Def_1"]
                    except:
                        figure.image = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Defense\\'+figure.name+"_"+figure.dir+"_Def_"+figure.defense_typ+"_1.png").convert_alpha()
                                   # hier aufgrund Fehlers umständlich und auf Pfad und nicht auf entsprechendes current_pic zurückgegriffen.
            else:
                figure.release_defending = False
                figure.image = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Fight\\'+figure.name+"_"+figure.dir+"_Fight_1.png").convert_alpha()

            
def block(figure):
    if not figure.defense_typ == "U":
        if not figure == Var.hero:
            folder = "Monsters\\"
        else:
            folder = ""
        if figure.start_blocking:
            figure.start_blocking = False
            figure.blocking = True
            figure.current_pics.clear()
            figure.current_pics["Block_1"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Block\\'+figure.name+"_"+figure.dir+"_Block_"+figure.defense_typ+"_1.png").convert_alpha()
            figure.current_pics["Block_2"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Block\\'+figure.name+"_"+figure.dir+"_Block_"+figure.defense_typ+"_2.png").convert_alpha()
            figure.current_pics["Block_3"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Block\\'+figure.name+"_"+figure.dir+"_Block_"+figure.defense_typ+"_3.png").convert_alpha()
        if figure.blocking:
            if figure.LPT + 100 < pygame.time.get_ticks(): # Hier wird daweil noch pauschal Geschwindigkeit der Abblockbewegung bestimmt! (Zahl!)
                figure.LPT = pygame.time.get_ticks()
                if not figure.block_CPN >= 3:
                    figure.block_CPN += 1
                    try:
                        figure.image = figure.current_pics["Block_"+str(figure.block_CPN)]
                    except KeyError:
                        figure.image = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Block\\'+figure.name+"_"+figure.dir+"_Block_"+figure.defense_typ+"_"+str(figure.block_CPN)+".png").convert_alpha()
                elif figure.block_CPN == 3:
                    figure.block_CPN += 1
                    try:
                        figure.image = figure.current_pics["Block_3"]
                    except:
                        figure.image = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Block\\'+figure.name+"_"+figure.dir+"_Block_"+figure.defense_typ+"_3.png").convert_alpha()
                else:
                    figure.block_CPN = 0 # Vorbereitung fürs nächste Mal
                    try:
                        figure.image = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Defense\\'+figure.name+"_"+figure.dir+"_Def_"+figure.defense_typ+"_4.png").convert_alpha()
                    except:
                        print("ERROR OCCURED when switching from block3 to defense4: There's NO defense_typ!")
                    figure.blocking = False
    else:
        u.start_blocking = False
    


def defblock(figure):
    if figure.defense_typ == "U":
        if not figure == Var.hero:
            folder = "Monsters\\"
        else:
            folder = ""
        if figure.start_defblocking:
            figure.start_defblocking = False
            figure.defblocking = True
            figure.current_pics.clear()
            figure.current_pics["Defblock_1"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Defblock\\'+figure.name+"_"+figure.dir+"_Defblock_"+figure.defense_typ+"_1.png").convert_alpha()
            figure.current_pics["Defblock_2"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Defblock\\'+figure.name+"_"+figure.dir+"_Defblock_"+figure.defense_typ+"_2.png").convert_alpha()
            figure.current_pics["Defblock_3"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Defblock\\'+figure.name+"_"+figure.dir+"_Defblock_"+figure.defense_typ+"_3.png").convert_alpha()
            figure.current_pics["Defblock_4"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Defblock\\'+figure.name+"_"+figure.dir+"_Defblock_"+figure.defense_typ+"_4.png").convert_alpha()
            figure.current_pics["Defblock_5"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Defblock\\'+figure.name+"_"+figure.dir+"_Defblock_"+figure.defense_typ+"_5.png").convert_alpha()
            figure.current_pics["Defblock_6"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Defblock\\'+figure.name+"_"+figure.dir+"_Defblock_"+figure.defense_typ+"_6.png").convert_alpha()
            figure.current_pics["Defblock_7"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Defblock\\'+figure.name+"_"+figure.dir+"_Defblock_"+figure.defense_typ+"_7.png").convert_alpha()
            figure.current_pics["Defblock_8"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Defblock\\'+figure.name+"_"+figure.dir+"_Defblock_"+figure.defense_typ+"_8.png").convert_alpha()
            figure.current_pics["Defblock_9"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Defblock\\'+figure.name+"_"+figure.dir+"_Defblock_"+figure.defense_typ+"_9.png").convert_alpha() 
        if figure.defblocking:
            if figure.LPT + figure.defend_TPP < pygame.time.get_ticks():  # hier sinngemäß auch "defend_TPP" angewandt
                figure.LPT = pygame.time.get_ticks()
                if not figure.defblock_CPN >= 9:
                    figure.defblock_CPN += 1
                    try:
                        figure.image = figure.current_pics["Defblock_"+str(figure.defblock_CPN)]
                    except:
                        pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Defblock\\'+figure.name+"_"+figure.dir+"_Defblock_"+figure.defense_typ+"_"+str(figure.defblock_CPN)+".png").convert_alpha()
                elif figure.defblock_CPN == 9:
                    figure.defblock_CPN += 1
                    try:
                        figure.image = figure.current_pics["Defblock_9"]
                    except:
                        pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Defblock\\'+figure.name+"_"+figure.dir+"_Defblock_"+figure.defense_typ+"_9.png").convert_alpha()
                else:
                    figure.defblock_CPN = 0 # Vorbereitung fürs nächste Mal
                    figure.image = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Fight\\'+figure.name+"_"+figure.dir+"_Fight_1.png").convert_alpha()
                    figure.defblocking = False
    else:
        figure.start_defblocking = False


def hit(figure):
    if not figure == Var.hero:
        folder = "Monsters\\"
    else:
        folder = ""
    if figure.start_being_hitted:
        figure.start_being_hitted = False
        figure.being_hitted = True
        figure.ready_to_block = False
        if pygame.time.get_ticks() > figure.last_sound_played + 150:
            figure.sounds["hit_"+figure.hit_typ+"_sound"].play()
            figure.last_sound_played = pygame.time.get_ticks()
        figure.current_pics.clear()
        figure.current_pics["Hit_1"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Hit\\'+figure.name+"_"+figure.dir+"_Hit_"+figure.hit_typ+"_1.png").convert_alpha()
        figure.current_pics["Hit_2"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Hit\\'+figure.name+"_"+figure.dir+"_Hit_"+figure.hit_typ+"_2.png").convert_alpha()
        figure.current_pics["Hit_3"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Hit\\'+figure.name+"_"+figure.dir+"_Hit_"+figure.hit_typ+"_3.png").convert_alpha()
        figure.current_pics["Hit_4"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Hit\\'+figure.name+"_"+figure.dir+"_Hit_"+figure.hit_typ+"_4.png").convert_alpha()
        figure.current_pics["Hit_5"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Hit\\'+figure.name+"_"+figure.dir+"_Hit_"+figure.hit_typ+"_5.png").convert_alpha()
    if figure.being_hitted:
        if figure.LPT + 100 < pygame.time.get_ticks(): # Hier wird daweil noch pauschal Geschwindigkeit der Hit-bewegung bestimmt! (Zahl!)
            figure.LPT = pygame.time.get_ticks()
            if not figure.hit_CPN >= 5:
                figure.hit_CPN += 1
                try:
                    figure.image = figure.current_pics["Hit_"+str(figure.hit_CPN)]
                except KeyError:
                    figure.image = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Hit\\'+figure.name+"_"+figure.dir+"_Hit_"+figure.hit_typ+"_"+str(figure.hit_CPN)+".png").convert_alpha()
                if figure.hit_CPN == 3:
                    if pygame.time.get_ticks() > figure.last_sound_played + 150:
                        z = random.choice([1,2])
                        figure.sounds["aua_"+str(z)+"_sound"].play()
                        figure.last_sound_played = pygame.time.get_ticks()
            elif figure.hit_CPN == 5:
                figure.hit_CPN += 1
                try:
                    figure.image = figure.current_pics["Hit_5"]
                except:
                    figure.image = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Hit\\'+figure.name+"_"+figure.dir+"_Hit_"+figure.hit_typ+"_5.png").convert_alpha()
            else:
                figure.hit_CPN = 0 # Vorbereitung fürs nächste Mal
                figure.image = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Fight\\'+figure.name+"_"+figure.dir+"_Fight_1.png").convert_alpha()
                figure.being_hitted = False


def die(figure):
    if not figure == Var.hero:
        folder = "Monsters\\"
    else:
        folder = ""
    if figure.start_dying:
        figure.start_dying = False
        figure.dying = True
        figure.dead = True
        figure.sounds["die_sound"].play()
        figure.current_pics.clear()
        figure.current_pics["Die_1"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Die\\'+figure.name+"_"+figure.dir+"_Die_1.png").convert_alpha()
        figure.current_pics["Die_2"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Die\\'+figure.name+"_"+figure.dir+"_Die_2.png").convert_alpha()
        figure.current_pics["Die_3"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Die\\'+figure.name+"_"+figure.dir+"_Die_3.png").convert_alpha()
        figure.current_pics["Die_4"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Die\\'+figure.name+"_"+figure.dir+"_Die_4.png").convert_alpha()
        figure.current_pics["Die_5"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Die\\'+figure.name+"_"+figure.dir+"_Die_5.png").convert_alpha()
        figure.current_pics["Die_6"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Die\\'+figure.name+"_"+figure.dir+"_Die_6.png").convert_alpha()
        figure.current_pics["Die_7"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Die\\'+figure.name+"_"+figure.dir+"_Die_7.png").convert_alpha()
        figure.current_pics["Die_8"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Die\\'+figure.name+"_"+figure.dir+"_Die_8.png").convert_alpha()
        figure.current_pics["Die_9"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Die\\'+figure.name+"_"+figure.dir+"_Die_9.png").convert_alpha()
        figure.current_pics["Die_10"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Die\\'+figure.name+"_"+figure.dir+"_Die_10.png").convert_alpha()
        figure.current_pics["Die_11"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Die\\'+figure.name+"_"+figure.dir+"_Die_11.png").convert_alpha()
        figure.current_pics["Die_12"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Die\\'+figure.name+"_"+figure.dir+"_Die_12.png").convert_alpha()
        figure.current_pics["Die_13"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Die\\'+figure.name+"_"+figure.dir+"_Die_13.png").convert_alpha()
        figure.current_pics["Die_14"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Die\\'+figure.name+"_"+figure.dir+"_Die_14.png").convert_alpha()
        figure.current_pics["Die_15"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Die\\'+figure.name+"_"+figure.dir+"_Die_15.png").convert_alpha()
        figure.current_pics["Die_16"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Die\\'+figure.name+"_"+figure.dir+"_Die_16.png").convert_alpha()
        figure.current_pics["Die_17"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Die\\'+figure.name+"_"+figure.dir+"_Die_17.png").convert_alpha()
        figure.current_pics["Die_18"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Die\\'+figure.name+"_"+figure.dir+"_Die_18.png").convert_alpha()
        figure.current_pics["Die_19"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Die\\'+figure.name+"_"+figure.dir+"_Die_19.png").convert_alpha()
        figure.current_pics["Die_20"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Die\\'+figure.name+"_"+figure.dir+"_Die_20.png").convert_alpha()
        figure.current_pics["Die_21"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Die\\'+figure.name+"_"+figure.dir+"_Die_21.png").convert_alpha()
        figure.current_pics["Die_22"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Die\\'+figure.name+"_"+figure.dir+"_Die_22.png").convert_alpha()
        figure.current_pics["Die_23"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Die\\'+figure.name+"_"+figure.dir+"_Die_23.png").convert_alpha()
        figure.current_pics["Die_24"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Die\\'+figure.name+"_"+figure.dir+"_Die_24.png").convert_alpha()
        figure.current_pics["Die_25"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Die\\'+figure.name+"_"+figure.dir+"_Die_25.png").convert_alpha()
        figure.current_pics["Die_26"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Die\\'+figure.name+"_"+figure.dir+"_Die_26.png").convert_alpha()
    if figure.dying:
        if figure.LPT + 90 < pygame.time.get_ticks(): # Hier wird die Geschwindigkeit der Sterbe-bewegung bestimmt! (Zahl!)
            figure.LPT = pygame.time.get_ticks()
            if not figure.die_CPN >= 25:
                figure.die_CPN += 1
                figure.image = figure.current_pics["Die_"+str(figure.die_CPN)]
                if figure.die_CPN == 25:
                    figure.die_CPN += 1
            elif figure.die_CPN == 26:
                if not (figure.name == "Hero"):
                    del Var.units[figure.ID]
                    Var.dead.append(basic_types.Dead(figure.name, "dead_"+figure.typ, "", figure.dir, figure.pos, transparency=0, ID=figure.ID))
                    figure.image = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\'+figure.name+"_empty.png").convert()
                    figure.image.set_colorkey([0,0,0], pygame.RLEACCEL)
                    figure.dying = False
                else:
                    Var.game_over = pygame.image.load(Var.path+"\\pics\\Game_Over.png").convert()
                    Var.game_over.set_colorkey([0,0,0], pygame.RLEACCEL)
                    Var.game_over.set_alpha(210, pygame.RLEACCEL)




def draw_button(figure):
    figure.LPT = pygame.time.get_ticks()
    if not figure == Var.hero:
        folder = "Monsters\\"
    else:
        folder = ""
    if figure.drawn:
        figure.putting_away = True
        figure.drawn = False
        try:
            figure.image = figure.current_pics["Fight_1"]
        except:
            figure.image = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Fight\\'+figure.name+"_"+figure.dir+"_Fight_1.png").convert_alpha()
        if pygame.time.get_ticks() > figure.last_sound_played + 150:
            figure.sounds["put_away_sound"].play()
            figure.last_sound_played = pygame.time.get_ticks()
    else:
        figure.drawing = True
        figure.image = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\'+figure.name+"_"+figure.dir+"_Stand.png").convert_alpha()
    figure.frameway = [0, 0]
    figure.go = False
    figure.sounds["footsteps_sound"].stop()
    figure.draw_pressed = False
    figure.current_pics.clear()
    figure.current_pics["Draw_1"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Draw\\'+figure.name+"_"+figure.dir+"_Draw_1.png").convert_alpha()
    figure.current_pics["Draw_2"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Draw\\'+figure.name+"_"+figure.dir+"_Draw_2.png").convert_alpha()
    figure.current_pics["Draw_3"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Draw\\'+figure.name+"_"+figure.dir+"_Draw_3.png").convert_alpha()
    figure.current_pics["Draw_4"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Draw\\'+figure.name+"_"+figure.dir+"_Draw_4.png").convert_alpha()
    figure.current_pics["Draw_5"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Draw\\'+figure.name+"_"+figure.dir+"_Draw_5.png").convert_alpha()
    figure.current_pics["Draw_6"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Draw\\'+figure.name+"_"+figure.dir+"_Draw_6.png").convert_alpha()
    figure.current_pics["Draw_7"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Draw\\'+figure.name+"_"+figure.dir+"_Draw_7.png").convert_alpha()
    figure.current_pics["Draw_8"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Draw\\'+figure.name+"_"+figure.dir+"_Draw_8.png").convert_alpha()
    figure.current_pics["Draw_9"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Draw\\'+figure.name+"_"+figure.dir+"_Draw_9.png").convert_alpha()
    figure.current_pics["Draw_10"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Draw\\'+figure.name+"_"+figure.dir+"_Draw_10.png").convert_alpha()
    figure.current_pics["Draw_11"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Draw\\'+figure.name+"_"+figure.dir+"_Draw_11.png").convert_alpha()
    figure.current_pics["Draw_12"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Draw\\'+figure.name+"_"+figure.dir+"_Draw_12.png").convert_alpha()
    figure.current_pics["Draw_13"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Draw\\'+figure.name+"_"+figure.dir+"_Draw_13.png").convert_alpha()
    figure.current_pics["Draw_14"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Draw\\'+figure.name+"_"+figure.dir+"_Draw_14.png").convert_alpha()
    figure.current_pics["Draw_15"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Draw\\'+figure.name+"_"+figure.dir+"_Draw_15.png").convert_alpha()

def draw(figure):
    if figure.go:
        figure.frameway = [0, 0]
        figure.go = False
        figure.sounds["footsteps_sound"].stop()
    if figure.LPT + figure.draw_TPP < pygame.time.get_ticks():
        figure.LPT = pygame.time.get_ticks()
        if not figure.draw_CPN >= 15:
            figure.draw_CPN += 1
            figure.image = figure.current_pics["Draw_"+str(figure.draw_CPN)]
            if figure.draw_CPN == 3:
                if pygame.time.get_ticks() > figure.last_sound_played + 150:
                    figure.sounds["draw_sound"].play()
                    figure.last_sound_played = pygame.time.get_ticks()
        elif figure.draw_CPN == 15:
            figure.draw_CPN += 1
            figure.image = figure.current_pics["Draw_15"]
        else:
            if not figure == Var.hero:
                folder = "Monsters\\"
            else:
                folder = ""
            figure.image = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split("_")[0]+"\\Fight\\"+figure.name+"_"+figure.dir+"_Fight_1.png").convert_alpha()
            figure.current_pics.clear()
            figure.current_pics["Fight_1"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Fight\\'+figure.name+"_"+figure.dir+"_Fight_1.png").convert_alpha()
            figure.current_pics["Fight_2"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Fight\\'+figure.name+"_"+figure.dir+"_Fight_2.png").convert_alpha()
            figure.current_pics["Fight_3"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Fight\\'+figure.name+"_"+figure.dir+"_Fight_3.png").convert_alpha()
            figure.current_pics["Fight_4"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Fight\\'+figure.name+"_"+figure.dir+"_Fight_4.png").convert_alpha()
            figure.current_pics["Fight_5"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Fight\\'+figure.name+"_"+figure.dir+"_Fight_5.png").convert_alpha()
            figure.current_pics["Fight_6"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Fight\\'+figure.name+"_"+figure.dir+"_Fight_6.png").convert_alpha()
            figure.current_pics["Fight_7"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Fight\\'+figure.name+"_"+figure.dir+"_Fight_7.png").convert_alpha()
            figure.drawing = False
            figure.drawn = True

def put_away(figure):
    if figure.go:
        figure.frameway = [0, 0]
        figure.go = False
        figure.sounds["footsteps_sound"].stop()
    if figure.LPT + figure.draw_TPP < pygame.time.get_ticks():
        figure.LPT = pygame.time.get_ticks()
        if not figure == Var.hero:
            folder = "Monsters\\"
        else:
            folder = ""
        if not figure.draw_CPN <= 1:
            figure.draw_CPN -= 1
            try:
                figure.image = figure.current_pics["Draw_"+str(figure.draw_CPN)]
            except KeyError:
                figure.image = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Draw\\'+figure.name+"_"+figure.dir+"_Draw_"+str(figure.draw_CPN)+".png").convert_alpha()
        elif figure.draw_CPN == 1:
            figure.draw_CPN -= 1
            try:
                figure.image = figure.current_pics["Draw_1"]
            except KeyError:
                figure.image = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Draw\\'+figure.name+"_"+figure.dir+"_Draw_1.png").convert_alpha()
        else:
            figure.image = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split("_")[0]+"\\"+figure.name+"_"+figure.dir+"_Stand.png").convert_alpha()
            figure.current_pics.clear()
            figure.current_pics["Stand"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\'+figure.name+"_"+figure.dir+"_Stand.png").convert_alpha()
            figure.current_pics["Go_R1"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\'+figure.name+"_"+figure.dir+"_Go_R1.png").convert_alpha()
            figure.current_pics["Go_R2"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\'+figure.name+"_"+figure.dir+"_Go_R2.png").convert_alpha()
            figure.current_pics["Go_L1"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\'+figure.name+"_"+figure.dir+"_Go_L1.png").convert_alpha()
            figure.current_pics["Go_L2"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\'+figure.name+"_"+figure.dir+"_Go_L2.png").convert_alpha()
            figure.putting_away = False


def calculate_fightpic_speeds(figure):   # TPPs werden hier "dynamisch" erstellt
    if figure.attackspeed == 1:
        figure.slash_TPP = 200
    elif figure.attackspeed == 2:
        figure.slash_TPP = 180
    elif figure.attackspeed == 3:
        figure.slash_TPP = 162
    elif figure.attackspeed == 4:
        figure.slash_TPP = 146
    elif figure.attackspeed == 5:
        figure.slash_TPP = 132
    elif figure.attackspeed == 6:
        figure.slash_TPP = 120
    elif figure.attackspeed == 7:
        figure.slash_TPP = 110
    elif figure.attackspeed == 8:
        figure.slash_TPP = 102
    elif figure.attackspeed == 9:
        figure.slash_TPP = 96
    elif figure.attackspeed == 10:
        figure.slash_TPP = 92
    if figure.defendspeed == 1:
        figure.defend_TPP = 100
    elif figure.defendspeed == 2:
        figure.defend_TPP = 90
    elif figure.defendspeed == 3:
        figure.defend_TPP = 81
    elif figure.defendspeed == 4:
        figure.defend_TPP = 73
    elif figure.defendspeed == 5:
        figure.defend_TPP = 66
    elif figure.defendspeed == 6:
        figure.defend_TPP = 60
    elif figure.defendspeed == 7:
        figure.defend_TPP = 55
    elif figure.defendspeed == 8:
        figure.defend_TPP = 51
    elif figure.defendspeed == 9:
        figure.defend_TPP = 48
    elif figure.defendspeed == 10:
        figure.defend_TPP = 46
    figure.slower_slash_TPP = (figure.slash_TPP//4)*5
    figure.normal_slash_TPP = figure.slash_TPP
    figure.faster_slash_TPP = (figure.slash_TPP//5)*4
    figure.slower_defend_TPP = (figure.defend_TPP//4)*5
    figure.normal_defend_TPP = figure.defend_TPP
    figure.faster_defend_TPP = (figure.defend_TPP//5)*4
    

    




    
