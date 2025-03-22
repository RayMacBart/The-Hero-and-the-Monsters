import pygame
from pool import Var
from pool import Frames


## check_border_transparence(border, unit)
## check_current_animation_pic(ani)
## go_point_animation()
## handle_marker_animation()
## check_dead()
## magnet(A, B, speed=1)
## drift_apart(A, B, speed=1)


def check_border_transparence(border, unit):
    
    inpos = [unit.realpos[0]-border.pos[0], unit.realpos[1]-border.pos[1]]
    
    if (border.name.split("_")[-1] in ["LR", "E", "W"]) or \
       (border.name.split("_")[-2:][0] + "_" + border.name.split("_")[-2:][1]) in \
       ["+_C", "+_N", "+_E", "+_S", "+_W"]:
        if (inpos[1] < 78) and (inpos[1] > 25):
            if not border.transparent:
                border.transparent = True
        else:
            if border.transparent:
                border.transparent = False
    elif border.name.split("_")[-1] in ["OR", "SE"]:
        if ((inpos[0] - inpos[1]) > 20) and ((inpos[0] - inpos[1]) < 66): 
            if not border.transparent:
                border.transparent = True
        else:
            if border.transparent:
                border.transparent = False
    elif border.name.split("_")[-1] in ["UL", "NW"]:
        if ((inpos[1] - inpos[0]) < 80) and ((inpos[1] - inpos[0]) > 35):
            if not border.transparent:
                border.transparent = True
        else:
            if border.transparent:
                border.transparent = False
    elif border.name.split("_")[-1] in ["OL", "SW"]:
        if ((inpos[0] + inpos[1]) < 77) and ((inpos[0] + inpos[1]) > 33):
            if not border.transparent:
                border.transparent = True
        else:
            if border.transparent:
                border.transparent = False
    elif border.name.split("_")[-1] in ["UR", "NE"]:
        if ((inpos[0] + inpos[1]) < 180) and ((inpos[0] + inpos[1]) > 135):
            if not border.transparent:
                border.transparent = True    
        else:                                
            if border.transparent:           
                border.transparent = False   
    elif (border.name.split("_")[-2:][0] + "_" + border.name.split("_")[-2:][1]) == "edge_OL":
        if ((inpos[0] < 44) and (inpos[1] > 25) and (inpos[1] < 76)):
            if not border.transparent:
                border.transparent = True
        else:
            if border.transparent:
                border.transparent = False
    elif (border.name.split("_")[-2:][0] + "_" + border.name.split("_")[-2:][1]) == "edge_OR":
        if ((inpos[0] > 54) and (inpos[1] > 25) and (inpos[1] < 76)):
            if not border.transparent:
                border.transparent = True
        else:
            if border.transparent:
                border.transparent = False
    elif (border.name.split("_")[-2:][0] + "_" + border.name.split("_")[-2:][1]) == "edge_UL":
        if ((inpos[0] < 60) and (inpos[1] > 25) and (inpos[1] < 82) and \
            (inpos[0]-inpos[1] < 21) and (inpos[0]-(inpos[1]/3) < 41)):
            if not border.transparent:
                border.transparent = True
        else:
            if border.transparent:
                border.transparent = False
    elif (border.name.split("_")[-2:][0] + "_" + border.name.split("_")[-2:][1]) == "edge_UR":
        if ((inpos[0] > 40) and (inpos[1] > 25) and (inpos[1] < 82) and \
            (inpos[0]+inpos[1] > 78) and ((inpos[0]*3)+inpos[1] > 174)):
            if not border.transparent:
                border.transparent = True
        else:
            if border.transparent:
                border.transparent = False
    elif (border.name.split("_")[-1] == "LR-OL"):
        if (((inpos[0]+inpos[1] < 172)) and ((inpos[1] > 25) and (inpos[1] < 75))):
            if not border.transparent:
                border.transparent = True
        else:
            if border.transparent:
                border.transparent = False    
    elif (border.name.split("_")[-1] == "LR-UL"):
        if ((inpos[0] > 97) and(inpos[0]-inpos[1] > 16) and (inpos[0]-inpos[1] < 63)) or \
            ((inpos[0] <= 97) and (inpos[1] < 81) and (inpos[1] > 25)):
            if not border.transparent:
                border.transparent = True
        else:
            if border.transparent:
                border.transparent = False
    elif (border.name.split("_")[-1] == "OR-LR"):
        if (((inpos[0]-inpos[1] > 27)) and ((inpos[1] > 25) and (inpos[1] < 75))):
            if not border.transparent:
                border.transparent = True
        else:
            if border.transparent:
                border.transparent = False
    elif (border.name.split("_")[-1] == "UR-LR"):
        if ((inpos[0] < 105) and (inpos[0]+inpos[1] < 186) and (inpos[0]+inpos[1] > 135)) or \
            ((inpos[0] >= 105 ) and (inpos[1] > 25) and (inpos[1] < 81)):
            if not border.transparent:
                border.transparent = True
        else:
            if border.transparent:
                border.transparent = False
    elif (border.name.split("_")[-1] == "OU-OL"):
        if ((inpos[0]+inpos[1] < 175) and (inpos[0]+inpos[1] > 128) and (inpos[0] < 46)):
            if not border.transparent:
                border.transparent = True
        else:
            if border.transparent:
                border.transparent = False
    elif (border.name.split("_")[-1] == "OU-OR"):
        if ((inpos[1]-inpos[0] < 77) and (inpos[1]-inpos[0] > 36) and (inpos[0] > 54)):
            if not border.transparent:
                border.transparent = True
        else:
            if border.transparent:
                border.transparent = False
    elif (border.name.split("_")[-1] == "UL-OU"):
        if ((inpos[1]-inpos[0] < 78) and (inpos[1]-inpos[0] > 36) and (inpos[0] < 45)):
            if not border.transparent:
                border.transparent = True
        else:
            if border.transparent:
                border.transparent = False
    elif (border.name.split("_")[-1] == "UR-OU"):
        if ((inpos[0]+inpos[1] < 180) and (inpos[0]+inpos[1] > 136) and (inpos[0] > 53)):
            if not border.transparent:
                border.transparent = True
        else:
            if border.transparent:
                border.transparent = False
    elif (border.name.split("_")[-2:][0] + "_" + border.name.split("_")[-2:][1]) in ["edge_R", "X_R"]:
        if (((inpos[1] < 79) and (inpos[0]-inpos[1] > 20) and (inpos[0]-inpos[1] < 64)) or \
            ((inpos[1] >= 79) and (inpos[0]+inpos[1] > 135) and (inpos[0]+inpos[1] < 178))):
            if not border.transparent:
                border.transparent = True
        else:
            if border.transparent:
                border.transparent = False
    elif (border.name.split("_")[-2:][0] + "_" + border.name.split("_")[-2:][1]) in ["edge_L", "X_L"]:
        if (((inpos[1] < 79) and (inpos[0]+inpos[1] > 35) and (inpos[0]+inpos[1] < 78)) or \
            ((inpos[1] >= 79) and (inpos[1]-inpos[0] < 79) and (inpos[1]-inpos[0] > 36))):
            if not border.transparent:
                border.transparent = True
        else:
            if border.transparent:
                border.transparent = False



def check_current_animation_pic(ani):
    if ani.last_pictime + ani.rate_duration < pygame.time.get_ticks():
        ani.last_pictime = pygame.time.get_ticks()
        ani.current_pic = 1 if (ani.current_pic == ani.quantity) else (ani.current_pic + 1)
        ani.blit_now = True

def go_point_animation():
    if Var.go_point["start"]:
        Var.go_point["active"] = True
        Var.go_point["CPN"] = 1
        Var.go_point["LPT"] = pygame.time.get_ticks()
        Var.go_point["start"] = False
    if Var.go_point["LPT"]+Var.go_point["TPP"] < pygame.time.get_ticks():
        if Var.go_point["CPN"] < 8:
            Var.go_point["CPN"] += 1
            Var.go_point["LPT"] = pygame.time.get_ticks()
        else:
            Var.go_point["active"] = False

            
def handle_marker_animation():
    for u in Var.units.values(): ### Marker ###
        try:
            if u.click_mask.get_at([Var.mouse_pos[0]-u.pos[0], Var.mouse_pos[1]-u.pos[1]]):
                if not u.marker_active:
                    u.marker_active = True
                if not u.marker_alpha >= 20:
                    if not (u.defmarker_alpha or u.attackmarker_alpha):
                        u.marker_alpha += 2
                        u.marker.set_alpha(u.marker_alpha, pygame.RLEACCEL)
                    elif (u.defmarker_alpha or u.attackmarker_alpha) < 20:
                        u.marker_alpha += 1
                        u.marker.set_alpha(u.marker_alpha, pygame.RLEACCEL)
            elif not u.marker_alpha == 0:
                u.marker_alpha -= 1
                u.marker.set_alpha(u.marker_alpha, pygame.RLEACCEL)
            else:
                u.marker_active = False
        except IndexError:
            if not u.marker_alpha == 0:
                u.marker_alpha -= 1
                u.marker.set_alpha(u.marker_alpha, pygame.RLEACCEL)
            else:
                u.marker_active = False



def redframe():
    if Var.start_redframe:
        Var.start_redframe = False
        Frames.redframing = "grow"
        Frames.redframe_CPN += 1
        Frames.redframe_TPP = 10
        Frames.LPT = pygame.time.get_ticks()
    elif Frames.redframing:
        if (Frames.redframe_LPT + Frames.redframe_TPP) < pygame.time.get_ticks():
            if (Frames.redframing == "grow") and not (Frames.redframe_CPN == 11):
                Frames.redframe_CPN += 1
                Frames.redframe_LPT = pygame.time.get_ticks()
            elif (Frames.redframing == "shrink") and not (Var.hero.dying or Var.game_over):
                if Frames.redframe_CPN:
                    Frames.redframe_CPN -= 1
                    Frames.redframe_LPT = pygame.time.get_ticks()
                else:
                    Frames.redframing = False
            elif (Frames.redframe_LPT + (Frames.redframe_TPP*20)) < pygame.time.get_ticks(): # hier Faktor, wie langs ganz rot bleibt.
                Frames.redframing = "shrink"
                Frames.redframe_TPP = 120




def check_dead():
    for d in Var.dead: #=Liste
        if not d.name == "Hero":
            if pygame.time.get_ticks() > (d.TPP + d.LPT):
                d.LPT = pygame.time.get_ticks()
                if not d.alpha <= 0:
                    d.alpha -= 1
                    d.image.set_alpha(d.alpha, pygame.RLEACCEL)
                elif d.typ == "dead_Monster":
                    d.image = pygame.image.load(Var.path+"\\pics\\Monsters\\"+d.name.split('_')[0]+'\\'+d.name+"_empty.png").convert()
                    d.image.set_colorkey([0,0,0], pygame.RLEACCEL)
                    Var.dead.remove(d)
                    del d

            
def magnet(A, B, speed=1):
    vekt = [B.realpos[0]-A.realpos[0], B.realpos[1]-A.realpos[1]]
    if (abs(vekt[0]) < abs(vekt[1]//2)) and (vekt[1] < 0): # oben
        A.frameway[1] -= speed
        B.frameway[1] += speed
    elif (abs(vekt[0]) < abs(vekt[1]//2)) and (vekt[1] > 0): # unten
        A.frameway[1] += speed
        B.frameway[1] -= speed
    elif (abs(vekt[1]) < abs(vekt[0]//2)) and (vekt[0] < 0): # links
        A.frameway[0] -= speed
        B.frameway[0] += speed
    elif (abs(vekt[1]) < abs(vekt[0]//2)) and (vekt[0] > 0): # rechts
        A.frameway[0] += speed
        B.frameway[0] -= speed
    elif (vekt[0] < 0) and (vekt[1] < 0): # links oben
        A.frameway[0] -= speed
        B.frameway[0] += speed
        A.frameway[1] -= speed
        B.frameway[1] += speed
    elif (vekt[0] > 0) and (vekt[1] < 0): # rechts oben
        A.frameway[0] += speed
        B.frameway[0] -= speed
        A.frameway[1] -= speed
        B.frameway[1] += speed
    elif (vekt[0] < 0) and (vekt[1] > 0): # links unten
        A.frameway[0] -= speed
        B.frameway[0] += speed
        A.frameway[1] += speed
        B.frameway[1] -= speed
    elif (vekt[0] > 0) and (vekt[1] > 0): # rechts unten
        A.frameway[0] += speed
        B.frameway[0] -= speed
        A.frameway[1] += speed
        B.frameway[1] -= speed


def drift_apart(A, B, speed=1):
    vekt = [B.realpos[0]-A.realpos[0], B.realpos[1]-A.realpos[1]]
    if (abs(vekt[0]) < abs(vekt[1]//2)) and (vekt[1] < 0): # oben
        A.frameway[1] += speed
        B.frameway[1] -= speed
    elif (abs(vekt[0]) < abs(vekt[1]//2)) and (vekt[1] > 0): # unten
        A.frameway[1] -= speed
        B.frameway[1] += speed
    elif (abs(vekt[1]) < abs(vekt[0]//2)) and (vekt[0] < 0): # links
        A.frameway[0] += speed
        B.frameway[0] -= speed
    elif (abs(vekt[1]) < abs(vekt[0]//2)) and (vekt[0] > 0): # rechts
        A.frameway[0] -= speed
        B.frameway[0] += speed
    elif (vekt[0] < 0) and (vekt[1] < 0): # links oben
        A.frameway[0] += speed
        B.frameway[0] -= speed
        A.frameway[1] += speed
        B.frameway[1] -= speed
    elif (vekt[0] > 0) and (vekt[1] < 0): # rechts oben
        A.frameway[0] -= speed
        B.frameway[0] += speed
        A.frameway[1] += speed
        B.frameway[1] -= speed
    elif (vekt[0] < 0) and (vekt[1] > 0): # links unten
        A.frameway[0] += speed
        B.frameway[0] -= speed
        A.frameway[1] -= speed
        B.frameway[1] += speed
    elif (vekt[0] > 0) and (vekt[1] > 0): # rechts unten
        A.frameway[0] -= speed
        B.frameway[0] += speed
        A.frameway[1] -= speed
        B.frameway[1] += speed

    
