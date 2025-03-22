import pygame
import menuehandler
import pool
from pool import Var
from pool import Channels
import basic_types
import hero
import figure_functions
import slot
import os
import pickle


## class Loadvar
## execute_load()
## loadloop()
## draw_loader()
## load()


class Loadvar():
    pics = {}
    sounds = {}
    confirmed = False
    choice_showbox = slot.Slot("")
    somethings_choosen = False
    text_edit = False
    slot_deleted = False
    unchoose_all = True
    security_question_start = False
    security_question = ""
    security_question_text_image = None
    security_question_answered = False
    message_timer = pool.Count()
    message_blitted = False
    message_changing = False
    message_font = pygame.font.Font(None, 16)
    message_color = (190,230,160)
    message_load = message_font.render("GAME LOADED!", True, message_color)
    message_deleted = message_font.render("File deleted.", True, message_color)




def execute_load():

    #Var.IDG += 10000  #verhindert doppelte IDs
    Var.game_over = None

    file = open("savegames\\"+Loadvar.choice_showbox.text+".txt", "rb")
    loaddict = pickle.load(file)

    Var.ref_point = loaddict["ref_point"]
    Var.main_background = loaddict["main_background"]

    del Var.hero
    Var.hero = hero.Hero("Hero", "Hero", [175, 100], 255, loaddict["hero"]["ID"])

    Var.hero.absolute_destination = loaddict["hero"]["absolute_destination"]
    Var.hero.layerpos = loaddict["hero"]["layerpos"]
    Var.hero.transparency = loaddict["hero"]["transparency"]
    Var.hero.current_way = loaddict["hero"]["current_way"]
    Var.hero.dir = loaddict["hero"]["dir"]
    Var.hero.border_dir = loaddict["hero"]["border_dir"]
    Var.hero.walk_animation_progress = loaddict["hero"]["walk_animation_progress"]
    Var.hero.walk_animation_delay = loaddict["hero"]["walk_animation_delay"]
    Var.hero.walk_animation_frame_countdown = loaddict["hero"]["walk_animation_frame_countdown"]
    Var.hero.go = loaddict["hero"]["go"]
    Var.hero.start_going = loaddict["hero"]["start_going"]
    Var.hero.frameway = loaddict["hero"]["frameway"]
    Var.hero.movement_skip_at_frame = loaddict["hero"]["movement_skip_at_frame"]
    Var.hero.movement_skip_countdown = loaddict["hero"]["movement_skip_countdown"]
    Var.hero.speed = loaddict["hero"]["speed"]
    Var.hero.last_frameways = loaddict["hero"]["last_frameways"]
    Var.hero.drawn = loaddict["hero"]["drawn"]
    Var.hero.draw_pressed = loaddict["hero"]["draw_pressed"]
    Var.hero.drawing = loaddict["hero"]["drawing"]
    Var.hero.putting_away = loaddict["hero"]["putting_away"]
    Var.hero.current_drawing_pic_nr = loaddict["hero"]["current_drawing_pic_nr"]
    Var.hero.draw_animation_pic_countdown = loaddict["hero"]["draw_animation_pic_countdown"]
    Var.hero.current_fightwalk_pic_nr = loaddict["hero"]["current_fightwalk_pic_nr"]
    Var.hero.fightwalk_animation_pic_countdown = loaddict["hero"]["fightwalk_animation_pic_countdown"]
    Var.hero.current_pics.clear()
    if not (Var.hero.drawing or Var.hero.putting_away):
        if not Var.hero.drawn:
            Var.hero.current_pics["Stand"] = pygame.image.load(Var.path+"\\pics\\"+Var.hero.name.split('_')[0]+'\\'+Var.hero.name+"_"+Var.hero.dir+"_Stand.png").convert_alpha()
            Var.hero.current_pics["Go_R1"] = pygame.image.load(Var.path+"\\pics\\"+Var.hero.name.split('_')[0]+'\\'+Var.hero.name+"_"+Var.hero.dir+"_Go_R1.png").convert_alpha()
            Var.hero.current_pics["Go_R2"] = pygame.image.load(Var.path+"\\pics\\"+Var.hero.name.split('_')[0]+'\\'+Var.hero.name+"_"+Var.hero.dir+"_Go_R2.png").convert_alpha()
            Var.hero.current_pics["Go_L1"] = pygame.image.load(Var.path+"\\pics\\"+Var.hero.name.split('_')[0]+'\\'+Var.hero.name+"_"+Var.hero.dir+"_Go_L1.png").convert_alpha()
            Var.hero.current_pics["Go_L2"] = pygame.image.load(Var.path+"\\pics\\"+Var.hero.name.split('_')[0]+'\\'+Var.hero.name+"_"+Var.hero.dir+"_Go_L2.png").convert_alpha()
        else:
            Var.hero.current_pics["Fight_1"] = pygame.image.load(Var.path+"\\pics\\"+Var.hero.name.split('_')[0]+'\\Fight\\'+Var.hero.name+"_"+Var.hero.dir+"_Fight_1.png").convert_alpha()
            Var.hero.current_pics["Fight_2"] = pygame.image.load(Var.path+"\\pics\\"+Var.hero.name.split('_')[0]+'\\Fight\\'+Var.hero.name+"_"+Var.hero.dir+"_Fight_2.png").convert_alpha()
            Var.hero.current_pics["Fight_3"] = pygame.image.load(Var.path+"\\pics\\"+Var.hero.name.split('_')[0]+'\\Fight\\'+Var.hero.name+"_"+Var.hero.dir+"_Fight_3.png").convert_alpha()
            Var.hero.current_pics["Fight_4"] = pygame.image.load(Var.path+"\\pics\\"+Var.hero.name.split('_')[0]+'\\Fight\\'+Var.hero.name+"_"+Var.hero.dir+"_Fight_4.png").convert_alpha()
            Var.hero.current_pics["Fight_5"] = pygame.image.load(Var.path+"\\pics\\"+Var.hero.name.split('_')[0]+'\\Fight\\'+Var.hero.name+"_"+Var.hero.dir+"_Fight_5.png").convert_alpha()
            Var.hero.current_pics["Fight_6"] = pygame.image.load(Var.path+"\\pics\\"+Var.hero.name.split('_')[0]+'\\Fight\\'+Var.hero.name+"_"+Var.hero.dir+"_Fight_6.png").convert_alpha()
            Var.hero.current_pics["Fight_7"] = pygame.image.load(Var.path+"\\pics\\"+Var.hero.name.split('_')[0]+'\\Fight\\'+Var.hero.name+"_"+Var.hero.dir+"_Fight_7.png").convert_alpha()
    else:
        Var.hero.current_pics["Draw_1"] = pygame.image.load(Var.path+"\\pics\\"+Var.hero.name.split('_')[0]+'\\Draw\\'+Var.hero.name+"_"+Var.hero.dir+"_Draw_1.png").convert_alpha()
        Var.hero.current_pics["Draw_2"] = pygame.image.load(Var.path+"\\pics\\"+Var.hero.name.split('_')[0]+'\\Draw\\'+Var.hero.name+"_"+Var.hero.dir+"_Draw_2.png").convert_alpha()
        Var.hero.current_pics["Draw_3"] = pygame.image.load(Var.path+"\\pics\\"+Var.hero.name.split('_')[0]+'\\Draw\\'+Var.hero.name+"_"+Var.hero.dir+"_Draw_3.png").convert_alpha()
        Var.hero.current_pics["Draw_4"] = pygame.image.load(Var.path+"\\pics\\"+Var.hero.name.split('_')[0]+'\\Draw\\'+Var.hero.name+"_"+Var.hero.dir+"_Draw_4.png").convert_alpha()
        Var.hero.current_pics["Draw_5"] = pygame.image.load(Var.path+"\\pics\\"+Var.hero.name.split('_')[0]+'\\Draw\\'+Var.hero.name+"_"+Var.hero.dir+"_Draw_5.png").convert_alpha()
        Var.hero.current_pics["Draw_6"] = pygame.image.load(Var.path+"\\pics\\"+Var.hero.name.split('_')[0]+'\\Draw\\'+Var.hero.name+"_"+Var.hero.dir+"_Draw_6.png").convert_alpha()
        Var.hero.current_pics["Draw_7"] = pygame.image.load(Var.path+"\\pics\\"+Var.hero.name.split('_')[0]+'\\Draw\\'+Var.hero.name+"_"+Var.hero.dir+"_Draw_7.png").convert_alpha()
        Var.hero.current_pics["Draw_8"] = pygame.image.load(Var.path+"\\pics\\"+Var.hero.name.split('_')[0]+'\\Draw\\'+Var.hero.name+"_"+Var.hero.dir+"_Draw_8.png").convert_alpha()
        Var.hero.current_pics["Draw_9"] = pygame.image.load(Var.path+"\\pics\\"+Var.hero.name.split('_')[0]+'\\Draw\\'+Var.hero.name+"_"+Var.hero.dir+"_Draw_9.png").convert_alpha()
        Var.hero.current_pics["Draw_10"] = pygame.image.load(Var.path+"\\pics\\"+Var.hero.name.split('_')[0]+'\\Draw\\'+Var.hero.name+"_"+Var.hero.dir+"_Draw_10.png").convert_alpha()
        Var.hero.current_pics["Draw_11"] = pygame.image.load(Var.path+"\\pics\\"+Var.hero.name.split('_')[0]+'\\Draw\\'+Var.hero.name+"_"+Var.hero.dir+"_Draw_11.png").convert_alpha()
        Var.hero.current_pics["Draw_12"] = pygame.image.load(Var.path+"\\pics\\"+Var.hero.name.split('_')[0]+'\\Draw\\'+Var.hero.name+"_"+Var.hero.dir+"_Draw_12.png").convert_alpha()
        Var.hero.current_pics["Draw_13"] = pygame.image.load(Var.path+"\\pics\\"+Var.hero.name.split('_')[0]+'\\Draw\\'+Var.hero.name+"_"+Var.hero.dir+"_Draw_13.png").convert_alpha()
        Var.hero.current_pics["Draw_14"] = pygame.image.load(Var.path+"\\pics\\"+Var.hero.name.split('_')[0]+'\\Draw\\'+Var.hero.name+"_"+Var.hero.dir+"_Draw_14.png").convert_alpha()
        Var.hero.current_pics["Draw_15"] = pygame.image.load(Var.path+"\\pics\\"+Var.hero.name.split('_')[0]+'\\Draw\\'+Var.hero.name+"_"+Var.hero.dir+"_Draw_15.png").convert_alpha()


    Var.current_blitmaps.clear()
    Var.grounds.clear()
    Var.backgrounds.clear()
    Var.decorations.clear()
    Var.animated_decorations.clear()
    Var.overlays.clear()
    Var.animated_overlays.clear()
    Var.borders.clear()
    Var.obstacles.clear()
    Var.animated_obstacles.clear()
    Var.doors.clear()
    Var.units.clear()

            
    for cb in loaddict["cbs"]:
##        if cb in ids:    #  Blitmaps können nur vom typ "Basic" sein
        Var.current_blitmaps.append(basic_types.Basic\
                                    (loaddict["cbs"][cb]["name"], \
                                     "", \
                                     loaddict["cbs"][cb]["pos"], \
                                     ID=cb)) 


    for g in loaddict["grounds"]: 
        if loaddict["grounds"][g]["typ"] == "Ground":
            Var.grounds[g] = basic_types.Basic\
                             (loaddict["grounds"][g]["name"],\
                              loaddict["grounds"][g]["typ"], \
                              loaddict["grounds"][g]["pos"], \
                              loaddict["grounds"][g]["transparency"], \
                              ID=g)
        else:
            print("ERROR: loaded typ unknown (in grounds)- so couldn't load it!")
        Var.grounds[g].realpos = loaddict["grounds"][g]["realpos"]


    for bg in loaddict["bgs"]: 
        if loaddict["bgs"][bg]["typ"] == "Background":
            Var.backgrounds[bg] = basic_types.Basic\
                                  (loaddict["bgs"][bg]["name"], \
                                   loaddict["bgs"][bg]["typ"], \
                                   loaddict["bgs"][bg]["pos"], \
                                   loaddict["bgs"][bg]["transparency"], \
                                   ID=bg)
        else:
            print("ERROR: loaded typ unknown (in bgs)- so couldn't load it!")
        Var.backgrounds[bg].realpos = loaddict["bgs"][bg]["realpos"]



    for abg in loaddict["abgs"]: 
        if loaddict["abgs"][abg]["typ"] == "Animated_Background":
            Var.animated_backgrounds[abg] = basic_types.Animated_Notmasked\
                                   (loaddict["abgs"][abg]["name"], \
                                    loaddict["abgs"][abg]["typ"], \
                                    loaddict["abgs"][abg]["pos"], \
                                    loaddict["abgs"][abg]["quantity"], \
                                    loaddict["abgs"][abg]["rate_duration"], \
                                    loaddict["abgs"][abg]["chaos"], \
                                    loaddict["abgs"][abg]["transparency"], \
                                    ID=abg)
        else:
            print("ERROR: loaded typ unknown (in abgs)- so couldn't load it!")
        Var.animated_backgrounds[abg].realpos = loaddict["abgs"][abg]["realpos"]
        Var.animated_backgrounds[abg].current_pic = loaddict["abgs"][abg]["current_pic"]
        Var.animated_backgrounds[abg].last_pictime = loaddict["abgs"][abg]["last_pictime"]
        
    for abg in Var.animated_backgrounds.values():
        if abg.name == "Water":
            abg.width = 100
            abg.height = 100


            
    for d in loaddict["decs"]:
        if loaddict["decs"][d]["typ"] == "Decoration":
            Var.decorations[d] = basic_types.Basic\
                                 (loaddict["decs"][d]["name"], \
                                  loaddict["decs"][d]["typ"], \
                                  loaddict["decs"][d]["pos"], \
                                  loaddict["decs"][d]["transparency"], \
                                  ID=d)
        else:
            print("ERROR: loaded typ unknown (in decs)- so couldn't load it!")
        Var.decorations[d].realpos = loaddict["decs"][d]["realpos"]

        

    for ad in loaddict["adecs"]:
        if loaddict["adecs"][ad]["typ"] == "Animated_Decoration":
            Var.animated_decorations[ad] = basic_types.Animated_Notmasked\
                                           (loaddict["adecs"][ad]["name"], \
                                            loaddict["adecs"][ad]["typ"], \
                                            loaddict["adecs"][ad]["pos"], \
                                            loaddict["adecs"][ad]["quantity"], \
                                            loaddict["adecs"][ad]["rate_duration"], \
                                            loaddict["adecs"][ad]["chaos"], \
                                            loaddict["adecs"][ad]["transparency"], \
                                            ID=ad)
        else:
            print("ERROR: loaded typ unknown (in adecs) - so couldn't load it!")
        Var.animated_decorations[ad].realpos = loaddict["adecs"][ad]["realpos"]
        Var.animated_decorations[ad].current_pic = loaddict["adecs"][ad]["current_pic"]
        Var.animated_decorations[ad].last_pictime = loaddict["adecs"][ad]["last_pictime"]

                                                                      

    for ov in loaddict["ovs"]:
        if loaddict["ovs"][ov]["typ"] == "Overlay":
            Var.overlays[ov] = basic_types.Basic\
                               (loaddict["ovs"][ov]["name"], \
                                loaddict["ovs"][ov]["typ"], \
                                loaddict["ovs"][ov]["pos"], \
                                loaddict["ovs"][ov]["transparency"], \
                                ID=ov)
        else:
            print("ERROR: loaded typ unknown (in ovs)- so couldn't load it!")
        Var.overlays[ov].realpos = loaddict["ovs"][ov]["realpos"]



    for aov in loaddict["aovs"]:
        if loaddict["aovs"][aov]["typ"] == "Animated_Overlay":
            Var.animated_overlays[aov] = basic_types.Animated_Notmasked\
                                         (loaddict["aovs"][aov]["name"], \
                                          loaddict["aovs"][aov]["typ"], \
                                          loaddict["aovs"][aov]["pos"], \
                                          loaddict["aovs"][aov]["quantity"], \
                                          loaddict["aovs"][aov]["rate_duration"], \
                                          loaddict["aovs"][aov]["chaos"], \
                                          loaddict["aovs"][aov]["transparency"], \
                                          ID=aov)
        else:
            print("ERROR: loaded typ unknown (in aovs) - so couldn't load it!")
        Var.animated_overlays[aov].realpos = loaddict["aovs"][aov]["realpos"]
        Var.animated_overlays[aov].current_pic = loaddict["aovs"][aov]["current_pic"]
        Var.animated_overlays[aov].last_pictime = loaddict["aovs"][aov]["last_pictime"]


            
    for b in loaddict["borders"]:
        if loaddict["borders"][b]["typ"] == "Border":
            Var.borders[b] = basic_types.Border\
                             (loaddict["borders"][b]["name"], \
                              loaddict["borders"][b]["typ"], \
                              loaddict["borders"][b]["pos"], \
                             # loaddict["borders"][b]["location"], \
                              loaddict["borders"][b]["transparency"], \
                              ID=b)
        elif loaddict["borders"][b]["typ"] == "High_border":
            Var.borders[b] = basic_types.High_border\
                             (loaddict["borders"][b]["name"], \
                              loaddict["borders"][b]["typ"], \
                              loaddict["borders"][b]["pos"], \
                             # loaddict["borders"][b]["location"], \
                              loaddict["borders"][b]["transparency"], \
                              ID=b)
##            print(Var.borders[b].name+str(Var.borders[b].ID), "at absolute_pos  X =", Var.borders[b].pos[0]-Var.ref_point[0], ",  Y =", Var.borders[b].pos[1]-Var.ref_point[1], ":",\
##                  "\ntyp:", Var.borders[b].typ, "transparency:", Var.borders[b].transparency, "transparent:", Var.borders[b].transparent)
            if Var.borders[b].transparency < 200:
                Var.borders[b].transparent = True
        else:
            print("ERROR: loaded typ unknown (in borders) - so couldn't load it!")
        Var.borders[b].realpos = loaddict["borders"][b]["realpos"]
        

            
    for o in loaddict["obs"]:
##        if o in ids:
        if loaddict["obs"][o]["typ"] == "Obstacle":
            Var.obstacles[o] = basic_types.Obstacle\
                             (loaddict["obs"][o]["name"], \
                              loaddict["obs"][o]["typ"], \
                              loaddict["obs"][o]["pos"], \
                              [loaddict["obs"][o]["realpos"][0]-loaddict["obs"][o]["pos"][0], loaddict["obs"][o]["realpos"][1]-loaddict["obs"][o]["pos"][1]], \
                              loaddict["obs"][o]["transparency"], \
                              ID=o)
        elif loaddict["obs"][o]["typ"] == "High_obstacle":
            Var.obstacles[o] = basic_types.High_obstacle\
                              (loaddict["obs"][o]["name"], \
                               loaddict["obs"][o]["typ"], \
                               loaddict["obs"][o]["pos"], \
                               [loaddict["obs"][o]["realpos"][0]-loaddict["obs"][o]["pos"][0], loaddict["obs"][o]["realpos"][1]-loaddict["obs"][o]["pos"][1]], \
                               loaddict["obs"][o]["transparency"], \
                               ID=o)
        elif loaddict["obs"][o]["typ"] == "Inclined_high_obstacle":
            Var.obstacles[o] = basic_types.Inclined_high_obstacle\
                              (loaddict["obs"][o]["name"], \
                               loaddict["obs"][o]["typ"], \
                               loaddict["obs"][o]["pos"], \
                               loaddict["obs"][o]["L_y_offset"], \
                               loaddict["obs"][o]["R_y_offset"], \
                               loaddict["obs"][o]["x_offset"], \
                               loaddict["obs"][o]["transparency"], \
                               ID=o)
            #  hier zukünftig weitere elifs (typen) eintragen
        else:
            print("ERROR: loaded typ unknown (in obs) - so couldn't load it!")
        Var.obstacles[o].realpos = loaddict["obs"][o]["realpos"]
        if (issubclass(type(Var.obstacles[o]), basic_types.High_obstacle)) or (type(Var.obstacles[o]) == basic_types.High_obstacle):
            Var.obstacles[o].transparent = loaddict["obs"][o]["transparent"]


    for ao in loaddict["aobs"]:
        if loaddict["aobs"][ao]["typ"] == "Animated_obstacle":
            Var.animated_obstacles[ao] = basic_types.Animated_obstacle\
                                       (loaddict["aobs"][ao]["name"], \
                                        loaddict["aobs"][ao]["typ"], \
                                        loaddict["aobs"][ao]["pos"], \
                                        [loaddict["aobs"][ao]["realpos"][0]-loaddict["aobs"][ao]["pos"][0], loaddict["aobs"][ao]["realpos"][1]-loaddict["aobs"][ao]["pos"][1]], \
                                        loaddict["aobs"][ao]["quantity"], \
                                        loaddict["aobs"][ao]["rate_duration"], \
                                        loaddict["aobs"][ao]["chaos"], \
                                        loaddict["aobs"][ao]["transparency"], \
                                        ID=ao)
        else:
            print("ERROR: loaded typ unknown (in aobs) - so couldn't load it!")
        Var.animated_obstacles[ao].realpos = loaddict["aobs"][ao]["realpos"]
        Var.animated_obstacles[ao].current_pic = loaddict["aobs"][ao]["current_pic"]
        Var.animated_obstacles[ao].last_pictime = loaddict["aobs"][ao]["last_pictime"]

    for do in loaddict["doors"]:
        if loaddict["doors"][do]["typ"] == "Door":
            Var.doors[do] = basic_types.Door\
                            (loaddict["doors"][do]["name"], \
                             loaddict["doors"][do]["typ"], \
                             loaddict["doors"][do]["pos"], \
                             [loaddict["doors"][do]["realpos"][0]-loaddict["doors"][do]["pos"][0], loaddict["doors"][do]["realpos"][1]-loaddict["doors"][do]["pos"][1]], \
                             loaddict["doors"][do]["quantity"], \
                             loaddict["doors"][do]["rate_duration"], \
                             loaddict["doors"][do]["chaos"], \
                             loaddict["doors"][do]["transparency"], \
                             ID=do)
        else:
            print("ERROR: loaded typ unknown (in doors) - so couldn't load it!")
        Var.doors[do].realpos = loaddict["doors"][do]["realpos"]
        Var.doors[do].current_pic = loaddict["doors"][do]["current_pic"]
        Var.doors[do].last_pictime = loaddict["doors"][do]["last_pictime"]
        Var.doors[do].dir = loaddict["doors"][do]["dir"]
        Var.doors[do].status = loaddict["doors"][do]["status"]
        Var.doors[do].in_focus = loaddict["doors"][do]["in_focus"]
        Var.doors[do].welcome_point = loaddict["doors"][do]["welcome_point"]
        Var.doors[do].reload_maskpic()
        for i in range(Var.doors[do].quantity):
            Var.doors[do].images[i+1] = pygame.image.load(Var.path+'\\pics\\Objects\\'+Var.doors[do].name.split('_')[0]+'\\'+\
                                                          Var.doors[do].name+'_'+Var.doors[do].dir+'-'+str(i+1)+'.png').convert()
            Var.doors[do].images[i+1].set_colorkey([0,0,0], pygame.RLEACCEL)
            Var.doors[do].images[i+1].set_alpha(Var.doors[do].transparency, pygame.RLEACCEL)


    for u in loaddict["units"]:
##        if u in ids:
        if loaddict["units"][u]["typ"] == "Character":
            Var.units[u] = basic_types.Character\
                           (loaddict["units"][u]["name"], \
                            loaddict["units"][u]["typ"], \
                            loaddict["units"][u]["pos"], \
                            loaddict["units"][u]["transparency"], \
                            ID=u)
        #  Hier weitere elifs mit Typen hinzufügen (sobald vorhanden)
        else:
            print("ERROR: loaded type unknown (in units) - so couldn't load it!")
        if (issubclass(type(Var.units[u]), basic_types.Character)) or (type(Var.units[u]) == basic_types.Character):
            Var.units[u].realpos = loaddict["units"][u]["realpos"]
            Var.units[u].layerpos = loaddict["units"][u]["layerpos"]
            Var.units[u].absolute_destination = loaddict["units"][u]["absolute_destination"]
            Var.units[u].current_way = loaddict["units"][u]["current_way"]
            Var.units[u].dir = loaddict["units"][u]["dir"]
            Var.units[u].border_dir = loaddict["units"][u]["border_dir"]
            Var.units[u].walk_animation_progress = loaddict["units"][u]["walk_animation_progress"]
            Var.units[u].walk_animation_delay = loaddict["units"][u]["walk_animation_delay"]
            Var.units[u].walk_animation_frame_countdown = loaddict["units"][u]["walk_animation_frame_countdown"]
            Var.units[u].go = loaddict["units"][u]["go"]
            Var.units[u].start_going = loaddict["units"][u]["start_going"]
            Var.units[u].frameway = loaddict["units"][u]["frameway"]
            Var.units[u].movement_skip_at_frame = loaddict["units"][u]["movement_skip_at_frame"]
            Var.units[u].movement_skip_countdown = loaddict["units"][u]["movement_skip_countdown"]
            Var.units[u].speed = loaddict["units"][u]["speed"]
            Var.units[u].last_frameways = loaddict["units"][u]["last_frameways"]         

    Var.blitlist.clear()
    Var.blitlist.append(Var.hero)
    #figure_functions.reload_pics(Var.hero)
##    for u in Var.units:
##        figure_functions.reload_pics(u)
    
    del loaddict
    del file
    
    
##    print("          ! ! !\n")
##    print("___________________________")
##    print("---------------------------")
##    print("###########################")
##    print("###########################")
##    print("---------------------------\n")
##    print("STATUS AFTER LOADING")
##    print(Loadvar.choice_showbox.text,"\n")
##    print("_____________________")
##    print("---------------------")
##    print("Var.IDG: ", Var.IDG)
##    print("ref_point: ", Var.ref_point)
##    print("_____________________")
##    print("---------------------")
##    print("\n")
##    print("HERO:")
##    print("ID: ", Var.hero.ID)
##    print("absolute_destination: ", Var.hero.absolute_destination)
##    print("current_way: ", Var.hero.current_way)
##    print("dir: ", Var.hero.dir)
##    print("walk_animation_progress: ", Var.hero.walk_animation_progress)
##    print("walk_animation_delay: ", Var.hero.walk_animation_delay)
##    print("walk_animation_frame_countdown: ", Var.hero.walk_animation_frame_countdown)
##    print("go: ", Var.hero.go)
##    print("start_going: ", Var.hero.start_going)
##    print("frameway: ", Var.hero.frameway)
##    print("movement_skip_at_frame: ", Var.hero.movement_skip_at_frame)
##    print("movement_skip_countdown: ", Var.hero.movement_skip_countdown)
##    print("speed: ", Var.hero.speed)
##    print("last_frameways: ", Var.hero.last_frameways)
##    print()
##    print("____________________________")
##    print("----------------------------")
##    print()
##
##    if Var.current_blitmaps:
##        print("CURRENT BLITMAPS:")
##        print("_________________")
##        print()
##        a = 1
##        for cb in Var.current_blitmaps:
##            print("current_blitmap nr.", a, ":", sep="")
##            a += 1
##            print("ID: ", cb.ID)
##            print("name: ", cb.name)
##            print("pos: ", cb.pos, "\n")
##    else:
##        print("NO current blitmaps!!!")
##    print()
##    print("____________________________")
##    print("----------------------------")
##    print()
##
##    if Var.decorations:
##        print("DECORATIONS:")
##        print("_________________")
##        print()
##        a = 1
##        for d in Var.decorations:
##            print("decoration nr.", a, sep="")
##            a += 1
##            print("ID (dict_key): ", d)
##            print("ID (ID_attr.): ", Var.decorations[d].ID)
##            print("type: ", Var.decorations[d].type)
##            print("name: ", Var.decorations[d].name)
##            print("pos: ", Var.decorations[d].pos)
##    else:
##        print("NO decorations!!!")
##    print()
##    print("____________________________")
##    print("----------------------------")
##    print()
##
##    if Var.obstacles:
##        print("obstacles:")
##        print("_________________")
##        print()
##        a = 1
##        for o in Var.obstacles:
##            print("object nr.", a, sep="")
##            a += 1
##            print("ID (dict_key): ", o)
##            print("ID (ID_attr.): ", Var.obstacles[o].ID)
##            print("type: ", Var.obstacles[o].type)
##            print("name: ", Var.obstacles[o].name)
##            print("pos: ", Var.obstacles[o].pos)
##            print("realpos: ", Var.obstacles[o].realpos)
##            if (issubclass(type(Var.obstacles[o]), basic_types.High_obstacle)) or (type(Var.obstacles[o]) == basic_types.High_obstacle):
##                print("transparent: ", Var.obstacles[o].transparent)
##            if type(Var.obstacles[o]) == basic_types.Inclined_high_obstacle:
##                print("L_y_offset: ", Var.obstacles[o].L_y_offset)
##                print("R_y_offset: ", Var.obstacles[o].R_y_offset)
##                print("x_offset: ", Var.obstacles[o].x_offset)
##    else:
##        print("NO obstacles!!!")
##    print()
##    print("____________________________")
##    print("----------------------------")
##    print()
##
##    if Var.units:
##        print("UNITS:")
##        print("_________________")
##        print()
##        a = 1
##        for u in Var.units:
##            print("unit nr.", a, sep="")
##            a += 1
##            print("ID (dict_key): ", u)
##            print("ID (ID_attr.): ", Var.units[u].ID)
##            print("type: ", Var.units[u].type)
##            print("name: ", Var.units[u].name)
##            print("pos: ", Var.units[u].pos)
##            print("realpos: ", Var.units[u].realpos)
##            print("absolute_destination: ", Var.units[u].absolute_destination)
##            print("current_way: ", Var.units[u].current_way)
##            print("dir: ", Var.units[u].dir)
##            print("walk_animation_progress: ", Var.units[u].walk_animation_progress)
##            print("walk_animation_delay: ", Var.units[u].walk_animation_delay)
##            print("walk_animation_frame_countdown: ", Var.units[u].walk_animation_frame_countdown)
##            print("go: ", Var.units[u].go)
##            print("start_going: ", Var.units[u].start_going)
##            print("frameway: ", Var.units[u].frameway)
##            print("movement_skip_at_frame: ", Var.units[u].movement_skip_at_frame)
##            print("movement_skip_countdown: ", Var.units[u].movement_skip_countdown)
##            print("speed: ", Var.units[u].speed)
##            print("last_frameways: ", Var.units[u].last_frameways)
##    else:
##        print("NO units!!!")
##    print()
##    print("____________________________")
##    print("----------------------------")
##    print()
##    del a
##    print("____________________________")
##    print("||||||||||||||||||||||||||||")
##    print("END OF STATUS AFTER LOADING SCRIPT")
##    print(Loadvar.choice_showbox.text)
##    print("||||||||||||||||||||||||||||")
##    print("____________________________")
##    print("----------------------------")
##    print("############################")
##    print("############################")
##    print("############################\n\n\n")




def loadloop():
    
    for e in pygame.event.get():
        if e.type == pygame.MOUSEMOTION:
            for s in slot.Slotvar.slots:
                if (e.pos[0] in range(s.pos[0], s.pos[0]+100)) and (e.pos[1] in range(s.pos[1], s.pos[1]+16)):
                    if not s.highlighted:
                        s.highlighted = True
                        s.getting_light = True
                elif s.highlighted:
                    s.removing_light = True
            for m in slot.Slotvar.menue_buttons.values():
                if m.active and m.pressed and not ((e.pos[0] in range(m.pos[0], m.pos[0]+50)) and (e.pos[1] in range(m.pos[1], m.pos[1]+15))):
                    m.pressed = False
                    m.changing_status = "active"
                    
        if e.type == pygame.MOUSEBUTTONUP:
            if not Loadvar.unchoose_all:
                Loadvar.unchoose_all = True
            for s in slot.Slotvar.slots:
                if (e.pos[0] in range(s.pos[0], s.pos[0]+100)) and (e.pos[1] in range(s.pos[1], s.pos[1]+16)):
                    Loadvar.unchoose_all = False
                    if not s.choosen:
                        s.choosen = True
                        s.getting_light = True
                        Channels.mouse_sounds.play(Loadvar.sounds["click"])
                        s.highlighted = False
                    if not (s.text == Loadvar.choice_showbox.text):
                        Loadvar.text_edit = True
                        Loadvar.choice_showbox.text = s.text
            for m in slot.Slotvar.menue_buttons.values():
                if ((e.pos[0] in range(m.pos[0], m.pos[0]+50)) and (e.pos[1] in range(m.pos[1], m.pos[1]+15))):
                    Loadvar.unchoose_all = False
            if Loadvar.unchoose_all:
                Loadvar.text_edit = True
                Loadvar.choice_showbox.text = ""
            for m in slot.Slotvar.menue_buttons.values():
                if m.active and m.pressed and ((e.pos[0] in range(m.pos[0], m.pos[0]+50)) and (e.pos[1] in range(m.pos[1], m.pos[1]+15))):
                    if m.text == "LOAD":
                        for s in slot.Slotvar.slots:
                            if s.choosen:
                                Loadvar.security_question = "Not saved data will be lost! Load '"+s.text+"'?"
                                Loadvar.security_question_start = True
                                if Loadvar.message_timer.count_name != "loaded":
                                    Loadvar.message_changing = True
                                Loadvar.message_timer.start_count(1500, "loaded")
                                Channels.signals.play(Loadvar.sounds["confirm"])
                                #Ladevorgang geschieht erst bei positiver Bestätigung der Security Question (siehe ganz unten)
                                
                    elif m.text == "DELETE":
                        for s in slot.Slotvar.slots:
                            if s.choosen:
                                Loadvar.security_question = "Are you sure you want to delete '"+s.text+"'?"
                        Loadvar.security_question_start = True

                    elif m.text == "CANCEL":
                        Loadvar.confirmed = True

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                Loadvar.confirmed = True
                menuehandler.Menuvar.esc_used = True
    pygame.event.pump()




                
                

def draw_loader():
    
    if menuehandler.Menuvar.saving_or_loading_is_starting:
        Loadvar.pics["Background"] = pygame.image.load(Var.path+"\\pics\\Load_Background.png").convert()
        Loadvar.pics["Message_Background"] = pygame.image.load(Var.path+"\\pics\\Load_Message_Background.png").convert()
        Loadvar.pics["Slot"] = pygame.image.load(Var.path+"\\pics\\Slot.png").convert()
        Loadvar.pics["Slot_Highlight"] = pygame.image.load(Var.path+"\\pics\\Slot_Highlight.png").convert()
        Loadvar.pics["Slot_Highlight"].set_colorkey([0,0,0], pygame.RLEACCEL)
        
        Loadvar.pics["Slot_Chooselight"] = pygame.image.load(Var.path+"\\pics\\Slot_Chooselight.png").convert()
        Loadvar.pics["Slot_Chooselight"].set_colorkey([0,0,0], pygame.RLEACCEL)

        Loadvar.pics["Active_Menue_Button"]  = pygame.image.load(Var.path+"\\pics\\Active_Save_Load_Menue_Button.png").convert()
        Loadvar.pics["Inactive_Menue_Button"]  = pygame.image.load(Var.path+"\\pics\\Inactive_Save_Load_Menue_Button.png").convert()
        Loadvar.pics["Pressed_Menue_Button"]  = pygame.image.load(Var.path+"\\pics\\Pressed_Save_Load_Menue_Button.png").convert()

        Var.screen.blit(Loadvar.pics["Background"], [0,0])
        for s in slot.Slotvar.slots:
            Var.screen.blit(Loadvar.pics["Slot"], s.pos)
            Var.screen.blit(s.text_image, [s.pos[0]+5, s.pos[1]+2])
        Var.screen.blit(Loadvar.pics["Slot"], [270, 300]) # Show_Box!
        for m in slot.Slotvar.menue_buttons.values():
            if m.text == "CANCEL":
                Var.screen.blit(Loadvar.pics["Active_Menue_Button"], m.pos)
                Var.screen.blit(m.active_text_image, [m.pos[0]+25-(int(len(m.text)*3.5)), m.pos[1]+2])
                
            else:
                Var.screen.blit(Loadvar.pics["Inactive_Menue_Button"], m.pos)
                Var.screen.blit(m.inactive_text_image, [m.pos[0]+25-(int(len(m.text)*3.5)), m.pos[1]+2])

    if Loadvar.text_edit:
        Loadvar.text_edit = False
        Var.screen.blit(Loadvar.pics["Slot"], [270, 300])
        Loadvar.choice_showbox.text_image = slot.Slotvar.slot_font.render(Loadvar.choice_showbox.text, True, slot.Slotvar.slot_text_color)
        Var.screen.blit(Loadvar.choice_showbox.text_image, [273, 301])

    if Loadvar.slot_deleted or Loadvar.security_question_answered:
        Channels.signals.play(Loadvar.sounds["confirm"])
        if Loadvar.slot_deleted:
            for s in slot.Slotvar.slots:
                if slot.Slotvar.slots.index(s) <= 8:
                    s.pos[0] = 100
                elif slot.Slotvar.slots.index(s) <= 17:
                    s.pos[0] = 270
                elif slot.Slotvar.slots.index(s) <= 26:
                    s.pos[0] = 440
                if slot.Slotvar.slots.index(s) in [0,9,18]:
                    s.pos[1] = 60
                elif slot.Slotvar.slots.index(s) in [1,10,19]:
                    s.pos[1] = 85
                elif slot.Slotvar.slots.index(s) in [2,11,20]:
                    s.pos[1] = 110
                elif slot.Slotvar.slots.index(s) in [3,12,21]:
                    s.pos[1] = 135
                elif slot.Slotvar.slots.index(s) in [4,13,22]:
                    s.pos[1] = 160
                elif slot.Slotvar.slots.index(s) in [5,14,23]:
                    s.pos[1] = 185
                elif slot.Slotvar.slots.index(s) in [6,15,24]:
                    s.pos[1] = 210
                elif slot.Slotvar.slots.index(s) in [7,16,25]:
                    s.pos[1] = 235
                elif slot.Slotvar.slots.index(s) in [8,17,26]:
                    s.pos[1] = 260

        Var.screen.blit(Loadvar.pics["Background"], [0,0])
        for s in slot.Slotvar.slots:
            Var.screen.blit(Loadvar.pics["Slot"], s.pos)
            Var.screen.blit(s.text_image, [s.pos[0]+5, s.pos[1]+2])
        Var.screen.blit(Loadvar.pics["Slot"], [270, 300]) # Input_Box!
        if not Loadvar.slot_deleted and not (Loadvar.security_question_answered == "loaded!"):
            Var.screen.blit(Loadvar.choice_showbox.text_image, [273, 301])
            Loadvar.security_question_answered = False
        else:
            Loadvar.somethings_choosen = False
            Loadvar.choice_showbox.text = ""
            Loadvar.slot_deleted = False
            Loadvar.security_question_answered = False
        for m in slot.Slotvar.menue_buttons.values():
            if m.active:
                Var.screen.blit(Loadvar.pics["Active_Menue_Button"], m.pos)
                Var.screen.blit(m.active_text_image, [m.pos[0]+25-(int(len(m.text)*3.5)), m.pos[1]+2])
            else:
                Var.screen.blit(Loadvar.pics["Inactive_Menue_Button"], m.pos)
                Var.screen.blit(m.inactive_text_image, [m.pos[0]+25-(int(len(m.text)*3.5)), m.pos[1]+2])

    if Loadvar.message_timer.check_if_ending():
        Var.screen.blit(Loadvar.pics["Message_Background"], [0, 322])
        Loadvar.message_blitted = False
    elif Loadvar.message_timer.counting and not Loadvar.message_blitted:
        if not Loadvar.message_changing:
            Loadvar.message_blitted = True
        else:
            Var.screen.blit(Loadvar.pics["Message_Background"], [0, 322])
            Loadvar.message_changing = False
        if Loadvar.message_timer.count_name == "loaded":
            Var.screen.blit(Loadvar.message_load, [280, 330])
        elif Loadvar.message_timer.count_name == "deleted":
            Var.screen.blit(Loadvar.message_deleted, [287, 330])
    
    for s in slot.Slotvar.slots:
        if s.highlighted and not s.choosen:
            if not s.removing_light:
                if s.getting_light:
                    s.getting_light = False
                    Var.screen.blit(Loadvar.pics["Slot_Highlight"], s.pos)
                    Channels.mouse_sounds.play(Loadvar.sounds["feel"])
            else:
                Var.screen.blit(Loadvar.pics["Slot"], s.pos)
                Var.screen.blit(s.text_image, [s.pos[0]+5, s.pos[1]+2])
                s.removing_light = False
                s.highlighted = False
        elif s.choosen:
            if s.getting_light:
                s.getting_light = False
                Var.screen.blit(Loadvar.pics["Slot_Chooselight"], s.pos)
                

    for m in slot.Slotvar.menue_buttons.values():
        if m.changing_status:
            if m.changing_status == "active":
                Var.screen.blit(Loadvar.pics["Active_Menue_Button"], m.pos)
                Var.screen.blit(m.active_text_image, [m.pos[0]+25-(int(len(m.text)*3.5)), m.pos[1]+2])
            elif m.changing_status == "inactive":
                Var.screen.blit(Loadvar.pics["Inactive_Menue_Button"], m.pos)
                Var.screen.blit(m.inactive_text_image, [m.pos[0]+25-(int(len(m.text)*3.5)), m.pos[1]+2])
            elif m.changing_status == "pressed":
                Var.screen.blit(Loadvar.pics["Pressed_Menue_Button"], m.pos)
                Var.screen.blit(m.pressed_text_image, [m.pos[0]+25-(int(len(m.text)*3.5)), m.pos[1]+2])
            m.changing_status = ""
            
    pygame.display.flip()

                    





def load():

    if menuehandler.Menuvar.saving_or_loading_is_starting:
        slot.Slotvar.menue_buttons["load"] = slot.Save_Load_Menue_Button("LOAD", [225, 360])
        slot.Slotvar.menue_buttons["delete"] = slot.Save_Load_Menue_Button("DELETE", [295, 360])
        slot.Slotvar.menue_buttons["cancel"] = slot.Save_Load_Menue_Button("CANCEL", [365, 360])
        slot.Slotvar.menue_buttons["cancel"].active = True

        Loadvar.sounds["popup"] = pygame.mixer.Sound(Var.path+"\\sound\\popupsound.wav")
        Loadvar.sounds["popup"].set_volume(0.5)
        Loadvar.sounds["click"] = pygame.mixer.Sound(Var.path+"\\sound\\clicksound.wav")
        Loadvar.sounds["click"].set_volume(0.5)
        Loadvar.sounds["feel"] = pygame.mixer.Sound(Var.path+"\\sound\\Button_Feel.wav")
        Loadvar.sounds["feel"].set_volume(0.5)
        Loadvar.sounds["confirm"] = pygame.mixer.Sound(Var.path+"\\sound\\Button_Confirm.wav")

        slot.Slotvar.slots.clear()
        for f in os.listdir("savegames"):
            slot.Slotvar.slots.append(slot.Slot(f.replace(".txt", "")))

            
    if not Loadvar.security_question:
        for s in slot.Slotvar.slots:
            if s.choosen:
                if not (s.text == Loadvar.choice_showbox.text):
                    s.removing_light = True
                    s.choosen = False
                    s.highlighted = True # (!)
                    Loadvar.somethings_choosen = False
                elif not Loadvar.somethings_choosen:
                    Loadvar.somethings_choosen = True
            elif (not s.choosen) and (s.text == Loadvar.choice_showbox.text):
                s.choosen = True
                Loadvar.somethings_choosen = True
        if len(slot.Slotvar.slots) == 0:
            Loadvar.somethings_choosen = False

        if slot.Slotvar.menue_buttons["load"].active:
            if not Loadvar.somethings_choosen:
                slot.Slotvar.menue_buttons["load"].active = False
                slot.Slotvar.menue_buttons["load"].changing_status = "inactive"
        else:
            if Loadvar.somethings_choosen:
                slot.Slotvar.menue_buttons["load"].active = True
                slot.Slotvar.menue_buttons["load"].changing_status = "active"
                
        if not Loadvar.somethings_choosen and slot.Slotvar.menue_buttons["delete"].active:
            slot.Slotvar.menue_buttons["delete"].active = False
            slot.Slotvar.menue_buttons["delete"].changing_status = "inactive"
        elif Loadvar.somethings_choosen and not slot.Slotvar.menue_buttons["delete"].active:
            slot.Slotvar.menue_buttons["delete"].active = True
            slot.Slotvar.menue_buttons["delete"].changing_status = "active"

        for m in slot.Slotvar.menue_buttons.values():
            if m.active:
                if pygame.mouse.get_pressed()[0] and (pygame.mouse.get_pos()[0] in range(m.pos[0], m.pos[0]+50)) and \
                   (pygame.mouse.get_pos()[1] in range(m.pos[1], m.pos[1]+15)) and (not m.pressed):
                    m.pressed = True
                    m.changing_status = "pressed"
                elif (not pygame.mouse.get_pressed()[0]) and m.pressed:
                    m.pressed = False
                    m.changing_status = "active"
            
        
        draw_loader()
        loadloop()

    else:  # security_question
        
        if Loadvar.security_question_start:
            Loadvar.security_question_start = False
            pygame.draw.rect(Var.screen, (100, 30, 12), [160, 130, 320, 180], 10)
            pygame.draw.rect(Var.screen, (65, 90, 130), [160, 130, 320, 180])
            slot.Slotvar.yes_no_buttons.append(slot.Save_Load_Menue_Button("YES", [260, 250]))
            slot.Slotvar.yes_no_buttons.append(slot.Save_Load_Menue_Button("NO", [330, 250]))
            Loadvar.security_question_text_image = Loadvar.message_font.render(Loadvar.security_question, True, Loadvar.message_color)
            Var.screen.blit(Loadvar.security_question_text_image, [193,188])
            for b in slot.Slotvar.yes_no_buttons:
                Var.screen.blit(Loadvar.pics["Active_Menue_Button"], b.pos)
                Var.screen.blit(b.active_text_image, [b.pos[0]+25-(int(len(b.text)*3.5)), b.pos[1]+2])
            pygame.display.flip()
            Channels.signals.play(Loadvar.sounds["popup"])

        for b in slot.Slotvar.yes_no_buttons:
            if pygame.mouse.get_pressed()[0] and (pygame.mouse.get_pos()[0] in range(b.pos[0], b.pos[0]+50)) and \
                   (pygame.mouse.get_pos()[1] in range(b.pos[1], b.pos[1]+15)) and (not b.pressed):
                b.pressed = True
                b.changing_status = "pressed"
            elif (not pygame.mouse.get_pressed()[0]) and b.pressed:
                b.pressed = False
                b.changing_status = "active"

        for e in pygame.event.get():
            if e.type == pygame.MOUSEMOTION:
                for b in slot.Slotvar.yes_no_buttons:
                    if not ((e.pos[0] in range(b.pos[0], b.pos[0]+50)) and (e.pos[1] in range(b.pos[1], b.pos[1]+15))) and b.pressed:
                        b.pressed = False
                        b.changing_status = "active"
            if e.type == pygame.MOUSEBUTTONUP:
                if ((e.pos[0] in range(260,310)) or (e.pos[0] in range(330,380))) and (e.pos[1] in range(250,265)):
                    if (e.pos[0] in range(260,310)) and (e.pos[1] in range(250,265)):  # yes
                        if Loadvar.security_question == "Are you sure you want to delete '"+Loadvar.choice_showbox.text+"'?":
                            for s in slot.Slotvar.slots:
                                if s.text == Loadvar.choice_showbox.text:
                                    slot.Slotvar.slots.remove(s)
                            os.remove("savegames\\"+Loadvar.choice_showbox.text+".txt")
                            Loadvar.slot_deleted = True
                            Loadvar.message_changing = True
                            Loadvar.message_timer.start_count(1500, "deleted")
                            Loadvar.security_question_answered = True
                        elif Loadvar.security_question == "Not saved data will be lost! Load '"+Loadvar.choice_showbox.text+"'?":
                            # LADEVORGANG
                            execute_load()
                            Loadvar.message_changing = True
                            Loadvar.message_timer.start_count(3000, "loaded")
                            Loadvar.security_question_answered = "loaded!"
                    else:  # no
                        Loadvar.security_question_answered = True
                        Channels.mouse_sounds.play(Loadvar.sounds["click"])
                    slot.Slotvar.yes_no_buttons.clear()
                    Loadvar.security_question_text_image = None
                    Loadvar.security_question = ""
                    
        for b in slot.Slotvar.yes_no_buttons:
            if b.changing_status == "pressed":
                b.changing_status = ""
                Var.screen.blit(Loadvar.pics["Pressed_Menue_Button"], b.pos)
                Var.screen.blit(b.pressed_text_image, [b.pos[0]+25-(int(len(b.text)*3.5)), b.pos[1]+2])
                pygame.display.flip()
            elif b.changing_status == "active":
                b.changing_status = ""
                Var.screen.blit(Loadvar.pics["Active_Menue_Button"], b.pos)
                Var.screen.blit(b.active_text_image, [b.pos[0]+25-(int(len(b.text)*3.5)), b.pos[1]+2])
                pygame.display.flip()



                
    
    if menuehandler.Menuvar.saving_or_loading_is_starting:
        menuehandler.Menuvar.saving_or_loading_is_starting = False
        menuehandler.Menuvar.pics.clear()
        Loadvar.choice_showbox.pos = [270, 300]
        
    if Loadvar.confirmed:
        Loadvar.confirmed = False
        for s in slot.Slotvar.slots:
            if s.choosen:
                s.choosen = False
                s.removing_light = True
        Loadvar.choice_showbox.text = ""
        Loadvar.somethings_choosen = False
        slot.Slotvar.menue_buttons.clear()
        Loadvar.pics.clear()
        Channels.signals.play(Loadvar.sounds["confirm"])
        Loadvar.sounds.clear()
        pygame.time.wait(800)
        menuehandler.Menuvar.starting = True
        menuehandler.Menuvar.loading = False
        menuehandler.Menuvar.saving_or_loading_just_closed = True
