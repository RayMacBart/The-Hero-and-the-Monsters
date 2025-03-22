import pygame
from pool import Var
from pool import BS
from pool import Frames
import basic_types
import other_functions
import random


## adjust_layers(border, sprite)
## check_layer_adjust()
## mapping()
## check_decoration_blitting()
## check_border_blitting()
## check_obstacle_blitting()
## check_door_blitting()
## check_unit_blitting()
## blitorder()
## check_alphas()
## draw()


def adjust_layers(border, sprite):
    
    inpos = [sprite.realpos[0]-border.pos[0], sprite.realpos[1]-border.pos[1]]
    
    if border.name.split("_")[-1] in ["LR", "L", "R"]:
        if (inpos[1] < 82) and (inpos[1] > 14):
                sprite.layerpos[1] = border.realpos[1]-3
            
    elif border.name.split("_")[-1] in ["OR", "SE"]:
        if ((inpos[0] - inpos[1]) > 20) and ((inpos[0] - inpos[1]) < 75):
                sprite.layerpos[1] = border.realpos[1]-3
                
    elif border.name.split("_")[-1] in ["UL", "NW"]:
        if ((inpos[1] - inpos[0]) < 80) and ((inpos[1] - inpos[0]) > 25):
                sprite.layerpos[1] = border.realpos[1]-3
                
    elif border.name.split("_")[-1] in ["OL", "SW"]:
        if ((inpos[0] + inpos[1]) < 77) and ((inpos[0] + inpos[1]) > 24):
                sprite.layerpos[1] = border.realpos[1]-3
        
    elif border.name.split("_")[-1] in ["UR", "NE"]:
        if ((inpos[0] + inpos[1]) < 180) and ((inpos[0] + inpos[1]) > 124):
                sprite.layerpos[1] = border.realpos[1]-3
        
    elif (border.name.split("_")[-2:][0] + "_" + border.name.split("_")[-2:][1]) == "edge_OL":
        if ((inpos[0] < 44) and (inpos[1] < 76)) and ((inpos[1] > 12) or (inpos[0]+inpos[1] > 44)):
                sprite.layerpos[1] = border.realpos[1]-3
        
    elif (border.name.split("_")[-2:][0] + "_" + border.name.split("_")[-2:][1]) == "edge_OR":
        if ((inpos[0] > 54) and (inpos[1] < 76)) and ((inpos[1] > 12) or (inpos[0]-inpos[1] < 55)):
                sprite.layerpos[1] = border.realpos[1]-3

    elif (border.name.split("_")[-2:][0] + "_" + border.name.split("_")[-2:][1]) == "edge_UL":
        if (not ((inpos[0] < 44) and (inpos[1] > 82))) and \
           ((inpos[0] < 60) and (inpos[1] > 14) and (inpos[0]-inpos[1] < 21) and (inpos[0]-(inpos[1]/3) < 41)):
            sprite.layerpos[1] = border.realpos[1]-3
        
    elif (border.name.split("_")[-2:][0] + "_" + border.name.split("_")[-2:][1]) == "edge_UR":
        if (not((inpos[0] > 56) and (inpos[1] > 82))) and \
           ((inpos[0] > 40) and (inpos[1] > 14) and (inpos[0]+inpos[1] > 78) and ((inpos[0]*3)+inpos[1] > 174)):
            sprite.layerpos[1] = border.realpos[1]-3
        
    elif (border.name.split("_")[-1] == "LR-OL"):
        if ((inpos[0]+inpos[1] < 172) and (inpos[1] < 75)) and ((inpos[1] > 14) or (inpos[0]+(inpos[1]*2) > 121)):
                sprite.layerpos[1] = border.realpos[1]-3
        
    elif (border.name.split("_")[-1] == "LR-UL"):
        if (not((inpos[0]-inpos[1] < 16) and (inpos[1] > 81))) and \
           ((inpos[1] > 14) and ((inpos[0]/3)-inpos[1] < 5) and \
            ((inpos[0]/2)-inpos[1] < 19) and (inpos[0]-inpos[1] < 75)):
            sprite.layerpos[1] = border.realpos[1]-3
        
    elif (border.name.split("_")[-1] == "OR-LR"):
        if ((inpos[0]-inpos[1] > 27) and (inpos[1] < 75)) and (((inpos[0]/2)-inpos[1] < 39) or (inpos[1] > 14)):
                sprite.layerpos[1] = border.realpos[1]-3
        
    elif (border.name.split("_")[-1] == "UR-LR"):
        if (not((inpos[0]+inpos[1] > 186) and (inpos[1] > 81))) and \
           ((inpos[0]+inpos[1] > 124) and (inpos[0]+(inpos[1]*2) > 161) and \
            (inpos[0]+(inpos[1]*3) > 184) and (inpos[1] > 14)):
            sprite.layerpos[1] = border.realpos[1]-3
        
    elif (border.name.split("_")[-1] == "OU-OL"):
        if ((inpos[0]+inpos[1] < 175) and (inpos[0] < 46)) and \
           (((inpos[1] > 41) and (inpos[0] > 36)) or ((inpos[0]*2)+inpos[1] > 145) or (inpos[0]+inpos[1] > 124)):
                sprite.layerpos[1] = border.realpos[1]-3
        
    elif (border.name.split("_")[-1] == "OU-OR"):
        if ((inpos[1]-inpos[0] < 77) and (inpos[0] > 54)) and \
           (((inpos[1] > 41) and (inpos[0] < 63)) or (inpos[0]-(inpos[1]/2) < 27) or (inpos[1]-inpos[0] > 25)):
                sprite.layerpos[1] = border.realpos[1]-3
        
    elif (border.name.split("_")[-1] == "UL-OU"):
        if (not((inpos[1]-inpos[0] > 78) and (inpos[0] < 45))) and \
           ((inpos[1]-inpos[0] > 25) and (inpos[0]-(inpos[1]/2) < 8) and \
            (inpos[0]-(inpos[1]/3) < 22) and (inpos[0] < 60)):
            sprite.layerpos[1] = border.realpos[1]-3
        
    elif (border.name.split("_")[-1] == "UR-OU"):
        if (not((inpos[0]+inpos[1] > 180) and (inpos[0] > 53))) and \
           ((inpos[0] > 39) and ((inpos[0]*3)+inpos[1] > 232) and \
            ((inpos[0]*2)+inpos[1] > 182) and (inpos[0]+inpos[1] > 124)):
            sprite.layerpos[1] = border.realpos[1]-3
        
    elif (border.name.split("_")[-2:][0] + "_" + border.name.split("_")[-2:][1]) == "edge_R":
        if (((inpos[0]+inpos[1] < 178) and (inpos[0]+inpos[1] > 124)) or \
           ((inpos[0]-inpos[1] > 20) and (inpos[0]-inpos[1] < 75))):
            sprite.layerpos[1] = border.realpos[1]-3
            
    elif (border.name.split("_")[-2:][0] + "_" + border.name.split("_")[-2:][1]) == "edge_L":
        if (((inpos[1]-inpos[0] < 79) and (inpos[1]-inpos[0] > 25)) or \
           ((inpos[0]+inpos[1] < 79) and (inpos[0]+inpos[1] > 24))):
            sprite.layerpos[1] = border.realpos[1]-3

    elif (border.name.split("_")[-1] == "OR-UL"):   # betrifft nur Door-Objekte!
        if (inpos[0]-inpos[1]) < 0 or (inpos[0]-inpos[1]) > 86:
            border.layerpos[1] = border.pos[1]
            if sprite.layerpos[1] < border.layerpos[1]:
                sprite.layerpos[1] = border.layerpos[1]+3
        elif sprite.layerpos[1] > border.layerpos[1]:
            sprite.layerpos[1] = border.layerpos[1]-3

    elif (border.name.split("_")[-1] == "UR-OL"):   # betrifft auch nur Door-Objekte!
        if (inpos[0]+inpos[1]) > 200 or (inpos[0]+inpos[1]) < 113:
            border.realpos[1] = border.pos[1]
            if sprite.layerpos[1] < border.realpos[1]:
                sprite.layerpos[1] = border.realpos[1]+3
        elif sprite.layerpos[1] > border.realpos[1]:
            sprite.layerpos[1] = border.realpos[1]-3


def check_layer_adjust():
    
    for b in Var.borders.values():
        for d in Var.decorations.values():
            if ((b.pos[0] <= d.realpos[0]) and (b.pos[0]+b.width > d.realpos[0])) and \
               ((b.pos[1] <= d.realpos[1]) and (b.pos[1]+b.height > d.realpos[1])):
                adjust_layers(b, d)
        for ad in Var.animated_decorations.values():
            if ((b.pos[0] <= ad.realpos[0]) and (b.pos[0]+b.width > ad.realpos[0])) and \
               ((b.pos[1] <= ad.realpos[1]) and (b.pos[1]+b.height > ad.realpos[1])):
                adjust_layers(b, ad)
        for o in Var.obstacles.values():
            if ((b.pos[0] <= o.realpos[0]) and (b.pos[0]+b.width > o.realpos[0])) and \
               ((b.pos[1] <= o.realpos[1]) and (b.pos[1]+b.height > o.realpos[1])):
                adjust_layers(b, o)
        for ao in Var.animated_obstacles.values():
            if ((b.pos[0] <= ao.realpos[0]) and (b.pos[0]+b.width > ao.realpos[0])) and \
               ((b.pos[1] <= ao.realpos[1]) and (b.pos[1]+b.height > ao.realpos[1])):
                adjust_layers(b, ao)

    for do in Var.doors.values():
        for d in Var.decorations.values():
            if ((do.pos[0] <= d.realpos[0]) and (do.pos[0]+do.width > d.realpos[0])) and \
               ((do.pos[1] <= d.realpos[1]) and (do.pos[1]+do.height > d.realpos[1])):
                adjust_layers(do, d)
        for ad in Var.animated_decorations.values():
            if ((do.pos[0] <= ad.realpos[0]) and (do.pos[0]+do.width > ad.realpos[0])) and \
               ((do.pos[1] <= ad.realpos[1]) and (do.pos[1]+do.height > ad.realpos[1])):
                adjust_layers(do, ad)
        for o in Var.obstacles.values():
            if ((do.pos[0] <= o.realpos[0]) and (do.pos[0]+do.width > o.realpos[0])) and \
               ((do.pos[1] <= o.realpos[1]) and (do.pos[1]+do.height > o.realpos[1])):
                adjust_layers(do, o)
        for ao in Var.animated_obstacles.values():
            if ((do.pos[0] <= ao.realpos[0]) and (do.pos[0]+do.width > ao.realpos[0])) and \
               ((do.pos[1] <= ao.realpos[1]) and (do.pos[1]+do.height > ao.realpos[1])):
                adjust_layers(do, ao)





def mapping():
    if Var.hero.go or Var.screen_scrolling_happened:
        x_mapset = set()   # in einem set kann ein Wert nur 1x vorkommen! Problem bei Liste war, dass immer mehrere (2-3) Fliesen die gleichen x- und y-werte haben und unten die Objekte entsprechend mehrfach in Var.current_blitmaps erzeugt wurden!
        y_mapset = set()
        for cbm in Var.current_blitmaps:
            x_mapset.add(cbm.pos[0])
            y_mapset.add(cbm.pos[1])
        if min(x_mapset) > 0:
            for y in y_mapset:
                Var.current_blitmaps.append(basic_types.Basic(Var.main_background, "", [min(x_mapset)-320, y]))
        if max(x_mapset) < 320:
            for y in y_mapset:
                Var.current_blitmaps.append(basic_types.Basic(Var.main_background, "", [max(x_mapset)+320, y]))
        if min(y_mapset) > 0:
            for x in x_mapset:
                Var.current_blitmaps.append(basic_types.Basic(Var.main_background, "", [x, min(y_mapset)-200]))
        if max(y_mapset) < 200:
            for x in x_mapset:
                Var.current_blitmaps.append(basic_types.Basic(Var.main_background, "", [x, max(y_mapset)+200]))

        if (min(x_mapset) > 0) and (min(y_mapset) > 0):
            Var.current_blitmaps.append(basic_types.Basic(Var.main_background, "", [min(x_mapset)-320, min(y_mapset)-200]))
        if (min(x_mapset) > 0) and (max(y_mapset) < 200):
            Var.current_blitmaps.append(basic_types.Basic(Var.main_background, "", [min(x_mapset)-320, max(y_mapset)+200]))
        if (max(x_mapset) < 320) and (min(y_mapset) > 0):
            Var.current_blitmaps.append(basic_types.Basic(Var.main_background, "", [max(x_mapset)+320, min(y_mapset)-200]))
        if (max(x_mapset) < 320) and (max(y_mapset) < 200):
            Var.current_blitmaps.append(basic_types.Basic(Var.main_background, "", [max(x_mapset)+320, max(y_mapset)+200]))

        for cbm in Var.current_blitmaps:
            if cbm.pos[0] < -320:
                Var.current_blitmaps.remove(cbm)
            if cbm.pos[0] > 640:
                Var.current_blitmaps.remove(cbm)
            if (cbm.pos[1] < -200) and (cbm in Var.current_blitmaps):   #
                Var.current_blitmaps.remove(cbm)                        # Fehlervorbeugungsmaßnahme: Falls x & y genau gleichzeitig aus dem Bild geht!
            if (cbm.pos[1] > 400) and (cbm in Var.current_blitmaps):    #  
                Var.current_blitmaps.remove(cbm)
        if Var.screen_scrolling_happened:
            Var.screen_scrolling_happened = False


def check_decoration_blitting():
    for d in Var.decorations.values():
        if ((((d.pos[0]+d.width) > 0) and (d.pos[0] < 640)) and (((d.pos[1]+d.height) > 0) and (d.pos[1] < 400))):
            if not (d in Var.blitlist):
                Var.blitlist.append(d)
        else:
            if (d in Var.blitlist):
                Var.blitlist.remove(d)
    for ad in Var.animated_decorations.values():
        if ((((ad.pos[0]+ad.width) > 0) and (ad.pos[0] < 640)) and (((ad.pos[1]+ad.height) > 0) and (ad.pos[1] < 400))):
            if not (ad in Var.blitlist):
                Var.blitlist.append(ad)
        else:
            if (ad in Var.blitlist):
                Var.blitlist.remove(ad)


                
def check_border_blitting():
    for b in Var.borders.values():
        if ((((b.pos[0]+b.width) > 0) and (b.pos[0] < 640)) and (((b.pos[1]+b.height) > 0) and (b.pos[1] < 400))):
            if not (b in Var.blitlist):
                Var.blitlist.append(b)
        else:
            if (b in Var.blitlist):
                Var.blitlist.remove(b)



def check_obstacle_blitting():
    for o in Var.obstacles.values():
        if ((((o.pos[0]+o.width) > 0) and (o.pos[0] < 640)) and (((o.pos[1]+o.height) > 0) and (o.pos[1] < 400))):
            if not (o in Var.blitlist):
                Var.blitlist.append(o)
        else:
            if (o in Var.blitlist):
                Var.blitlist.remove(o)
    for ao in Var.animated_obstacles.values():
        if ((((ao.pos[0]+ao.width) > 0) and (ao.pos[0] < 640)) and (((ao.pos[1]+ao.height) > 0) and (ao.pos[1] < 400))):
            if not (ao in Var.blitlist):
                Var.blitlist.append(ao)
        else:
            if (ao in Var.blitlist):
                Var.blitlist.remove(ao)


def check_door_blitting():
    for do in Var.doors.values():
        if ((((do.pos[0]+do.width) > 0) and (do.pos[0] < 640)) and (((do.pos[1]+do.height) > 0) and (do.pos[1] < 400))):
            if not (do in Var.blitlist):
                Var.blitlist.append(do)
            if (("OU" in do.name) and (do.status == "open") and (not do.blitcopydone) and (not do.I_am_doorcopy)):
                do.layerpos[1] = do.pos[1]
                do.doorcopy = basic_types.Door(do.name, do.typ, do.pos, [do.realpos[0]-do.pos[0], do.realpos[1]-do.pos[1]], do.quantity, do.rate_duration)
                do.doorcopy.status = "open"
                do.doorcopy.current_pic = 6
                do.doorcopy.images[6] = pygame.image.load(Var.path+'\\pics\\Objects\\'+do.name.split('_')[0]+'\\'+do.name+'_'+do.dir+'-'+str(6)+'V.png').convert()
                do.doorcopy.images[6].set_colorkey([0,0,0], pygame.RLEACCEL)
                do.doorcopy.images[6].set_alpha(do.transparency, pygame.RLEACCEL)
                do.doorcopy.layerpos[1] = do.pos[1]+do.height
                Var.blitlist.append(do.doorcopy)
                do.blitcopydone = True
                do.doorcopy.I_am_doorcopy = True
            elif (("OU" in do.name) and ((do.status == "closed") or (do.status == "closing")) and (do.blitcopydone)):
                if do.doorcopy in Var.blitlist:
                    Var.blitlist.remove(do.doorcopy)
                do.doorcopy = 0
                do.blitcopydone = False
        else:
            if (do in Var.blitlist):
                Var.blitlist.remove(do)
            if do.doorcopy in Var.blitlist:
                Var.blitlist.remove(do.doorcopy)
                do.doorcopy = 0
                do.blitcopydone = False

                
def check_unit_blitting():
    for u in Var.units.values():
        if ((((u.pos[0]+u.width) > 0) and (u.pos[0] < 640)) and (((u.pos[1]+u.height) > 0) and (u.pos[1] < 400))):
            if not (u in Var.blitlist):
                Var.blitlist.append(u)
        else:
            if (u in Var.blitlist):
                Var.blitlist.remove(u)


def blitorder():   
#Ebenendarstellung: Die surfaces und positions der Elemente von blitlist werden geordnet auf sorted_blitlist übertragen
    for b in Var.blitlist:
        if type(b) is basic_types.Inclined_high_obstacle:
            if Var.hero.realpos[0] <= b.pos[0]+b.x_offset:
                b.realpos[1] = b.pos[1]+b.L_y_offset
            else:
                b.realpos[1] = b.pos[1]+b.R_y_offset
                
    y_positions = []
    for b in Var.blitlist:
        y_positions.append(b.layerpos[1])
    y_positions.sort()
    
    while y_positions:
        for b in Var.blitlist:
            if y_positions:
                if (b.layerpos[1] == y_positions[0]):
##                if ((((issubclass(type(b), basic_types.Character)) or (type(b) == basic_types.Character)) and (b.layerpos[1] == y_positions[0])) or \
##                   ((not((issubclass(type(b), basic_types.Character)) or (type(b) == basic_types.Character))) and (b.realpos[1] == y_positions[0]))):

                    if (type(b) is basic_types.High_obstacle) or (type(b) is basic_types.Inclined_high_obstacle) or \
                       (type(b) is basic_types.High_border):
                        if b.transparent == True:
                            Var.sorted_blitlist.append((b.image_shiny, b.pos))
                        else:
                            Var.sorted_blitlist.append((b.image, b.pos))
                            
                    elif (type(b) is basic_types.Animated_high_obstacle):
                        if b.chaos and b.blit_now:
                            b.current_pic = random.randrange(1, b.quantity+1)
                            b.blit_now = False
                        if b.transparent == True:
                            Var.sorted_blitlist.append((b.images_shiny[b.current_pic], b.pos))
                        Var.sorted_blitlist.append((b.images[b.current_pic], b.pos))
                    elif (type(b) is basic_types.Door):
                        if b.blit_now:
                            b.blit_now = False
                        Var.sorted_blitlist.append((b.images[b.current_pic], b.pos))
                    else:
                        if b.typ[:8] == "Animated":
                            if b.chaos and b.blit_now:
                                cp = b.current_pic
                                while True:
                                    b.current_pic = random.randrange(1, b.quantity+1)
                                    if b.current_pic == cp:
                                        continue
                                    else:
                                        break
                                b.blit_now = False
                            Var.sorted_blitlist.append((b.images[b.current_pic], b.pos))
                        else:
                            Var.sorted_blitlist.append((b.image, b.pos)) # = Zeile der meisten blits!
                    del y_positions[0]




def check_alphas():
    for b in Var.blitlist:
        if (type(b) is basic_types.High_obstacle) or (type(b) is basic_types.Inclined_high_obstacle):
            if ((b.pos[0] < Var.hero.realpos[0]) and (b.pos[0]+b.width > Var.hero.realpos[0])) and \
               ((b.pos[1] < Var.hero.realpos[1]) and (b.realpos[1] > Var.hero.realpos[1])):
                if b.transparent == False:
                    b.transparent = True
            else:
                if b.transparent == True:
                    b.transparent = False
            for u in Var.units.values():
                if u.name == "Hero":
                    if ((b.pos[0] < u.realpos[0]) and (b.pos[0]+b.width > u.realpos[0])) and \
                       ((b.pos[1] < u.realpos[1]) and (b.realpos[1] > u.realpos[1])):
                        if b.transparent == False:
                            b.transparent = True
                    else:
                        if b.transparent == True:
                            b.transparent = False
        elif (type(b) is basic_types.High_border):
            if ((b.pos[0] < Var.hero.realpos[0]) and (b.pos[0]+b.width > Var.hero.realpos[0])) and ((b.pos[1] < Var.hero.realpos[1]) and (b.pos[1]+b.height > Var.hero.realpos[1])):
                other_functions.check_border_transparence(b, Var.hero)
            elif b.transparent:
                b.transparent = False
            for u in Var.units.values():
                if u.name == "Hero":
                    if ((b.pos[0] < u.realpos[0]) and (b.pos[0]+b.width > u.realpos[0])) and \
                       ((b.pos[1] < u.realpos[1]) and (b.pos[1]+b.height > u.realpos[1])):
                        other_functions.check_border_transparence(b, u)
                    elif b.transparent:
                        b.transparent = False

            
def draw_BS():
    for e in Var.fight.enemies:
##        Falls nötig:  nur jene in der "keep_fighting-range", die also angreifbar sind.
##        if int(math.sqrt((((abs(e.realpos[0]-Var.fight.hero.realpos[0])**2)//4)*3) + \
##                         (abs(e.realpos[1]-Var.fight.hero.realpos[1])**2))) <= 82:

        if Var.fight.current_turn == "hero":
            if Var.fight.hero.flow:
                Var.screen.blit(BS.x_hero, [e.realpos[0]-24,e.realpos[1]-100])
            else:
                Var.screen.blit(BS.o_hero, [e.realpos[0]-24,e.realpos[1]-100])

        elif Var.fight.enemy_flowing:
            if e.flow:
                Var.screen.blit(BS.enemy_flow, [e.realpos[0]-24,e.realpos[1]-100])
            else:
                Var.screen.blit(BS.o_enemy, [e.realpos[0]-24,e.realpos[1]-100])
        else:
            Var.screen.blit(BS.x_enemy, [e.realpos[0]-24,e.realpos[1]-100])
        
        
        
        if not (Var.fight.current_turn == "hero" and not Var.fight.hero.flow) and not Var.fight.enemy_flowing:
            if e.sword_up_BS:
                Var.screen.blit(BS.sword_O, [e.realpos[0]-24,e.realpos[1]-100])
            if e.sword_right_BS:
                Var.screen.blit(BS.sword_R, [e.realpos[0]-24,e.realpos[1]-100])
            if e.sword_down_BS:
                Var.screen.blit(BS.sword_U, [e.realpos[0]-24,e.realpos[1]-100])
            if e.sword_left_BS:
                Var.screen.blit(BS.sword_L, [e.realpos[0]-24,e.realpos[1]-100])
            
            if e.next_up_CBS == 1:
                Var.screen.blit(BS.shield_O1, [e.realpos[0]-24,e.realpos[1]-100])
                Var.screen.blit(BS.shield_makeup_O1, [e.realpos[0]-24,e.realpos[1]-100])
            elif e.next_up_CBS == 2:
                Var.screen.blit(BS.shield_O2, [e.realpos[0]-24,e.realpos[1]-100])
                Var.screen.blit(BS.shield_makeup_O2, [e.realpos[0]-24,e.realpos[1]-100])
            elif e.next_up_CBS == 3:
                Var.screen.blit(BS.shield_O3, [e.realpos[0]-24,e.realpos[1]-100])
                Var.screen.blit(BS.shield_makeup_O3, [e.realpos[0]-24,e.realpos[1]-100])
            if e.next_right_CBS == 1:
                Var.screen.blit(BS.shield_R1, [e.realpos[0]-24,e.realpos[1]-100])
                Var.screen.blit(BS.shield_makeup_R1, [e.realpos[0]-24,e.realpos[1]-100])
            elif e.next_right_CBS == 2:
                Var.screen.blit(BS.shield_R2, [e.realpos[0]-24,e.realpos[1]-100])
                Var.screen.blit(BS.shield_makeup_R2, [e.realpos[0]-24,e.realpos[1]-100])
            elif e.next_right_CBS == 3:
                Var.screen.blit(BS.shield_R3, [e.realpos[0]-24,e.realpos[1]-100])
                Var.screen.blit(BS.shield_makeup_R3, [e.realpos[0]-24,e.realpos[1]-100])
            if e.next_down_CBS == 1:
                Var.screen.blit(BS.shield_U1, [e.realpos[0]-24,e.realpos[1]-100])
                Var.screen.blit(BS.shield_makeup_U1, [e.realpos[0]-24,e.realpos[1]-100])
            elif e.next_down_CBS == 2:
                Var.screen.blit(BS.shield_U2, [e.realpos[0]-24,e.realpos[1]-100])
                Var.screen.blit(BS.shield_makeup_U2, [e.realpos[0]-24,e.realpos[1]-100])
            elif e.next_down_CBS == 3:
                Var.screen.blit(BS.shield_U3, [e.realpos[0]-24,e.realpos[1]-100])
                Var.screen.blit(BS.shield_makeup_U3, [e.realpos[0]-24,e.realpos[1]-100])
            if e.next_left_CBS == 1:
                Var.screen.blit(BS.shield_L1, [e.realpos[0]-24,e.realpos[1]-100])
                Var.screen.blit(BS.shield_makeup_L1, [e.realpos[0]-24,e.realpos[1]-100])
            elif e.next_left_CBS == 2:
                Var.screen.blit(BS.shield_L2, [e.realpos[0]-24,e.realpos[1]-100])
                Var.screen.blit(BS.shield_makeup_L2, [e.realpos[0]-24,e.realpos[1]-100])
            elif e.next_left_CBS == 3:
                Var.screen.blit(BS.shield_L3, [e.realpos[0]-24,e.realpos[1]-100])
                Var.screen.blit(BS.shield_makeup_L3, [e.realpos[0]-24,e.realpos[1]-100])
    
        

		
def draw():
    mapping()
    for cbm in Var.current_blitmaps:
        Var.screen.blit(cbm.image, cbm.pos)
    check_decoration_blitting()
    check_border_blitting()
    check_obstacle_blitting()
    check_door_blitting()
    check_unit_blitting()
    blitorder()
    check_alphas()
    for bg in Var.backgrounds.values():
        if ((((bg.pos[0]+bg.width) > 0) and (bg.pos[0] < 640)) and (((bg.pos[1]+bg.height) > 0) and (bg.pos[1] < 400))):
            Var.screen.blit(bg.image, bg.pos)
            
    for abg in Var.animated_backgrounds.values():
        if ((((abg.pos[0]+abg.width) > 0) and (abg.pos[0] < 640)) and (((abg.pos[1]+abg.height) > 0) and (abg.pos[1] < 400))):
            if abg.name == "Water":
                for i in range(5):
                    Var.screen.blit(abg.images[(abg.current_pic+i if abg.quantity >= abg.current_pic+i else abg.quantity-abg.current_pic+(i if i > 0 else 1))], [abg.pos[0], abg.pos[1]+(i*20)])
                    Var.screen.blit(abg.images[(abg.current_pic+abg.quantity//4+i if abg.quantity >= abg.current_pic+abg.quantity//4+i else abg.quantity-abg.current_pic+(i if i > 0 else 1))], [abg.pos[0]+50, abg.pos[1]+(i*20)])
            else:
                if abg.chaos and abg.blit_now:
                    cp = abg.current_pic
                    while True:
                        abg.current_pic = random.randrange(1, abg.quantity+1)
                        if abg.current_pic == cp:
                            continue
                        else:
                            break
                    abg.blit_now = False
                Var.screen.blit(abg.images[abg.current_pic], abg.pos)

    for g in Var.grounds.values():
        if ((((g.pos[0]+g.width) > 0) and (g.pos[0] < 640)) and (((g.pos[1]+g.height) > 0) and (g.pos[1] < 400))):
            Var.screen.blit(g.image, g.pos)

    for d in Var.dead:  #=Liste
        Var.screen.blit(d.image, d.pos)
        
    for u in Var.units.values():
        if u.marker_active:
            Var.screen.blit(u.marker, [u.pos[0]+126, u.pos[1]+98])
        if u.defmarker_alpha:
            Var.screen.blit(u.defmarker, [u.pos[0]+126, u.pos[1]+98])
            u.defmarker_alpha -= 2
            u.defmarker.set_alpha(u.defmarker_alpha, pygame.RLEACCEL)
        if u.attackmarker_alpha:
            Var.screen.blit(u.attackmarker, [u.pos[0]+126, u.pos[1]+98])
            u.attackmarker_alpha -= 2
            u.attackmarker.set_alpha(u.attackmarker_alpha, pygame.RLEACCEL)

        
    # ERKLÄRUNG: Backgrounds sind IMMER unterster Layer und dann kommen die Toten und Marker.
    # darum erst jetzt blitting anhand sorted_blitlist aus blitorder.
    for b in Var.sorted_blitlist:
        Var.screen.blit(b[0], b[1])
    # und danach die overlays extra, die IMMER oberster Layer sind!


    del Var.sorted_blitlist[:]

    if Var.go_point["active"]:
        Var.screen.blit(Var.go_point["images"][Var.go_point["CPN"]], Var.go_point["pos"])


    if Var.hero.fighting:
        draw_BS()
    
    
    for ov in Var.overlays.values():
        if ((((ov.pos[0]+ov.width) > 0) and (ov.pos[0] < 640)) and (((ov.pos[1]+ov.height) > 0) and (ov.pos[1] < 400))):
            Var.screen.blit(ov.image, ov.pos)
    for aov in Var.animated_overlays.values():
        if ((((aov.pos[0]+aov.width) > 0) and (aov.pos[0] < 640)) and (((aov.pos[1]+aov.height) > 0) and (aov.pos[1] < 400))):
            if aov.chaos and aov.blit_now:
                cp = aov.current_pic
                while True:
                    aov.current_pic = random.randrange(1, aov.quantity+1)
                    if aov.current_pic == cp:
                        continue
                    else:
                        break
                aov.blit_now = False
            Var.screen.blit(aov.images[aov.current_pic], aov.pos)

    for u in Var.units.values():
        if u in Var.blitlist:
            Var.screen.blit(u.lifebar, [u.pos[0]+u.lifebar_pos_offset[0], u.pos[1]+u.lifebar_pos_offset[1]])

    Var.screen.blit(Var.hero.lifebar, [0,5])

    if (Frames.redframing or Var.start_redframe) and Frames.redframe_CPN:
        Var.screen.blit(Frames.redframes[Frames.redframe_CPN-1], [0,0])
    
    if Var.game_over:
        Var.screen.blit(Var.game_over, [155,145])
    
    
    pygame.display.flip()


