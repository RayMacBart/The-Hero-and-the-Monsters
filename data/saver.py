import pygame
import menuehandler
import pool
from pool import Var
from pool import Channels
import basic_types
import slot
import os
import pickle


## class Savevar
## execute_save()
## saveloop()
## draw_saver()
## save()


class Savevar():
    pics = {}
    sounds = {}
    confirmed = False
    input_box = slot.Slot("")
    somethings_choosen = False
    text_edit = False
    name_already_existing = False
    slot_added = False
    slot_deleted = False
    security_question_start = False
    security_question = ""
    security_question_text_image = None
    security_question_answered = False
    message_timer = pool.Count()
    message_blitted = False
    message_changing = False
    message_font = pygame.font.Font(None, 16)
    message_color = (190,230,160)
    message_full_text = "It's full! All Slots are already used, sorry. Choose one to overwrite."
    message_full = message_font.render(message_full_text, True, message_color)
    message_save = message_font.render("GAME SAVED!", True, message_color)
    message_toolong = message_font.render("Name cannot be longer", True, message_color)
    message_deleted = message_font.render("File deleted.", True, message_color)
    message_invalid = message_font.render("Invalid character!", True, message_color)






def execute_save():

##    print("          ! ! !\n")
##    print("___________________________")
##    print("---------------------------")
##    print("###########################")
##    print("###########################")
##    print("---------------------------\n")
##    print("STATUS BEFORE SAVING")
##    print(Savevar.input_box.text,"\n")
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
##    print("END OF STATUS BEFORE SAVING SCRIPT")
##    print(Savevar.input_box.text)
##    print("||||||||||||||||||||||||||||")
##    print("____________________________")
##    print("----------------------------")
##    print("############################")
##    print("############################")
##    print("############################\n\n\n")
    



    
    
    savedict = {}
    savedict["ref_point"] = Var.ref_point
    savedict["main_background"] = Var.main_background
    savedict["hero"] = {}
    savedict["cbs"] = {}
    savedict["grounds"] = {}
    savedict["bgs"] = {}
    savedict["abgs"] = {}
    savedict["decs"] = {}
    savedict["adecs"] = {}
    savedict["ovs"] = {}
    savedict["aovs"] = {}
    savedict["borders"] = {}
    savedict["doors"] = {}
    savedict["obs"] = {}
    savedict["aobs"] = {}
    savedict["units"] = {}

    savedict["hero"]["ID"] = Var.hero.ID
    savedict["hero"]["layerpos"] = Var.hero.layerpos
    savedict["hero"]["transparency"] = Var.hero.transparency
    savedict["hero"]["absolute_destination"] = Var.hero.absolute_destination
    savedict["hero"]["current_way"] = Var.hero.current_way
    savedict["hero"]["dir"] = Var.hero.dir
    savedict["hero"]["border_dir"] = Var.hero.dir
    savedict["hero"]["walk_animation_progress"] = Var.hero.walk_animation_progress
    savedict["hero"]["walk_animation_delay"] = Var.hero.walk_animation_delay
    savedict["hero"]["walk_animation_frame_countdown"] = Var.hero.walk_animation_frame_countdown
    savedict["hero"]["go"] = Var.hero.go
    savedict["hero"]["start_going"] = Var.hero.start_going
    savedict["hero"]["frameway"] = Var.hero.frameway
    savedict["hero"]["movement_skip_at_frame"] = Var.hero.movement_skip_at_frame
    savedict["hero"]["movement_skip_countdown"] = Var.hero.movement_skip_countdown
    savedict["hero"]["speed"] = Var.hero.speed
    savedict["hero"]["last_frameways"] = Var.hero.last_frameways
    savedict["hero"]["drawn"] = Var.hero.drawn
    savedict["hero"]["draw_pressed"] = Var.hero.draw_pressed
    savedict["hero"]["drawing"] = Var.hero.drawing
    savedict["hero"]["putting_away"] = Var.hero.putting_away
    savedict["hero"]["current_drawing_pic_nr"] = Var.hero.current_drawing_pic_nr
    savedict["hero"]["draw_animation_pic_countdown"] = Var.hero.draw_animation_pic_countdown
    savedict["hero"]["current_fightwalk_pic_nr"] = Var.hero.current_fightwalk_pic_nr
    savedict["hero"]["fightwalk_animation_pic_countdown"] = Var.hero.fightwalk_animation_pic_countdown
    

    for cb in Var.current_blitmaps:
        savedict["cbs"][cb.ID] = {}
        savedict["cbs"][cb.ID]["name"] = cb.name
        savedict["cbs"][cb.ID]["pos"] = cb.pos
        
    for g in Var.grounds.values(): #
        savedict["grounds"][g.ID] = {} #
        savedict["grounds"][g.ID]["typ"] = g.typ #
        savedict["grounds"][g.ID]["name"] = g.name #
        savedict["grounds"][g.ID]["pos"] = g.pos #
        savedict["grounds"][g.ID]["realpos"] = g.realpos#
        savedict["grounds"][g.ID]["transparency"] = g.transparency #

    for bg in Var.backgrounds.values(): #
        savedict["bgs"][bg.ID] = {} #
        savedict["bgs"][bg.ID]["typ"] = bg.typ #
        savedict["bgs"][bg.ID]["name"] = bg.name #
        savedict["bgs"][bg.ID]["pos"] = bg.pos #
        savedict["bgs"][bg.ID]["realpos"] = bg.realpos#
        savedict["bgs"][bg.ID]["transparency"] = bg.transparency #

    for abg in Var.animated_backgrounds.values(): #
        savedict["abgs"][abg.ID] = {} #
        savedict["abgs"][abg.ID]["typ"] = abg.typ #
        savedict["abgs"][abg.ID]["name"] = abg.name #
        savedict["abgs"][abg.ID]["pos"] = abg.pos #
        savedict["abgs"][abg.ID]["realpos"] = abg.realpos#
        savedict["abgs"][abg.ID]["chaos"] = abg.chaos#
        savedict["abgs"][abg.ID]["transparency"] = abg.transparency #
        savedict["abgs"][abg.ID]["quantity"] = abg.quantity#
        savedict["abgs"][abg.ID]["current_pic"] = abg.current_pic#
        savedict["abgs"][abg.ID]["rate_duration"] = abg.rate_duration#
        savedict["abgs"][abg.ID]["last_pictime"] = abg.last_pictime#

    for d in Var.decorations.values():
        savedict["decs"][d.ID] = {}
        savedict["decs"][d.ID]["typ"] = d.typ #
        savedict["decs"][d.ID]["name"] = d.name
        savedict["decs"][d.ID]["pos"] = d.pos
        savedict["decs"][d.ID]["realpos"] = d.realpos#
        savedict["decs"][d.ID]["transparency"] = d.transparency#

    for ad in Var.animated_decorations.values():#
        savedict["adecs"][ad.ID] = {}#
        savedict["adecs"][ad.ID]["typ"] = ad.typ#
        savedict["adecs"][ad.ID]["name"] = ad.name#
        savedict["adecs"][ad.ID]["pos"] = ad.pos#
        savedict["adecs"][ad.ID]["realpos"] = ad.realpos#
        savedict["adecs"][ad.ID]["chaos"] = ad.chaos#
        savedict["adecs"][ad.ID]["transparency"] = ad.transparency#
        savedict["adecs"][ad.ID]["quantity"] = ad.quantity#
        savedict["adecs"][ad.ID]["current_pic"] = ad.current_pic#
        savedict["adecs"][ad.ID]["rate_duration"] = ad.rate_duration#
        savedict["adecs"][ad.ID]["last_pictime"] = ad.last_pictime#

    for ov in Var.overlays.values():#
        savedict["ovs"][ov.ID] = {}#
        savedict["ovs"][ov.ID]["typ"] = ov.typ #
        savedict["ovs"][ov.ID]["name"] = ov.name#
        savedict["ovs"][ov.ID]["pos"] = ov.pos#
        savedict["ovs"][ov.ID]["realpos"] = ov.realpos#
        savedict["ovs"][ov.ID]["transparency"] = ov.transparency#

    for aov in Var.animated_overlays.values():#
        savedict["aovs"][aov.ID] = {}#
        savedict["aovs"][aov.ID]["typ"] = aov.typ#
        savedict["aovs"][aov.ID]["name"] = aov.name#
        savedict["aovs"][aov.ID]["pos"] = aov.pos#
        savedict["aovs"][aov.ID]["realpos"] = aov.realpos#
        savedict["aovs"][aov.ID]["chaos"] = aov.chaos#
        savedict["aovs"][aov.ID]["transparency"] = aov.transparency#
        savedict["aovs"][aov.ID]["quantity"] = aov.quantity#
        savedict["aovs"][aov.ID]["current_pic"] = aov.current_pic#
        savedict["aovs"][aov.ID]["rate_duration"] = aov.rate_duration#
        savedict["aovs"][aov.ID]["last_pictime"] = aov.last_pictime#

    for b in Var.borders.values():
        savedict["borders"][b.ID] = {}
        savedict["borders"][b.ID]["typ"] = b.typ#
        savedict["borders"][b.ID]["name"] = b.name
        savedict["borders"][b.ID]["pos"] = b.pos
       # savedict["borders"][b.ID]["location"] = b.location
        savedict["borders"][b.ID]["realpos"] = b.realpos
        savedict["borders"][b.ID]["transparency"] = b.transparency#
        if type(b) == basic_types.High_border:
            savedict["borders"][b.ID]["transparent"] = b.transparent
            
    for do in Var.doors.values():
        savedict["doors"][do.ID] = {}
        savedict["doors"][do.ID]["typ"] = do.typ
        savedict["doors"][do.ID]["name"] = do.name
        savedict["doors"][do.ID]["pos"] = do.pos
        savedict["doors"][do.ID]["realpos"] = do.realpos
        savedict["doors"][do.ID]["quantity"] = do.quantity
        savedict["doors"][do.ID]["rate_duration"] = do.rate_duration
        savedict["doors"][do.ID]["chaos"] = do.chaos
        savedict["doors"][do.ID]["transparency"] = do.transparency # 'noch' nicht hineingenommen: transparent
        savedict["doors"][do.ID]["current_pic"] = do.current_pic
        savedict["doors"][do.ID]["last_pictime"] = do.last_pictime
        savedict["doors"][do.ID]["dir"] = do.dir   # ab hier Door-spezifische Attribute
        savedict["doors"][do.ID]["status"] = do.status
        savedict["doors"][do.ID]["in_focus"] = do.in_focus
        savedict["doors"][do.ID]["welcome_point"] = do.welcome_point
        
    for o in Var.obstacles.values():
        savedict["obs"][o.ID] = {}
        savedict["obs"][o.ID]["typ"] = o.typ#
        savedict["obs"][o.ID]["name"] = o.name
        savedict["obs"][o.ID]["pos"] = o.pos
        savedict["obs"][o.ID]["realpos"] = o.realpos
        savedict["obs"][o.ID]["transparency"] = o.transparency#
        if (issubclass(type(o), basic_types.High_obstacle)) or (type(o) == basic_types.High_obstacle):
            savedict["obs"][o.ID]["transparent"] = o.transparent
        if type(o) == basic_types.Inclined_high_obstacle:
            savedict["obs"][o.ID]["L_y_offset"] = o.L_y_offset
            savedict["obs"][o.ID]["R_y_offset"] = o.R_y_offset
            savedict["obs"][o.ID]["x_offset"] = o.x_offset

    for ao in Var.animated_obstacles.values():
        savedict["aobs"][ao.ID] = {}
        savedict["aobs"][ao.ID]["typ"] = ao.typ#
        savedict["aobs"][ao.ID]["name"] = ao.name
        savedict["aobs"][ao.ID]["pos"] = ao.pos
        savedict["aobs"][ao.ID]["realpos"] = ao.realpos
        savedict["aobs"][ao.ID]["quantity"] = ao.quantity
        savedict["aobs"][ao.ID]["rate_duration"] = ao.rate_duration
        savedict["aobs"][ao.ID]["chaos"] = ao.chaos#
        savedict["aobs"][ao.ID]["transparency"] = ao.transparency#
        savedict["aobs"][ao.ID]["current_pic"] = ao.current_pic
        savedict["aobs"][ao.ID]["last_pictime"] = ao.last_pictime
        if (issubclass(type(ao), basic_types.High_obstacle)) or (type(ao) == basic_types.High_obstacle):
            savedict["aobs"][ao.ID]["transparent"] = ao.transparent
        if type(ao) == basic_types.Inclined_high_obstacle:
            savedict["aobs"][ao.ID]["L_y_offset"] = ao.L_y_offset
            savedict["aobs"][ao.ID]["R_y_offset"] = ao.R_y_offset
            savedict["aobs"][ao.ID]["x_offset"] = ao.x_offset
            
    for u in Var.units.values():
        savedict[u.ID] = {}
        if (issubclass(type(u), basic_types.Character)) or (type(u) == basic_types.Character):
            savedict["units"][u.ID]["typ"] = u.typ#
            savedict["units"][u.ID]["name"] = u.name
            savedict["units"][u.ID]["pos"] = u.pos
            savedict["units"][u.ID]["realpos"] = u.realpos
            savedict["units"][u.ID]["layerpos"] = u.layerpos
            savedict["units"][u.ID]["transparency"] = u.transparency#
            savedict["units"][u.ID]["absolute_destination"] = u.absolute_destination
            savedict["units"][u.ID]["current_way"] = u.current_way
            savedict["units"][u.ID]["dir"] = u.dir
            savedict["units"][u.ID]["border_dir"] = u.border_dir
            savedict["units"][u.ID]["walk_animation_progress"] = u.walk_animation_progress
            savedict["units"][u.ID]["walk_animation_delay"] = u.walk_animation_delay
            savedict["units"][u.ID]["walk_animation_frame_countdown"] = u.walk_animation_frame_countdown
            savedict["units"][u.ID]["go"] = u.go
            savedict["units"][u.ID]["start_going"] = u.start_going
            savedict["units"][u.ID]["frameway"] = u.frameway
            savedict["units"][u.ID]["movement_skip_at_frame"] = u.movement_skip_at_frame
            savedict["units"][u.ID]["movement_skip_countdown"] = u.movement_skip_countdown
            savedict["units"][u.ID]["speed"] = u.speed
            savedict["units"][u.ID]["last_frameways"] = u.last_frameways

    file = open("savegames\\"+Savevar.input_box.text+".txt", "wb")
    pickle.dump(savedict, file)
    file.close()
    
    del savedict
    del file

    






def saveloop():
    
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
            for s in slot.Slotvar.slots:
                if (e.pos[0] in range(s.pos[0], s.pos[0]+100)) and (e.pos[1] in range(s.pos[1], s.pos[1]+16)):
                    if not s.choosen:
                        s.choosen = True
                        s.getting_light = True
                        Channels.mouse_sounds.play(Savevar.sounds["click"])
                        s.highlighted = False
                    if not (s.text == Savevar.input_box.text):
                        Savevar.text_edit = True
                        Savevar.input_box.text = s.text
            for m in slot.Slotvar.menue_buttons.values():
                if m.active and m.pressed and ((e.pos[0] in range(m.pos[0], m.pos[0]+50)) and (e.pos[1] in range(m.pos[1], m.pos[1]+15))):
                    if m.text == "SAVE":  
                        for s in slot.Slotvar.slots:
                            if s.choosen and (s.text == Savevar.input_box.text):
                                Savevar.name_already_existing = True
                        if not Savevar.name_already_existing:
                            if len(slot.Slotvar.slots) < 27:
                                slot.Slotvar.slots.append(slot.Slot(Savevar.input_box.text))
                                Savevar.slot_added = True
                                if Savevar.message_timer.count_name != "saved":
                                    Savevar.message_changing = True
                                Savevar.message_timer.start_count(1500, "saved")
                                #Speichervorgang
                                execute_save()
                            else:
                                if Savevar.message_timer.count_name != "slots full":
                                    Savevar.message_changing = True
                                Savevar.message_timer.start_count(4000, "slots full")
                        else:
                            #Überschreibung-Sicherheits-Frage startet
                            for s in slot.Slotvar.slots:
                                if s.choosen:
                                    Savevar.security_question = "Are you sure you want to overwrite '"+s.text+"'?"
                            Savevar.security_question_start = True
                            Savevar.name_already_existing = False
                                
                    elif m.text == "DELETE":
                        for s in slot.Slotvar.slots:
                            if s.choosen:
                                Savevar.security_question = "Are you sure you want to delete '"+s.text+"'?"
                        Savevar.security_question_start = True

                    elif m.text == "CANCEL":
                        Savevar.confirmed = True

        if e.type == pygame.KEYDOWN:
            Savevar.text_edit = True
            if (e.key == pygame.K_BACKSPACE) and (len(Savevar.input_box.text) > 0):
                Savevar.input_box.text = Savevar.input_box.text[:-1]
            elif e.key == pygame.K_ESCAPE:
                Savevar.confirmed = True
                menuehandler.Menuvar.esc_used = True
            else:
                if (Savevar.input_box.text_image.get_width() <= 85):
                    if e.key not in [pygame.K_BACKSPACE, pygame.K_RETURN, pygame.K_KP_ENTER]:
                        Savevar.input_box.text += e.unicode
                        for t in Savevar.input_box.text:
                            if t in ['~','"','#','%','&','*',':','<','>','?','/','\\','{','|','}']:  # ungültige Zeichen für Dateinamen
                                Savevar.input_box.text = Savevar.input_box.text.replace(t, "")
                                if Savevar.message_timer.count_name != "invalid":
                                    Savevar.message_changing = True
                                Savevar.message_timer.start_count(800, "invalid")
                else:
                    if Savevar.message_timer.count_name != "too long":
                        Savevar.message_changing = True
                    Savevar.message_timer.start_count(2000, "too long")
    pygame.event.pump()
                



                

def draw_saver():
    
    if menuehandler.Menuvar.saving_or_loading_is_starting:
        Savevar.pics["Background"] = pygame.image.load(Var.path+"\\pics\\Save_Background.png").convert()
        Savevar.pics["Message_Background"] = pygame.image.load(Var.path+"\\pics\\Save_Message_Background.png").convert()
        Savevar.pics["Slot"] = pygame.image.load(Var.path+"\\pics\\Slot.png").convert()
        Savevar.pics["Slot_Highlight"] = pygame.image.load(Var.path+"\\pics\\Slot_Highlight.png").convert()
        Savevar.pics["Slot_Highlight"].set_colorkey([0,0,0], pygame.RLEACCEL)
        
        Savevar.pics["Slot_Chooselight"] = pygame.image.load(Var.path+"\\pics\\Slot_Chooselight.png").convert()
        Savevar.pics["Slot_Chooselight"].set_colorkey([0,0,0], pygame.RLEACCEL)

        Savevar.pics["Active_Menue_Button"]  = pygame.image.load(Var.path+"\\pics\\Active_Save_Load_Menue_Button.png").convert()
        Savevar.pics["Inactive_Menue_Button"]  = pygame.image.load(Var.path+"\\pics\\Inactive_Save_Load_Menue_Button.png").convert()
        Savevar.pics["Pressed_Menue_Button"]  = pygame.image.load(Var.path+"\\pics\\Pressed_Save_Load_Menue_Button.png").convert()

        Var.screen.blit(Savevar.pics["Background"], [0,0])
        for s in slot.Slotvar.slots:
            Var.screen.blit(Savevar.pics["Slot"], s.pos)
            Var.screen.blit(s.text_image, [s.pos[0]+5, s.pos[1]+2])
        Var.screen.blit(Savevar.pics["Slot"], [270, 300]) # Input_Box!
        for m in slot.Slotvar.menue_buttons.values():
            if m.text == "CANCEL":
                Var.screen.blit(Savevar.pics["Active_Menue_Button"], m.pos)
                Var.screen.blit(m.active_text_image, [m.pos[0]+25-(int(len(m.text)*3.5)), m.pos[1]+2])
                
            else:
                Var.screen.blit(Savevar.pics["Inactive_Menue_Button"], m.pos)
                Var.screen.blit(m.inactive_text_image, [m.pos[0]+25-(int(len(m.text)*3.5)), m.pos[1]+2])

    if Savevar.text_edit:
        Savevar.text_edit = False
        Var.screen.blit(Savevar.pics["Slot"], [270, 300])
        Savevar.input_box.text_image = slot.Slotvar.slot_font.render(Savevar.input_box.text, True, slot.Slotvar.slot_text_color)
        Var.screen.blit(Savevar.input_box.text_image, [273, 301])
        
    if Savevar.slot_added:
        Channels.signals.play(Savevar.sounds["confirm"])
        Savevar.slot_added = False
        Savevar.input_box.text = ""
        Var.screen.blit(Savevar.pics["Slot"], [270, 300])
        Var.screen.blit(Savevar.pics["Slot"], slot.Slotvar.slots[-1].pos)
        Var.screen.blit(slot.Slotvar.slots[-1].text_image, \
                        [slot.Slotvar.slots[-1].pos[0]+5, slot.Slotvar.slots[-1].pos[1]+2])

    if Savevar.slot_deleted or Savevar.security_question_answered:
        Channels.signals.play(Savevar.sounds["confirm"])
        if Savevar.slot_deleted:
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

        Var.screen.blit(Savevar.pics["Background"], [0,0])
        for s in slot.Slotvar.slots:
            Var.screen.blit(Savevar.pics["Slot"], s.pos)
            Var.screen.blit(s.text_image, [s.pos[0]+5, s.pos[1]+2])
        Var.screen.blit(Savevar.pics["Slot"], [270, 300]) # Input_Box!
        if not Savevar.slot_deleted and not (Savevar.security_question_answered == "overwritten!"):
            Var.screen.blit(Savevar.input_box.text_image, [273, 301])
            Savevar.security_question_answered = False
        else:
            Savevar.somethings_choosen = False
            Savevar.input_box.text = ""
            Savevar.slot_deleted = False
            Savevar.security_question_answered = False
        for m in slot.Slotvar.menue_buttons.values():
            if m.active:
                Var.screen.blit(Savevar.pics["Active_Menue_Button"], m.pos)
                Var.screen.blit(m.active_text_image, [m.pos[0]+25-(int(len(m.text)*3.5)), m.pos[1]+2])
            else:
                Var.screen.blit(Savevar.pics["Inactive_Menue_Button"], m.pos)
                Var.screen.blit(m.inactive_text_image, [m.pos[0]+25-(int(len(m.text)*3.5)), m.pos[1]+2])

    if Savevar.message_timer.check_if_ending():
        Var.screen.blit(Savevar.pics["Message_Background"], [0, 322])
        Savevar.message_blitted = False
    elif Savevar.message_timer.counting and not Savevar.message_blitted:
        if not Savevar.message_changing:
            Savevar.message_blitted = True
        else:
            Var.screen.blit(Savevar.pics["Message_Background"], [0, 322])
            Savevar.message_changing = False
        if Savevar.message_timer.count_name == "slots full":
            Var.screen.blit(Savevar.message_full, [150, 330])
            Channels.signals.play(Savevar.sounds["error"])
        elif Savevar.message_timer.count_name == "too long":
            Var.screen.blit(Savevar.message_toolong, [258, 330])
            Channels.signals.play(Savevar.sounds["error"])
        elif Savevar.message_timer.count_name == "saved":
            Var.screen.blit(Savevar.message_save, [280, 330])
        elif Savevar.message_timer.count_name == "deleted":
            Var.screen.blit(Savevar.message_deleted, [287, 330])
        elif Savevar.message_timer.count_name == "invalid":
            Var.screen.blit(Savevar.message_invalid, [275, 330])
            Channels.signals.play(Savevar.sounds["error"])
    
    for s in slot.Slotvar.slots:
        if s.highlighted and not s.choosen:
            if not s.removing_light:
                if s.getting_light:
                    s.getting_light = False
                    Var.screen.blit(Savevar.pics["Slot_Highlight"], s.pos)
                    Channels.mouse_sounds.play(Savevar.sounds["feel"])
            else:
                Var.screen.blit(Savevar.pics["Slot"], s.pos)
                Var.screen.blit(s.text_image, [s.pos[0]+5, s.pos[1]+2])
                s.removing_light = False
                s.highlighted = False
        elif s.choosen:
            if s.getting_light:
                s.getting_light = False
                Var.screen.blit(Savevar.pics["Slot_Chooselight"], s.pos)

    for m in slot.Slotvar.menue_buttons.values():
        if m.changing_status:
            if m.changing_status == "active":
                Var.screen.blit(Savevar.pics["Active_Menue_Button"], m.pos)
                Var.screen.blit(m.active_text_image, [m.pos[0]+25-(int(len(m.text)*3.5)), m.pos[1]+2])
            elif m.changing_status == "inactive":
                Var.screen.blit(Savevar.pics["Inactive_Menue_Button"], m.pos)
                Var.screen.blit(m.inactive_text_image, [m.pos[0]+25-(int(len(m.text)*3.5)), m.pos[1]+2])
            elif m.changing_status == "pressed":
                Var.screen.blit(Savevar.pics["Pressed_Menue_Button"], m.pos)
                Var.screen.blit(m.pressed_text_image, [m.pos[0]+25-(int(len(m.text)*3.5)), m.pos[1]+2])
            m.changing_status = ""
            
    pygame.display.flip()

                    





def save():

    if menuehandler.Menuvar.saving_or_loading_is_starting:
        slot.Slotvar.menue_buttons["save"] = slot.Save_Load_Menue_Button("SAVE", [225, 360])
        slot.Slotvar.menue_buttons["delete"] = slot.Save_Load_Menue_Button("DELETE", [295, 360])
        slot.Slotvar.menue_buttons["cancel"] = slot.Save_Load_Menue_Button("CANCEL", [365, 360])
        slot.Slotvar.menue_buttons["cancel"].active = True
        Savevar.sounds["popup"] = pygame.mixer.Sound(Var.path+"\\sound\\popupsound.wav")
        Savevar.sounds["popup"].set_volume(0.5)
        Savevar.sounds["click"] = pygame.mixer.Sound(Var.path+"\\sound\\clicksound.wav")
        Savevar.sounds["click"].set_volume(0.5)
        Savevar.sounds["error"] = pygame.mixer.Sound(Var.path+"\\sound\\errorsound.wav")
        Savevar.sounds["error"].set_volume(0.5)
        Savevar.sounds["feel"] = pygame.mixer.Sound(Var.path+"\\sound\\Button_Feel.wav")
        Savevar.sounds["feel"].set_volume(0.5)
        Savevar.sounds["confirm"] = pygame.mixer.Sound(Var.path+"\\sound\\Button_Confirm.wav")
        
        slot.Slotvar.slots.clear()
        for f in os.listdir("savegames"):
            slot.Slotvar.slots.append(slot.Slot(f.replace(".txt", "")))
            
        
    if not Savevar.security_question:
        for s in slot.Slotvar.slots:
            if s.choosen:
                if not (s.text == Savevar.input_box.text):
                    s.removing_light = True
                    s.choosen = False
                    s.highlighted = True # (!)
                    Savevar.somethings_choosen = False
                elif not Savevar.somethings_choosen:
                    Savevar.somethings_choosen = True
            elif (not s.choosen) and (s.text == Savevar.input_box.text):
                s.choosen = True
                s.getting_light = True
                Savevar.somethings_choosen = True
        if len(slot.Slotvar.slots) == 0:
            Savevar.somethings_choosen = False

        if slot.Slotvar.menue_buttons["save"].active:
            if (len(Savevar.input_box.text) == 0):
                slot.Slotvar.menue_buttons["save"].active = False
                slot.Slotvar.menue_buttons["save"].changing_status = "inactive"
        elif (len(Savevar.input_box.text) > 0):
            slot.Slotvar.menue_buttons["save"].active = True
            slot.Slotvar.menue_buttons["save"].changing_status = "active"
                
        if not Savevar.somethings_choosen and slot.Slotvar.menue_buttons["delete"].active:
            slot.Slotvar.menue_buttons["delete"].active = False
            slot.Slotvar.menue_buttons["delete"].changing_status = "inactive"
        elif Savevar.somethings_choosen and not slot.Slotvar.menue_buttons["delete"].active:
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
        
        draw_saver()
        saveloop()

    else:  # security_question
        
        if Savevar.security_question_start:
            Savevar.security_question_start = False
            pygame.draw.rect(Var.screen, (20, 66, 8), [160, 130, 320, 180], 10)
            pygame.draw.rect(Var.screen, (65, 90, 130), [160, 130, 320, 180])
            slot.Slotvar.yes_no_buttons.append(slot.Save_Load_Menue_Button("YES", [260, 250]))
            slot.Slotvar.yes_no_buttons.append(slot.Save_Load_Menue_Button("NO", [330, 250]))
            Savevar.security_question_text_image = Savevar.message_font.render(Savevar.security_question, True, Savevar.message_color)
            Var.screen.blit(Savevar.security_question_text_image, [193,188])
            for b in slot.Slotvar.yes_no_buttons:
                Var.screen.blit(Savevar.pics["Active_Menue_Button"], b.pos)
                Var.screen.blit(b.active_text_image, [b.pos[0]+25-(int(len(b.text)*3.5)), b.pos[1]+2])
            pygame.display.flip()
            Channels.signals.play(Savevar.sounds["popup"])

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
                        if Savevar.security_question == "Are you sure you want to delete '"+Savevar.input_box.text+"'?":
                            for s in slot.Slotvar.slots:
                                if s.text == Savevar.input_box.text:
                                    slot.Slotvar.slots.remove(s)
                            os.remove("savegames\\"+Savevar.input_box.text+".txt")
                            Savevar.slot_deleted = True
                            Savevar.message_changing = True
                            Savevar.message_timer.start_count(1500, "deleted")
                            Savevar.security_question_answered = True
                        elif Savevar.security_question == "Are you sure you want to overwrite '"+Savevar.input_box.text+"'?":
                            # SPEICHERVORGANG (ÜBERSCHREIBUNG)
                            execute_save()
                            Savevar.message_changing = True
                            Savevar.message_timer.start_count(3000, "saved")
                            Savevar.security_question_answered = "overwritten!"
                    else:  # no
                        Savevar.security_question_answered = True
                        Channels.mouse_sounds.play(Savevar.sounds["click"])
                    slot.Slotvar.yes_no_buttons.clear()
                    Savevar.security_question_text_image = None
                    Savevar.security_question = ""
                    
        for b in slot.Slotvar.yes_no_buttons:
            if b.changing_status == "pressed":
                b.changing_status = ""
                Var.screen.blit(Savevar.pics["Pressed_Menue_Button"], b.pos)
                Var.screen.blit(b.pressed_text_image, [b.pos[0]+25-(int(len(b.text)*3.5)), b.pos[1]+2])
                pygame.display.flip()
            elif b.changing_status == "active":
                b.changing_status = ""
                Var.screen.blit(Savevar.pics["Active_Menue_Button"], b.pos)
                Var.screen.blit(b.active_text_image, [b.pos[0]+25-(int(len(b.text)*3.5)), b.pos[1]+2])
                pygame.display.flip()


    if menuehandler.Menuvar.saving_or_loading_is_starting:
        menuehandler.Menuvar.saving_or_loading_is_starting = False
        pygame.key.set_repeat(300, 180)
        menuehandler.Menuvar.pics.clear()
        Savevar.input_box.pos = [270, 300]
        
    if Savevar.confirmed:
        Savevar.confirmed = False
        for s in slot.Slotvar.slots:
            if s.choosen:
                s.choosen = False
                s.removing_light = True
        Savevar.input_box.text = ""
        Savevar.somethings_choosen = False
        Channels.signals.play(Savevar.sounds["confirm"])
        slot.Slotvar.menue_buttons.clear()
        Savevar.pics.clear()
        Savevar.sounds.clear()
        pygame.time.wait(800)
        pygame.key.set_repeat(332, 17)
        menuehandler.Menuvar.starting = True
        menuehandler.Menuvar.saving = False
        menuehandler.Menuvar.saving_or_loading_just_closed = True
    
