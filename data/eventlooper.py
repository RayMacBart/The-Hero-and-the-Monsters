import pygame
from pool import Var
from pool import Channels
import menuehandler

## eventloop()


####################################
## e.type:
##
## KEYDOWN = 2
## KEYUP = 3
## MOUSEMOVEMENT = 4
## MOUSEDOWN = 5
## MOUSEUP = 6
## PYGAMEQUIT = 12

##e.button:
## 1 = LEFT, 2 = WHEEL, 3 = RIGHT, 4 = WHEELUP, 5 = WHEELDOWN

## e.key:
## ESCAPE = 27
## SPACE = 32
## left ENTER = 13
## left ctrl: 306
## left alt: 308
## left shift: 304
## w: 119
## a: 97
## s: 115
## d: 100
## e: 101
## q: 113
## 1: 49
## 2: 50
## 3: 51


def eventloop():
    for e in pygame.event.get():
#        print("e.type, e.__dict__:",e.type,e.__dict__,sep=" ")
        if e.type == 2:  # KEYDOWN
            if e.key == 32: # SPACE
                #print("AbsHeroRealPos:",[Var.hero.realpos[0]-Var.ref_point[0], \
                #                         Var.hero.realpos[1]-Var.ref_point[1]], \
                #      "  AbsHeroLayerPos:", [Var.hero.layerpos[0]-Var.ref_point[0], \
                #                             Var.hero.layerpos[1]-Var.ref_point[1]])
                print("\n\nHERO:")
                print("Pos:", Var.hero.pos, "\nRealpos:", Var.hero.realpos, "\nLayerpos:", Var.hero.layerpos,\
                      "border_dir:", Var.hero.border_dir)
            if Var.hero.fighting:
                if e.key == 119: # W
                    if not Var.fight.W_pressed:
                        Var.fight.W_pressed = True
                        #print(str(pygame.time.get_ticks())+":", "Keydown: W ( = O )")
                if e.key == 97: # A
                    if not Var.fight.A_pressed:
                        Var.fight.A_pressed = True
                        #print(str(pygame.time.get_ticks())+":", "Keydown: A ( = L )")
                if e.key == 115: # S
                    if not Var.fight.S_pressed:
                        Var.fight.S_pressed = True
                        #print(str(pygame.time.get_ticks())+":", "Keydown: S ( = U )")
                if e.key == 100: # D
                    if not Var.fight.D_pressed:
                        Var.fight.D_pressed = True
                        #print(str(pygame.time.get_ticks())+":", "Keydown: D ( = R )")


        if Var.frames_since_last_click > 5:  # Soll vor Fehlreaktionen durch zu schnelle Clicks hintereinander schützen.
            if e.type == pygame.MOUSEBUTTONUP: # Mousebuttonup
                Var.frames_since_last_click = 0
                if e.button == 1: # Linke Maustaste
                    #print(str(pygame.time.get_ticks())+":", "Left Click")
                    if not (Var.hero.fighting or Var.hero.drawing or Var.hero.putting_away):
                        Var.hero.go = True
                        Var.hero.start_going = True
                        Var.hero.sounds["footsteps_sound"].stop()  # wird in blaster wieder geplayed, ist hier um mehrfach Soundüberlagerungen zu verhindern
                        Var.hero.absolute_destination = [e.pos[0]-Var.ref_point[0], e.pos[1]-Var.ref_point[1]]
                        for do in Var.doors.values():
                            do.in_focus = False
                        Var.go_point["start"] = True
                        Var.go_point["pos"] = [e.pos[0]-7,e.pos[1]-5]

                    elif Var.hero.fighting:
                        if Var.fight.W_pressed or Var.fight.A_pressed or Var.fight.S_pressed or Var.fight.D_pressed:
                            Var.hero.attack_pressed = True
                        for u in Var.units.values():
                            try:
                                if u.click_mask.get_at([e.pos[0]-u.pos[0], e.pos[1]-u.pos[1]]):
                                    Var.hero.attack_focus = u.ID
                                    Var.hero.focussed_enemy = u
                                    
                                    #print(str(pygame.time.get_ticks())+":", "Hero Attack Klick - hero.attack_focus:", u.ID)

                                    if not Var.fight.starting:
                                        Var.fight.handle_hero_permission()
                                        if Var.hero.attack_permission:
                                            Var.fight.handle_hero_attack()
                                        if Var.hero.attack_pressed:
                                            Var.hero.attack_pressed = False
                                        
                                    Var.hero.new_focus = True
                                    #Var.fight.enemy = u ### NEU !!!!!!!!!!!!!!
                            except IndexError:
                                print(str(pygame.time.get_ticks())+":", "IndexError @ eventlooper when Left-Clicking!!")
                            
                elif e.button == 3: # Rechte Maustaste
                    #print(str(pygame.time.get_ticks())+":", "Right Click")
                    for d in Var.doors.values():
                        d.check_action(e.pos)

                    if Var.hero.fighting:
                        if Var.fight.W_pressed or Var.fight.A_pressed or Var.fight.D_pressed:
                            Var.hero.defense_pressed = True
                        elif Var.fight.S_pressed:
                            Var.hero.defblock_pressed = True
                        for u in Var.units.values():
                            try:
                                if u.click_mask.get_at([e.pos[0]-u.pos[0], e.pos[1]-u.pos[1]]):
                                    Var.hero.defense_focus = u.ID
                                    #print(str(pygame.time.get_ticks())+":", "Hero Defense Klick - hero.defense_focus:", u.ID)
                            except IndexError:
                                pass

                for u in Var.units.values():  # Kampfcursor soll nicht nur beim Kämpfen sichtbar sein.
                    if u in Var.blitlist:     # ...und egal ob rechts- oder linksclick
                        try:
                            if u.click_mask.get_at([e.pos[0]-u.pos[0], e.pos[1]-u.pos[1]]):
                                Var.last_fightclick = pygame.time.get_ticks()
                        except IndexError:
                            pass

                    
        if e.type == 3: # KEYUP
##            print(pygame.key.name(e.key)+":", e.key)
            if e.key == 304: # L Shift
                Var.hero.draw_pressed = True
            if e.key == 306: # L Ctrl
                print("\nHero dead:", Var.hero.dead, "\nHero fighting", Var.hero.fighting, "\nHero focussed_enemy", Var.hero.focussed_enemy, \
                      "\nHero min_one_detected", Var.hero.min_one_detected, "\nHero attention", Var.hero.attention)
##                print("Hero Hitpoints:", Var.hero.hitpoints)
##                for u in Var.units.values():
##                    print("Ork Hitpoints:", u.hitpoints)
                #print("border-dir:",Var.hero.border_dir, "coll-dir:",Var.collision_direction, "xdir:", Var.xdir, "ydir:", Var.ydir)
##                print("\n...\n...\nstart def:",Var.hero.start_defending, "\ndef:",Var.hero.defending, "\nreadyTB:",Var.hero.ready_to_block, \
##                      "\nstart release def:",Var.hero.start_release_defending, "\nrelease def:",Var.hero.release_defending, \
##                      "\nstart defblock:",Var.hero.start_defblocking, "\ndefblock:",Var.hero.defblocking, \
##                      "\nstart block:",Var.hero.start_blocking, "\nblock:",Var.hero.blocking, \
##                      "\nstart hit:",Var.hero.start_being_hitted, "\nhit:",Var.hero.being_hitted)
                    
            if e.key == 27: # Escape
                Var.menue = True
                menuehandler.Menuvar.starting = True
                Channels.background_music.pause()

            if Var.hero.fighting:
                if e.key == 119: # W
                    Var.fight.W_pressed = False
                    #print(str(pygame.time.get_ticks())+":", "Key release: W ( = O )")
                if e.key == 97: # A
                    Var.fight.A_pressed = False
                    #print(str(pygame.time.get_ticks())+":", "Key release: A ( = L )")
                if e.key == 115: # S
                    Var.fight.S_pressed = False
                    #print(str(pygame.time.get_ticks())+":", "Key release: S ( = U )")
                if e.key == 100: # D
                    Var.fight.D_pressed = False
                    #print(str(pygame.time.get_ticks())+":", "Key release: D ( = R )")


        if e.type == 4: # MOUSE MOVEMENT
            Var.mouse_pos = pygame.mouse.get_pos() # Leider aufgrund unergründlicher Fehler bei Verwendung von pygame.mouse.get_pos() notwendig
            
    pygame.event.pump()




