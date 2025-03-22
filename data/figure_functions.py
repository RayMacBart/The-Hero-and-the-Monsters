import pygame
from pool import Var


## handle_movement_purpose(figure)
## reload_pics(figure)
## handle_direction(figure)
## handle_walk_animation(figure)
## check_border_dir_and_layer_switch(border, figure)
## detect_borders(figure)
## get_other_blitted_masktypes(figure)
## handle_collision(figure)
## execute_movement(figure)



def handle_movement_purpose(figure):

    figure.current_absolute_pos = [figure.realpos[0] - Var.ref_point[0], figure.realpos[1] - Var.ref_point[1]]
    figure.current_way = [figure.absolute_destination[0] - figure.current_absolute_pos[0], figure.absolute_destination[1] - figure.current_absolute_pos[1]]
    xy_way_sign = [0, 0]
    xy_way_sign[0] = 1 if figure.current_way[0] >= 0 else -1
    xy_way_sign[1] = 1 if figure.current_way[1] >= 0 else -1
    if (abs(figure.current_way[0]) > 4+figure.speed) or (abs(figure.current_way[1]) > 4+figure.speed):
        if abs(figure.current_way[1]) > 0:
            x_to_y = abs(figure.current_way[0]/figure.current_way[1])
        else:
            x_to_y = figure.speed
        if (0.7 < x_to_y < 1.42):
            figure.frameway = [round(figure.speed/2)*xy_way_sign[0], round(figure.speed/2)*xy_way_sign[1]]
        elif x_to_y > 1.42:
            figure.frameway = [round((figure.speed-figure.speed/x_to_y)*xy_way_sign[0]), round((figure.speed/x_to_y)*xy_way_sign[1])]
        else:
            figure.frameway = [round((figure.speed*x_to_y)*xy_way_sign[0]), round((figure.speed-figure.speed*x_to_y)*xy_way_sign[1])]
    elif (abs(figure.current_way[0]) > 2) or (abs(figure.current_way[1]) > 2):
        figure.frameway = [0, 0]
        if abs(figure.current_way[0]) > 4:
            figure.frameway[0] = 4*xy_way_sign[0]
        elif figure.current_way[0]:
            figure.frameway[0] = xy_way_sign[0]
        if abs(figure.current_way[1]) > 4:
            figure.frameway[1] = 4*xy_way_sign[1]
        elif figure.current_way[1]:
            figure.frameway[1] = xy_way_sign[1]
    else:
        figure.frameway = [0, 0]
        figure.go = False
        figure.sounds["footsteps_sound"].stop()
        figure.footstep_sound_active = False
        figure.start_standing = True
        if not figure.drawn:
            figure.image = figure.current_pics["Stand"]

    if (figure.frameway[0] == 0) and (abs(figure.frameway[1]) >= 4):          # Entschärft Tempo gerader Gehlinien
        figure.frameway[1] -= 2*xy_way_sign[1]                                # (verstärkte oben-unten-Entschärfung 
    elif (abs(figure.frameway[0]) == 1) and (abs(figure.frameway[1]) >= 3):   # weil das ergibt 
        figure.frameway[1] -= 1*xy_way_sign[1]                                # 3D-Effekt!)
    elif (abs(figure.frameway[0]) >= 4) and (figure.frameway[1] == 0):        # 
        figure.frameway[0] -= 1*xy_way_sign[0]                                #
        
    if figure.drawn:
        a = abs(figure.frameway[0])//2       # Hier die Verlangsamung durch gezogene Waffe
        figure.frameway[0] = a*xy_way_sign[0]
        a = abs(figure.frameway[1])//2
        figure.frameway[1] = a*xy_way_sign[1]
        del a

    if not (figure == Var.hero):
        if not ((662 > figure.realpos[0] > -22) and (445 > figure.realpos[1] > -45)): # nicht auf screen zu sehen
            figure.frameway = [0, 0]
            figure.go = False
            figure.sounds["footsteps_sound"].stop()
            figure.footstep_sound_active = False
            figure.start_standing = True
            if not figure.drawn:
                figure.image = figure.current_pics["Stand"]


                            

def reload_pics(figure):  # wird von handle_direction(figure) verwendet (siehe unten)
    
    figure.current_pics.clear()
    if figure == Var.hero:
        folder = ""
    elif figure.typ == "Monster":
        folder = "Monsters\\"
    if not figure.drawn:
        figure.current_pics["Stand"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\'+figure.name+"_"+figure.dir+"_Stand.png").convert_alpha()
        figure.current_pics["Go_R1"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\'+figure.name+"_"+figure.dir+"_Go_R1.png").convert_alpha()
        figure.current_pics["Go_R2"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\'+figure.name+"_"+figure.dir+"_Go_R2.png").convert_alpha()
        figure.current_pics["Go_L1"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\'+figure.name+"_"+figure.dir+"_Go_L1.png").convert_alpha()
        figure.current_pics["Go_L2"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\'+figure.name+"_"+figure.dir+"_Go_L2.png").convert_alpha()
    else:
        figure.current_pics["Fight_1"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Fight\\'+figure.name+"_"+figure.dir+"_Fight_1.png").convert_alpha()
        figure.current_pics["Fight_2"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Fight\\'+figure.name+"_"+figure.dir+"_Fight_2.png").convert_alpha()
        figure.current_pics["Fight_3"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Fight\\'+figure.name+"_"+figure.dir+"_Fight_3.png").convert_alpha()
        figure.current_pics["Fight_4"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Fight\\'+figure.name+"_"+figure.dir+"_Fight_4.png").convert_alpha()
        figure.current_pics["Fight_5"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Fight\\'+figure.name+"_"+figure.dir+"_Fight_5.png").convert_alpha()
        figure.current_pics["Fight_6"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Fight\\'+figure.name+"_"+figure.dir+"_Fight_6.png").convert_alpha()
        figure.current_pics["Fight_7"] = pygame.image.load(Var.path+"\\pics\\"+folder+figure.name.split('_')[0]+'\\Fight\\'+figure.name+"_"+figure.dir+"_Fight_7.png").convert_alpha()
    


def handle_direction(figure):
    if (abs(figure.current_way[0])+abs(figure.current_way[1])) > 30: # für ruhigeren Richtungsgang und sinnvolleres/schöneres Stehenbleiben letztes Stück "gefreezed"
        if abs(figure.current_way[0])*3.7 <= figure.current_way[1]*(-1):
            if not figure.dir == "N":
                figure.dir = "N"
                reload_pics(figure)
        elif figure.current_way[0]*3.7 > figure.current_way[1]*(-1) and figure.current_way[0] < (figure.current_way[1]*3.7)*(-1):
            if not figure.dir == "NE":
                figure.dir = "NE"
                reload_pics(figure)
        elif abs(figure.current_way[1])*3.7 <= figure.current_way[0]:
            if not figure.dir == "E":
                figure.dir = "E"
                reload_pics(figure)
        elif figure.current_way[0] < figure.current_way[1]*3.7 and figure.current_way[0]*3.7 > figure.current_way[1]:
            if not figure.dir == "SE":
                figure.dir = "SE"
                reload_pics(figure)
        elif abs(figure.current_way[0])*3.7 <= figure.current_way[1]:
            if not figure.dir == "S":
                figure.dir = "S"
                reload_pics(figure)
        elif (figure.current_way[0]*(-1))*3.7 > figure.current_way[1] and figure.current_way[1]*3.7 > figure.current_way[0]*(-1):
            if not figure.dir == "SW":
                figure.dir = "SW"
                reload_pics(figure)
        elif abs(figure.current_way[1])*3.7 <= figure.current_way[0]*(-1):
            if not figure.dir == "W":
                figure.dir = "W"
                reload_pics(figure)
        elif (figure.current_way[1]*(-1))*3.7 > figure.current_way[0]*(-1) and (figure.current_way[0]*(-1))*3.7 > figure.current_way[1]*(-1):
            if not figure.dir == "NW":
                figure.dir = "NW"
                reload_pics(figure)




def handle_walk_animation(figure):
    if not figure.drawn:
        if figure.walk_animation_frame_countdown:
            figure.walk_animation_frame_countdown -= 1
        else:
            figure.walk_animation_frame_countdown = figure.walk_animation_delay
            if not figure.walk_animation_progress == 8:
                figure.walk_animation_progress += 1
            else:
                figure.walk_animation_progress = 1
            if (figure.walk_animation_progress == 1) or (figure.walk_animation_progress == 5):
                try:
                    figure.image = figure.current_pics["Stand"]
                except:
                    print("ERROR NO STAND IN IMAGES. CURRENT PICS:", figure.current_pics)
            elif (figure.walk_animation_progress == 2) or (figure.walk_animation_progress == 4):
                figure.image = figure.current_pics["Go_R1"]
            elif (figure.walk_animation_progress == 3):
                figure.image = figure.current_pics["Go_R2"]
            elif (figure.walk_animation_progress == 6) or (figure.walk_animation_progress == 8):
                figure.image = figure.current_pics["Go_L1"]
            elif (figure.walk_animation_progress == 7):
                figure.image = figure.current_pics["Go_L2"]
    else:
        figure.handle_fightwalk_animation()






def check_border_dir_and_layer_switch(border, figure):     # wird von "detect_borders" (siehe unten) verwendet.
    
    inpos = [figure.realpos[0]-border.pos[0], figure.realpos[1]-border.pos[1]]

    if (border.name.split("_")[-2:][0] + "_" + border.name.split("_")[-2:][1]) == "edge_OL":
        #figure.border_dir = "SE" if ((inpos[0] < 44) and (inpos[1] < 76)) else "NW"
        if ((inpos[0] < 44) and (inpos[1] < 76) and (inpos[0] < 18)):
            figure.border_dir = "S"
        elif ((inpos[0] < 44) and (inpos[1] < 76) and (inpos[1] < 58)):
            figure.border_dir = "E"
        elif ((inpos[0] < 44) and (inpos[1] < 76)):
            figure.border_dir = "SE"
        elif (inpos[0] < 40):
            figure.border_dir = "N"
        elif (inpos[1] < 64):
            figure.border_dir = "W"
        else:
            figure.border_dir = "NW"
        if ((inpos[0] < 44) and (inpos[1] < 76)):
            if ((inpos[1] > 12) or (inpos[0]+inpos[1] > 44)):
                if figure.layerpos[1] > border.layerpos[1]:
                    border.layerpos[1] = figure.layerpos[1]+9
        elif figure.layerpos[1] < figure.realpos[1]:
            figure.layerpos[1] = figure.pos[1]+figure.height//2+10
        
    elif (border.name.split("_")[-2:][0] + "_" + border.name.split("_")[-2:][1]) == "edge_OR":
        #figure.border_dir = "SW" if ((inpos[0] > 54) and (inpos[1] < 76)) else "NE"
        if ((inpos[0] > 54) and (inpos[1] < 76) and (inpos[0] > 82)):
            figure.border_dir = "S"
        elif ((inpos[0] > 54) and (inpos[1] < 76) and (inpos[1] < 58)):
            figure.border_dir = "W"
        elif ((inpos[0] > 54) and (inpos[1] < 76)):
            figure.border_dir = "SW"
        elif (inpos[0] > 60):
            figure.border_dir = "N"
        elif (inpos[1] < 64):
            figure.border_dir = "E"
        else:
            figure.border_dir = "NE"
        if ((inpos[0] > 54) and (inpos[1] < 76)):
            if ((inpos[1] > 12) or (inpos[0]-inpos[1] < 55)):
                if figure.layerpos[1] > border.layerpos[1]:
                    border.layerpos[1] = figure.layerpos[1]+9
        elif figure.layerpos[1] < figure.realpos[1]:
            figure.layerpos[1] = figure.pos[1]+figure.height//2+10

    elif (border.name.split("_")[-2:][0] + "_" + border.name.split("_")[-2:][1]) == "edge_UL":
        figure.border_dir = "NE" if ((inpos[0] < 44) and (inpos[1] > 82)) else "SW"
        if ((inpos[0] < 44) and (inpos[1] > 82)):
            if figure.layerpos[1] < figure.realpos[1]:
                figure.layerpos[1] = figure.pos[1]+figure.height//2+10
        elif ((inpos[0] < 60) and (inpos[1] > 14) and (inpos[0]-inpos[1] < 21) and (inpos[0]-(inpos[1]/3) < 41)):
            if figure.layerpos[1] > border.layerpos[1]:
                border.layerpos[1] = figure.layerpos[1]+9
        
    elif (border.name.split("_")[-2:][0] + "_" + border.name.split("_")[-2:][1]) == "edge_UR":
        figure.border_dir = "NW" if ((inpos[0] > 56) and (inpos[1] > 82)) else "SE"
        if ((inpos[0] > 56) and (inpos[1] > 82)):
            if figure.layerpos[1] < figure.realpos[1]:
                figure.layerpos[1] = figure.pos[1]+figure.height//2+10
        elif ((inpos[0] > 40) and (inpos[1] > 14) and (inpos[0]+inpos[1] > 78) and ((inpos[0]*3)+inpos[1] > 174)):
            if figure.layerpos[1] > border.layerpos[1]:
                border.layerpos[1] = figure.layerpos[1]+9

    elif (border.name.split("_")[-2:][0] + "_" + border.name.split("_")[-2:][1]) in ["edge_R", "X_R"]:
        if (inpos[0] > 95) and (88 > inpos[1] > 70):
            figure.border_dir = "W"
        elif (inpos[0]-inpos[1] > 20):
            figure.border_dir = "SW"
        elif (inpos[0]+inpos[1] > 178):
            figure.border_dir = "NW"
        elif (inpos[1] < 79):
            figure.border_dir = "NE"
        else:
            figure.border_dir = "SE"
        if (((inpos[0]+inpos[1] < 178) and (inpos[0]+inpos[1] > 154)) or \
           ((inpos[0]-inpos[1] > 20) and (inpos[0]-inpos[1] < 75))):
            if figure.layerpos[1] > border.layerpos[1]:
                border.layerpos[1] = figure.layerpos[1]+9
        elif figure.layerpos[1] < figure.realpos[1]:
            figure.layerpos[1] = figure.pos[1]+figure.height//2+10
    
    elif (border.name.split("_")[-2:][0] + "_" + border.name.split("_")[-2:][1]) in ["edge_L", "X_L"]:
        if (inpos[0] < 5) and (88 > inpos[1] > 70):
            figure.border_dir = "E"
        elif (inpos[0]+inpos[1] < 79):
            figure.border_dir = "SE"
        elif (inpos[1]-inpos[0] > 79):
            figure.border_dir = "NE"
        elif (inpos[1] < 79):
            figure.border_dir = "NW"
        else:
            figure.border_dir = "SW"
        if (((inpos[1]-inpos[0] < 79) and (inpos[1]-inpos[0] > 55)) or \
           ((inpos[0]+inpos[1] < 79) and (inpos[0]+inpos[1] > 24))):
            #print("behinder")
            if figure.layerpos[1] > border.layerpos[1]:
                border.layerpos[1] = figure.layerpos[1]+9
        elif figure.layerpos[1] < figure.realpos[1]:
            #print("beforer")
            figure.layerpos[1] = figure.pos[1]+figure.height//2+10

    elif (border.name.split("_")[-2:][0] + "_" + border.name.split("_")[-2:][1]) == "+_C":
        if ((inpos[0] < 44) and (inpos[1] > 82)):
            figure.border_dir = "NE"
        elif ((inpos[0] > 56) and (inpos[1] > 82)):
            figure.border_dir = "NW"
        elif ((inpos[0] < 44) and (inpos[1] < 76)):
            figure.border_dir = "SE"
        elif ((inpos[0] > 54) and (inpos[1] < 76)):
            figure.border_dir = "SW"
        if ((inpos[1] < 76) and (inpos[1] > 14)):
            if figure.layerpos[1] > border.layerpos[1]:
                border.layerpos[1] = figure.layerpos[1]+9
        elif figure.layerpos[1] < figure.realpos[1]:
            figure.layerpos[1] = figure.pos[1]+figure.height//2+10

    elif (border.name.split("_")[-2:][0] + "_" + border.name.split("_")[-2:][1]) == "+_N":
        if ((inpos[0] < 44) and (inpos[1] > 82)):
            figure.border_dir = "NE"
        elif ((inpos[0] > 56) and (inpos[1] > 82)):
            figure.border_dir = "NW"
        elif (inpos[1] < 76):
            figure.border_dir = "S"
        if ((inpos[1] < 76) and (inpos[1] > 14)):
            if figure.layerpos[1] > border.layerpos[1]:
                border.layerpos[1] = figure.layerpos[1]+9
        elif figure.layerpos[1] < figure.realpos[1]:
            figure.layerpos[1] = figure.pos[1]+figure.height//2+10

    elif (border.name.split("_")[-2:][0] + "_" + border.name.split("_")[-2:][1]) == "+_E":
        if ((inpos[0] < 44) and (inpos[1] > 82)):
            figure.border_dir = "NE"
        elif ((inpos[0] < 44) and (inpos[1] < 76)):
            figure.border_dir = "SE"
        elif (inpos[0] > 54):
            figure.border_dir = "W"
        if ((inpos[1] < 76) and (inpos[1] > 14)):
            if figure.layerpos[1] > border.layerpos[1]:
                border.layerpos[1] = figure.layerpos[1]+9
        elif figure.layerpos[1] < figure.realpos[1]:
            figure.layerpos[1] = figure.pos[1]+figure.height//2+10

    elif (border.name.split("_")[-2:][0] + "_" + border.name.split("_")[-2:][1]) == "+_S":
        if (inpos[1] > 82):
            figure.border_dir = "N"
        elif ((inpos[0] < 44) and (inpos[1] < 76)):
            figure.border_dir = "SE"
        elif ((inpos[0] > 54) and (inpos[1] < 76)):
            figure.border_dir = "SW"
        if ((inpos[1] < 76) and (inpos[1] > 14)):
            if figure.layerpos[1] > border.layerpos[1]:
                border.layerpos[1] = figure.layerpos[1]+9
        elif figure.layerpos[1] < figure.realpos[1]:
            figure.layerpos[1] = figure.pos[1]+figure.height//2+10

    elif (border.name.split("_")[-2:][0] + "_" + border.name.split("_")[-2:][1]) == "+_W":
        if ((inpos[0] > 56) and (inpos[1] > 82)):
            figure.border_dir = "NW"
        elif (inpos[0] < 44):
            figure.border_dir = "E"
        elif ((inpos[0] > 54) and (inpos[1] < 76)):
            figure.border_dir = "SW"
        if ((inpos[1] < 76) and (inpos[1] > 14)):
            if figure.layerpos[1] > border.layerpos[1]:
                border.layerpos[1] = figure.layerpos[1]+9
        elif figure.layerpos[1] < figure.realpos[1]:
            figure.layerpos[1] = figure.pos[1]+figure.height//2+10
    
    elif border.name.split("_")[-1] in ["LR", "W", "E"]:
        if inpos[1] < 82:
            figure.border_dir = "S"
            if inpos[1] > 14:
                if figure.layerpos[1] > border.layerpos[1]:
                    border.layerpos[1] = figure.layerpos[1]+9
            else:
                if figure.layerpos[1] < figure.realpos[1]:
                    figure.layerpos[1] = figure.pos[1]+figure.height//2+10
        elif (inpos[1] > 75):
            figure.border_dir = "N"
            if figure.layerpos[1] < figure.realpos[1]:
                figure.layerpos[1] = figure.pos[1]+figure.height//2+10
            if figure.layerpos[1] < border.layerpos[1]:
                border.layerpos[1] = figure.layerpos[1]-9
            

    elif border.name.split("_")[-1] in ["OU", "N", "S"]:
        figure.border_dir = "E" if inpos[0] < 50 else "W"
        if figure.layerpos[1] < figure.realpos[1]:
            figure.layerpos[1] = figure.pos[1]+figure.height//2+10
            
    elif border.name.split("_")[-1] in ["OR", "SE"]:
        figure.border_dir = "SW" if ((inpos[0] - inpos[1]) > 20) else "NE"
        if ((inpos[0] - inpos[1]) > 20) :
            if ((inpos[0] - inpos[1]) < 75):
                if figure.layerpos[1] > border.layerpos[1]:
                    border.layerpos[1] = figure.layerpos[1]+9
        elif figure.layerpos[1] < figure.realpos[1]:
            figure.layerpos[1] = figure.pos[1]+figure.height//2+10
                
    elif border.name.split("_")[-1] in ["UL", "NW"]:
        figure.border_dir = "SW" if ((inpos[1] - inpos[0]) < 80) else "NE"
        if ((inpos[1] - inpos[0]) < 80):
            if ((inpos[1] - inpos[0]) > 25):
                if figure.layerpos[1] > border.layerpos[1]:
                    border.layerpos[1] = figure.layerpos[1]+9
        elif figure.layerpos[1] < figure.realpos[1]:
            figure.layerpos[1] = figure.pos[1]+figure.height//2+10
                
    elif border.name.split("_")[-1] in ["OL", "SW"]:
        figure.border_dir = "SE" if ((inpos[0] + inpos[1]) < 77) else "NW"
        if ((inpos[0] + inpos[1]) < 77):
            if ((inpos[0] + inpos[1]) > 24):
                if figure.layerpos[1] > border.layerpos[1]:
                    border.layerpos[1] = figure.layerpos[1]+9
        elif figure.layerpos[1] < figure.realpos[1]:
            figure.layerpos[1] = figure.pos[1]+figure.height//2+10
        
    elif border.name.split("_")[-1] in ["UR", "NE"]:
        figure.border_dir = "SE" if ((inpos[0] + inpos[1]) < 180) else "NW"
        if ((inpos[0] + inpos[1]) < 180):
            if ((inpos[0] + inpos[1]) > 124):
                if figure.layerpos[1] > border.layerpos[1]:
                    border.layerpos[1] = figure.layerpos[1]+9
        elif figure.layerpos[1] < figure.realpos[1]:
            figure.layerpos[1] = figure.pos[1]+figure.height//2+10
        
    elif (border.name.split("_")[-1] == "LR-OL"):
        figure.border_dir = "SE" if ((inpos[0]+inpos[1] < 172) and (inpos[1] < 75)) else "NW"
        if ((inpos[0]+inpos[1] < 172) and (inpos[1] < 75)):
            if ((inpos[1] > 14) or (inpos[0]+(inpos[1]*2) > 121)):
                if figure.layerpos[1] > border.layerpos[1]:
                    border.layerpos[1] = figure.layerpos[1]+9
        elif figure.layerpos[1] < figure.realpos[1]:
            figure.layerpos[1] = figure.pos[1]+figure.height//2+10
        
    elif (border.name.split("_")[-1] == "LR-UL"):
        figure.border_dir = "NE" if ((inpos[0]-inpos[1] < 16) and (inpos[1] > 81)) else "SW"
        if ((inpos[0]-inpos[1] < 16) and (inpos[1] > 81)):
            if figure.layerpos[1] < figure.realpos[1]:
                figure.layerpos[1] = figure.pos[1]+figure.height//2+10
        elif ((inpos[1] > 14) and ((inpos[0]/3)-inpos[1] < 5) and \
              ((inpos[0]/2)-inpos[1] < 19) and (inpos[0]-inpos[1] < 75)):
            if figure.layerpos[1] > border.layerpos[1]:
                border.layerpos[1] = figure.layerpos[1]+9
        
    elif (border.name.split("_")[-1] == "OR-LR"):
        figure.border_dir = "SW" if ((inpos[0]-inpos[1] > 27) and (inpos[1] < 75)) else "NE"
        if ((inpos[0]-inpos[1] > 27) and (inpos[1] < 75)):
            if (((inpos[0]/2)-inpos[1] < 39) or (inpos[1] > 14)):
                if figure.layerpos[1] > border.layerpos[1]:
                    border.layerpos[1] = figure.layerpos[1]+9
        elif figure.layerpos[1] < figure.realpos[1]:
            figure.layerpos[1] = figure.pos[1]+figure.height//2+10
        
    elif (border.name.split("_")[-1] == "UR-LR"):
        figure.border_dir = "NW" if ((inpos[0]+inpos[1] > 186) and (inpos[1] > 81)) else "SE"
        if ((inpos[0]+inpos[1] > 186) and (inpos[1] > 81)):
            if figure.layerpos[1] < figure.realpos[1]:
                figure.layerpos[1] = figure.pos[1]+figure.height//2+10
        elif ((inpos[0]+inpos[1] > 124) and (inpos[0]+(inpos[1]*2) > 161) and \
              (inpos[0]+(inpos[1]*3) > 184) and (inpos[1] > 14)):
            if figure.layerpos[1] > border.layerpos[1]:
                border.layerpos[1] = figure.layerpos[1]+9
        
    elif (border.name.split("_")[-1] == "OU-OL"):
        figure.border_dir = "SE" if ((inpos[0]+inpos[1] < 175) and (inpos[0] < 46)) else "NW"
        if ((inpos[0]+inpos[1] < 175) and (inpos[0] < 46)):
            if (((inpos[1] > 41) and (inpos[0] > 36)) or ((inpos[0]*2)+inpos[1] > 145) or (inpos[0]+inpos[1] > 124)):
                if figure.layerpos[1] > border.layerpos[1]:
                    border.layerpos[1] = figure.layerpos[1]+9
        elif figure.layerpos[1] < figure.realpos[1]:
            figure.layerpos[1] = figure.pos[1]+figure.height//2+10
        
    elif (border.name.split("_")[-1] == "OU-OR"):
        figure.border_dir = "SW" if ((inpos[1]-inpos[0] < 77) and (inpos[0] > 54)) else "NE"
        if ((inpos[1]-inpos[0] < 77) and (inpos[0] > 54)):
            if (((inpos[1] > 41) and (inpos[0] < 63)) or (inpos[0]-(inpos[1]/2) < 27) or (inpos[1]-inpos[0] > 25)):
                if figure.layerpos[1] > border.layerpos[1]:
                    border.layerpos[1] = figure.layerpos[1]+9
        elif figure.layerpos[1] < figure.realpos[1]:
            figure.layerpos[1] = figure.pos[1]+figure.height//2+10
        
    elif (border.name.split("_")[-1] == "UL-OU"):
        figure.border_dir = "NE" if ((inpos[1]-inpos[0] > 78) and (inpos[0] < 45)) else "SW"
        if ((inpos[1]-inpos[0] > 78) and (inpos[0] < 45)):
            if figure.layerpos[1] < figure.realpos[1]:
                figure.layerpos[1] = figure.pos[1]+figure.height//2+10
        elif ((inpos[1]-inpos[0] > 25) and (inpos[0]-(inpos[1]/2) < 8) and \
              (inpos[0]-(inpos[1]/3) < 22) and (inpos[0] < 60)):
            if figure.layerpos[1] > border.layerpos[1]:
                border.layerpos[1] = figure.layerpos[1]+9
        
    elif (border.name.split("_")[-1] == "UR-OU"):
        figure.border_dir = "NW" if ((inpos[0]+inpos[1] > 180) and (inpos[0] > 53)) else "SE"
        if ((inpos[0]+inpos[1] > 180) and (inpos[0] > 53)):
            if figure.layerpos[1] < figure.realpos[1]:
                figure.layerpos[1] = figure.pos[1]+figure.height//2+10
        elif ((inpos[0] > 39) and ((inpos[0]*3)+inpos[1] > 232) and \
              ((inpos[0]*2)+inpos[1] > 182) and (inpos[0]+inpos[1] > 124)):
            if figure.layerpos[1] > border.layerpos[1]:
                border.layerpos[1] = figure.layerpos[1]+9
        
    elif "OR-UL" in border.name:                                               # Ab hier wieder DOOR
        if ((inpos[0] - inpos[1]) < -4):
            figure.border_dir = "NE"
        elif ((inpos[0] - inpos[1]) > 15):
            figure.border_dir = "SW"
        else:
            figure.border_dir = "SE" if ((inpos[0] + inpos[1]) >= 179) else "NW"
        if (inpos[0]-inpos[1]) < 15 or (inpos[0]-inpos[1]) > 86:
            if figure.layerpos[1] < border.layerpos[1]:
                border.layerpos[1] = figure.layerpos[1]-9
        elif figure.layerpos[1] > border.layerpos[1]:
            border.layerpos[1] = figure.layerpos[1]+9

    elif "UR-OL" in border.name:
        if ((inpos[0] + inpos[1]) > 203):
            figure.border_dir = "NW"
        elif ((inpos[0] + inpos[1]) < 184):
            figure.border_dir = "SE"
        else:
            figure.border_dir = "SW" if ((inpos[0]-inpos[1]) <= 20) else "NE"
        if (inpos[0]+inpos[1]) > 184 or (inpos[0]+inpos[1]) < 113:
            if figure.layerpos[1] < border.layerpos[1]:
                border.layerpos[1] = figure.layerpos[1]-9
        elif figure.layerpos[1] > border.layerpos[1]:
            border.layerpos[1] = figure.layerpos[1]+9

    if "Door_LR" in border.name:
        if inpos[1] > 84:
            figure.border_dir = "N"
        elif inpos[1] < 73:
            figure.border_dir = "S"
        else:
            figure.border_dir = "W" if (inpos[0] < 50) else "E"

    if "Door_OU" in border.name:
        if inpos[0] < 40:
            figure.border_dir = "E"
        elif inpos[0] > 59:
            figure.border_dir = "W"
        else:
            figure.border_dir = "N" if (inpos[1] < 69) else "S"
        if border.doorcopy:
            if border.doorcopy.layerpos[1] < border.pos[1]+border.height:
                border.doorcopy.layerpos[1] = border.pos[1]+border.height

    

def detect_borders(figure):
    bordertest = False
    for b in Var.blitlist:
        if (b.typ == "Border") or (b.typ == "High_border") or (b.typ == "Door"):
            if ((b.pos[0]-12 <= figure.realpos[0]) and (b.pos[0]+b.width+12 > figure.realpos[0])) and \
               ((b.pos[1]-5 <= figure.realpos[1]) and (b.pos[1]+b.height+50 > figure.realpos[1])):
               #((b.pos[1]+5 <= figure.realpos[1]) and (b.pos[1]+b.height-5 > figure.realpos[1])):
                bordertest = True
                check_border_dir_and_layer_switch(b, figure)
##            elif not b.layerpos == b.realpos:
##                b.layerpos = b.realpos
    if not bordertest:
        figure.border_dir = ""
        figure.layerpos[1] = figure.pos[1]+figure.height//2+10




            



def get_other_blitted_masktypes(figure):  #wird von handle_collision verwendet (siehe unten)
    
    for cc in figure.other_blitted_masktypes:
        if not (cc in Var.blitlist) or not ((cc in Var.borders.values()) or \
               (cc in Var.doors.values()) or \
               (cc in Var.obstacles.values()) or \
               (cc in Var.animated_obstacles.values()) or \
               (cc in Var.units.values())):
            figure.other_blitted_masktypes.remove(cc)
    for b in Var.blitlist:
        if (not (b == figure)) and (not (b in figure.other_blitted_masktypes)):
            if (b == Var.hero) or (b in Var.borders.values()) or \
               (b in Var.doors.values()) or \
               (b in Var.obstacles.values()) or \
               (b in Var.animated_obstacles.values()) or \
               (b in Var.units.values()):
                figure.other_blitted_masktypes.append(b)





def handle_collision(figure):
    
    get_other_blitted_masktypes(figure)
    figure.collision_direction = None
    for cc in figure.other_blitted_masktypes:
        othermask = None
        if not ((figure.typ == "Monster") and (cc.typ == "Monster")):
            othermask = cc.mask
        else:
            othermask = cc.bigmask # soll beim Kampf gegen mehrere Feinde bewirken, dass die Feinde nicht so nah beieinanderstehen können.
        if figure.x_mask.overlap_area(othermask, [cc.pos[0]-figure.pos[0], cc.pos[1]-figure.pos[1]]) or \
           figure.straight_mask.overlap_area(othermask, [cc.pos[0]-figure.pos[0], cc.pos[1]-figure.pos[1]]):
            #if figure == Var.hero:
                #print(str(pygame.time.get_ticks())+":", "Collision with", cc.name)
#            if figure == Var.hero:
            if cc.typ in ["Border", "High_border", "Door"]:
                if figure.border_dir in ["W", "NW", "SW"]:
                    if figure.frameway[0] < 0:
                        figure.frameway[0] = 0
                if figure.border_dir in ["N", "NW", "NE"]:
                    if figure.frameway[1] < 0:
                        figure.frameway[1] = 0
                if figure.border_dir in ["E", "NE", "SE"]:
                    if figure.frameway[0] > 0:
                        figure.frameway[0] = 0
                if figure.border_dir in ["S", "SW", "SE"]:
                    if figure.frameway[1] > 0:
                        figure.frameway[1] = 0
            else:
                if (cc.realpos[0]-figure.realpos[0] < 0):
                    if figure.frameway[0] < 0:
                        figure.frameway[0] = 0
                if (cc.realpos[1]-figure.realpos[1] < 0):
                    if figure.frameway[1] < 0:
                        figure.frameway[1] = 0
                if (cc.realpos[0]-figure.realpos[0] > 0):
                    if figure.frameway[0] > 0:
                        figure.frameway[0] = 0
                if (cc.realpos[1]-figure.realpos[1] > 0):
                    if figure.frameway[1] > 0:
                        figure.frameway[1] = 0
                            
            # ab hier wird Kollisionsrichtung per mask.overlap eruiert

            xdir = 0
            ydir = 0

            if figure.straight_mask.overlap_area(othermask, [cc.pos[0]-figure.pos[0], cc.pos[1]-figure.pos[1]]):
                coords_from_mask = figure.straight_mask.overlap(othermask, [cc.pos[0]-figure.pos[0], cc.pos[1]-figure.pos[1]])
                xdir = coords_from_mask[0] - figure.mask_mid[0]
                ydir = coords_from_mask[1] - figure.mask_mid[1]
                if (xdir in [-5,-4,-3,-2,-1,0,1,2,3,4,5]) and (ydir in [-15,-14,-13]):
                    figure.collision_direction = "N"
                elif (xdir in [23,24,25]) and (ydir in [-3,-2,-1,0,1,2,3]):
                    figure.collision_direction = "E"
                elif (xdir in [-5,-4,-3,-2,-1,0,1,2,3,4,5]) and (ydir in [13,14,15]):
                    figure.collision_direction = "S"
                elif (xdir in [-25,-24,-23]) and (ydir == [-3,-2,-1,0,1,2,3]):
                    figure.collision_direction = "W"
                    
            # Da die x_mask hier später extra behandelt wird, kann sie figure.collision_direction überschreiben und hat somit Priorität.
            if figure.x_mask.overlap_area(othermask, [cc.pos[0]-figure.pos[0], cc.pos[1]-figure.pos[1]]): 
                coords_from_mask = figure.x_mask.overlap(othermask, [cc.pos[0]-figure.pos[0], cc.pos[1]-figure.pos[1]])
                xdir = coords_from_mask[0] - figure.mask_mid[0]
                ydir = coords_from_mask[1] - figure.mask_mid[1]
                if (xdir in [13,14,15,16,17,18,19,20,21,22]) and (ydir in [-12,-11,-10,-9,-8,-7,-6]):
                    figure.collision_direction = "NE"
                elif (xdir in [13,14,15,16,17,18,19,20,21,22]) and (ydir in [6,7,8,9,10,11,12]):
                    figure.collision_direction = "SE"
                elif (xdir in [-21,-20,-19,-18,-17,-16,-15,-14,-12,-11]) and (ydir in [6,7,8,9,10,11,12]):
                    figure.collision_direction = "SW"
                elif (xdir in [-21,-20,-19,-18,-17,-16,-15,-14,-12,-11]) and (ydir in [-12,-11,-10,-9,-8,-7,-6]):
                    figure.collision_direction = "NW"
                elif xdir in [-25,-24,-23,-22,-21] and ydir in [0,-1,-2,-3]:
                    figure.collision_direction = "NW"

            del coords_from_mask
            Var.xdir = xdir
            Var.ydir = ydir
            
            if figure.collision_direction == "NE":
                if figure.frameway[0] > 0:
                    figure.frameway[0] = 0
                if figure.frameway[1] < 0:
                    figure.frameway[1] = 0
            elif figure.collision_direction == "SE":
                if figure.frameway[0] > 0:
                    figure.frameway[0] = 0
                if figure.frameway[1] > 0:
                    figure.frameway[1] = 0
            elif figure.collision_direction == "SW":
                if figure.frameway[0] < 0:
                    figure.frameway[0] = 0
                if figure.frameway[1] > 0:
                    figure.frameway[1] = 0
            elif figure.collision_direction == "NW":
                if figure.frameway[0] < 0:
                    figure.frameway[0] = 0
                if figure.frameway[1] < 0:
                    figure.frameway[1] = 0
            elif figure.collision_direction == "N":
                if figure.frameway[1] < 0:
                    figure.frameway[1] = 0
            elif figure.collision_direction == "E":
                if figure.frameway[0] > 0:
                    figure.frameway[0] = 0
            elif figure.collision_direction == "S":
                if figure.frameway[1] > 0:
                    figure.frameway[1] = 0
            elif figure.collision_direction == "W":
                if figure.frameway[0] < 0:
                    figure.frameway[0] = 0           

            # Feststecken der Figur wird durch folgende Maßnahme verhindert:
                    
            try:
                if (figure.frameway[0] == 0) and (abs(figure.current_way[0]) > 10):
                    if ((figure.current_way[0]) > 0) and figure.collision_direction in ["E", "NE", "SE"]:
                        if Var.frames_since_last_click < 3:
                            figure.frameway[0] = (figure.current_way[0]//abs(figure.current_way[0]))*-1
                    elif ((figure.current_way[0]) < 0) and figure.collision_direction in ["W", "NW", "SW"]:
                        if Var.frames_since_last_click < 3:
                            figure.frameway[0] = (figure.current_way[0]//abs(figure.current_way[0]))*-1
                    elif ((figure.current_way[0]) < 0) and figure.collision_direction in ["E", "NE", "SE"]:
                        figure.frameway[0] -= 3
                    elif ((figure.current_way[0]) > 0) and figure.collision_direction in ["W", "NW", "SW"]:
                        figure.frameway[0] += 3
                    
                if (figure.frameway[1] == 0) and (abs(figure.current_way[1]) > 10):
                    if ((figure.current_way[1]) > 0) and figure.collision_direction in ["S", "SW", "SE"]:
                        if Var.frames_since_last_click < 3:
                            figure.frameway[1] = (figure.current_way[1]//abs(figure.current_way[1]))*-1
                    elif ((figure.current_way[1]) < 0) and figure.collision_direction in ["N", "NW", "NE"]:
                        if Var.frames_since_last_click < 3:
                            figure.frameway[1] = (figure.current_way[1]//abs(figure.current_way[1]))*-1
                    elif ((figure.current_way[1]) < 0) and figure.collision_direction in ["S", "SW", "SE"]:
                        figure.frameway[1] -= 3
                    elif ((figure.current_way[1]) > 0) and figure.collision_direction in ["N", "NW", "NE"]:
                        figure.frameway[1] += 3

                if not figure.collision_direction:
                    if Var.frames_since_last_click < 5:
                        figure.frameway[0] = (figure.current_way[0]//abs(figure.current_way[0]))
                        figure.frameway[1] = (figure.current_way[1]//abs(figure.current_way[1]))
                    
            except ZeroDivisionError:
                pass

            

####            Var.collision_direction = collision_direction


            # Alte Idee (leider noch vergebliche Versuche), damit Kollision "smoother" zu machen
          
##            if collision_direction == "N":
##                if (abs(figure.frameway[0]) == 0) and (abs(figure.current_way[0]) > 0):
##                    figure.frameway[0] = figure.current_way[0]//abs(figure.current_way[0])
##            elif collision_direction == "NE":
##                if (figure.frameway[0] == 0) and (abs(figure.current_way[0]) > abs(figure.current_way[1])):
##                    figure.frameway[0] = 1
##                    figure.frameway[1] = 1
##                if (figure.frameway[1] == 0) and (abs(figure.current_way[1]) > abs(figure.current_way[0])):
##                    figure.frameway[0] = -1
##                    figure.frameway[1] = -1
##            elif collision_direction == "E":
##                if (abs(figure.frameway[1]) == 0) and (abs(figure.current_way[1]) > 0):
##                    figure.frameway[1] = figure.current_way[0]//abs(figure.current_way[0])
##            elif collision_direction == "SE":
##                if (figure.frameway[0] == 0) and (abs(figure.current_way[0]) > abs(figure.current_way[1])):
##                    figure.frameway[0] = 1
##                    figure.frameway[1] = -1
##                if (figure.frameway[1] == 0) and (abs(figure.current_way[1]) > abs(figure.current_way[0])):
##                    figure.frameway[0] = -1
##                    figure.frameway[1] = 1
##            elif collision_direction == "S":
##                if (abs(figure.frameway[0]) == 0) and (abs(figure.current_way[0]) > 0):
##                    figure.frameway[0] = figure.current_way[0]//abs(figure.current_way[0])
##            elif collision_direction == "SW":
##                if (figure.frameway[0] == 0) and (abs(figure.current_way[0]) > abs(figure.current_way[1])):
##                    figure.frameway[0] = -1
##                    figure.frameway[1] = -1
##                if (figure.frameway[1] == 0) and (abs(figure.current_way[1]) > abs(figure.current_way[0])):
##                    figure.frameway[0] = 1
##                    figure.frameway[1] = 1
##            elif collision_direction == "W":
##                if (abs(figure.frameway[1]) == 0) and (abs(figure.current_way[1]) > 0):
##                    figure.frameway[1] = figure.current_way[0]//abs(figure.current_way[0])
##            elif collision_direction == "NW":
##                if (figure.frameway[0] == 0) and (abs(figure.current_way[0]) > abs(figure.current_way[1])):
##                    figure.frameway[0] = -1
##                    figure.frameway[1] = 1
##                if (figure.frameway[1] == 0) and (abs(figure.current_way[1]) > abs(figure.current_way[0])):
##                    figure.frameway[0] = 1
##                    figure.frameway[1] = -1

            # "APRALLEN"/Spiegelreflektiert weitergehen von KIs bei Kollision:
            if not (figure == Var.hero) and (figure.last_collision_time < pygame.time.get_ticks()+300):
                figure.last_collision_time = pygame.time.get_ticks()
                if figure.collision_direction == "N":
                    if figure.current_way[1] < 0:   
                        figure.absolute_destination[1] = figure.current_absolute_pos[1] + (figure.current_way[1]*(-1))
                elif figure.collision_direction == "NE":
                    if figure.current_way[0] > 0:
                        figure.absolute_destination[0] = figure.current_absolute_pos[0] + (figure.current_way[0]*(-1))
                    if figure.current_way[1] < 0:
                        figure.absolute_destination[1] = figure.current_absolute_pos[1] + (figure.current_way[1]*(-1))
                elif figure.collision_direction == "E":
                    if figure.current_way[0] > 0:
                        figure.absolute_destination[0] = figure.current_absolute_pos[0] + (figure.current_way[0]*(-1))
                elif figure.collision_direction == "SE":
                    if figure.current_way[0] > 0:
                        figure.absolute_destination[0] = figure.current_absolute_pos[0] + (figure.current_way[0]*(-1))
                    if figure.current_way[1] > 0:
                        figure.absolute_destination[1] = figure.current_absolute_pos[1] + (figure.current_way[1]*(-1))
                elif figure.collision_direction == "S":
                    if figure.current_way[1] > 0:
                        figure.absolute_destination[1] = figure.current_absolute_pos[1] + (figure.current_way[1]*(-1))
                elif figure.collision_direction == "SW":
                    if figure.current_way[0] < 0:
                        figure.absolute_destination[0] = figure.current_absolute_pos[0] + (figure.current_way[0]*(-1))
                    if figure.current_way[1] > 0:
                        figure.absolute_destination[1] = figure.current_absolute_pos[1] + (figure.current_way[1]*(-1))
                elif figure.collision_direction == "W":
                    if figure.current_way[0] < 0:
                        figure.absolute_destination[0] = figure.current_absolute_pos[0] + (figure.current_way[0]*(-1))
                elif figure.collision_direction == "NW":
                    if figure.current_way[0] < 0:
                        figure.absolute_destination[0] = figure.current_absolute_pos[0] + (figure.current_way[0]*(-1))
                    if figure.current_way[1] < 0:
                        figure.absolute_destination[1] = figure.current_absolute_pos[1] + (figure.current_way[1]*(-1))

###    figure.collision_direction = ""
            

            

def execute_movement(figure):
    if figure == Var.hero:
        Var.ref_point[0] -= figure.frameway[0]
        Var.ref_point[1] -= figure.frameway[1]
        for cbm in Var.current_blitmaps:
            cbm.pos[0] -= figure.frameway[0]
            cbm.pos[1] -= figure.frameway[1]
        for g in Var.grounds.values():
            g.pos[0] -= figure.frameway[0]
            g.pos[1] -= figure.frameway[1]
        for bg in Var.backgrounds.values():
            bg.pos[0] -= figure.frameway[0]
            bg.pos[1] -= figure.frameway[1]
        for abg in Var.animated_backgrounds.values():
            abg.pos[0] -= figure.frameway[0]
            abg.pos[1] -= figure.frameway[1]
        for d in Var.decorations.values():
            if not "Darkness" in d.name:
                d.pos[0] -= figure.frameway[0]
                d.pos[1] -= figure.frameway[1]
                d.realpos[0] -= figure.frameway[0]
                d.realpos[1] -= figure.frameway[1]
                d.layerpos[0] -= figure.frameway[0]
                d.layerpos[1] -= figure.frameway[1]
        for ad in Var.animated_decorations.values():
            ad.pos[0] -= figure.frameway[0]
            ad.pos[1] -= figure.frameway[1]
            ad.realpos[0] -= figure.frameway[0]
            ad.realpos[1] -= figure.frameway[1]
            ad.layerpos[0] -= figure.frameway[0]
            ad.layerpos[1] -= figure.frameway[1]
        for ov in Var.overlays.values():
            ov.pos[0] -= figure.frameway[0]
            ov.pos[1] -= figure.frameway[1]
        for aov in Var.animated_overlays.values():
            aov.pos[0] -= figure.frameway[0]
            aov.pos[1] -= figure.frameway[1]
        for b in Var.borders.values():
            b.pos[0] -= figure.frameway[0]
            b.pos[1] -= figure.frameway[1]
            b.realpos[0] -= figure.frameway[0]
            b.realpos[1] -= figure.frameway[1]
            b.layerpos[0] -= figure.frameway[0]
            b.layerpos[1] -= figure.frameway[1]
        for o in Var.obstacles.values():
            o.pos[0] -= figure.frameway[0]
            o.pos[1] -= figure.frameway[1]
            o.realpos[0] -= figure.frameway[0]
            o.realpos[1] -= figure.frameway[1]
            o.layerpos[0] -= figure.frameway[0]
            o.layerpos[1] -= figure.frameway[1]
        for ao in Var.animated_obstacles.values():
            ao.pos[0] -= figure.frameway[0]
            ao.pos[1] -= figure.frameway[1]
            ao.realpos[0] -= figure.frameway[0]
            ao.realpos[1] -= figure.frameway[1]
            ao.layerpos[0] -= figure.frameway[0]
            ao.layerpos[1] -= figure.frameway[1]
        for do in Var.doors.values():
            do.pos[0] -= figure.frameway[0]
            do.pos[1] -= figure.frameway[1]
            do.realpos[0] -= figure.frameway[0]
            do.realpos[1] -= figure.frameway[1]
            do.layerpos[0] -= figure.frameway[0]
            do.layerpos[1] -= figure.frameway[1]
        for u in Var.units.values():
            u.pos[0] -= figure.frameway[0]
            u.pos[1] -= figure.frameway[1]
            u.realpos[0] -= figure.frameway[0]
            u.realpos[1] -= figure.frameway[1]
            u.layerpos[0] -= figure.frameway[0]
            u.layerpos[1] -= figure.frameway[1]
        for d in Var.dead:  #=Liste
            d.pos[0] -= figure.frameway[0]  # Bei dead wird Layerpos absichtlich nicht aktualisiert(Soll im Hintergrund bleiben)
            d.pos[1] -= figure.frameway[1]
        Var.go_point["pos"][0] -= figure.frameway[0]
        Var.go_point["pos"][1] -= figure.frameway[1]
    else:
        figure.pos[0] += figure.frameway[0]
        figure.pos[1] += figure.frameway[1]
        figure.realpos[0] += figure.frameway[0]
        figure.realpos[1] += figure.frameway[1]
        figure.layerpos[0] += figure.frameway[0]
        figure.layerpos[1] += figure.frameway[1]

    figure.current_absolute_pos = [figure.realpos[0] - Var.ref_point[0], figure.realpos[1] - Var.ref_point[1]]

    if not Var.hero.fighting:
        if len(figure.last_frameways) == 8:
            figure.last_frameways.pop()
        figure.last_frameways.insert(0, figure.frameway)
        x_waycheck = 0
        y_waycheck = 0
        for lf in figure.last_frameways:
            x_waycheck += abs(lf[0])
            y_waycheck += abs(lf[1])
            
        if (abs(x_waycheck)+abs(y_waycheck)) < 3:
            figure.frameway = [0, 0]
            figure.go = False
            if not figure == Var.hero:
                figure.start_standing = True
            figure.sounds["footsteps_sound"].stop()
            figure.footstep_sound_active = False
            if not figure.drawn:
                try:
                    figure.image = figure.current_pics["Stand"]
                except IndexError:
                    print("Pic-IndexError: 'Stand'")
            else:
                try:
                    figure.image = figure.current_pics["Fight_1"]
                except KeyError:
                    print("Pic-KeyError: 'Fight_1'")
                
    else:   # beim Kämpfen
        if not figure.frameway == [0,0]:
            Var.screen_scrolling_happened = True
            figure.frameway = [0,0]



        
