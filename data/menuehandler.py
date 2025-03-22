import pygame
from pool import Var
from pool import Channels
import loader
import saver


## class Menuvar()
## draw_menue()
## close_menue()
## menue_eventloop()
## blast_menue()
## handle_menue()


class Menuvar():
    pics = {}
    starting = True
    music = pygame.mixer.Sound(Var.path+"\\sound\\The Freedom Catcher.wav")
    feeling_button = None
    saving = False
    loading = False
    saving_or_loading_is_starting = False
    saving_or_loading_just_closed = False
    
    esc_used = False #Verhindert doppeltes Erkennen d. esc-taste hintereinander
    


def draw_menue():
    if Menuvar.starting:
        Menuvar.pics["Background"] = pygame.image.load(Var.path+"\\pics\\Menue_Background.png").convert()
        Menuvar.pics["Background"].set_alpha(228, pygame.RLEACCEL)
        Menuvar.pics["Resume"] = pygame.image.load(Var.path+"\\pics\\Resume_Button.png").convert()
        Menuvar.pics["Load"] = pygame.image.load(Var.path+"\\pics\\Load_Button.png").convert()
        Menuvar.pics["Save"] = pygame.image.load(Var.path+"\\pics\\Save_Button.png").convert()
        Menuvar.pics["Quit"] = pygame.image.load(Var.path+"\\pics\\Quit_Button.png").convert()    
        Menuvar.pics["Button_Feel_Borderline"] = pygame.image.load(Var.path+"\\pics\\Button_Feel_Borderline.png").convert()
        Menuvar.pics["Button_Feel_Borderline"].set_colorkey([0,0,0], pygame.RLEACCEL)
        Menuvar.pics["Button_Confirm_Borderline"] = pygame.image.load(Var.path+"\\pics\\Button_Confirm_Borderline.png").convert()
        Menuvar.pics["Button_Confirm_Borderline"].set_colorkey([0,0,0], pygame.RLEACCEL)
        Var.screen.blit(Menuvar.pics["Background"], [0, 0])
        Var.screen.blit(Menuvar.pics["Resume"], [280, 135])
        Var.screen.blit(Menuvar.pics["Load"], [280, 160])
        Var.screen.blit(Menuvar.pics["Save"], [280, 185])
        Var.screen.blit(Menuvar.pics["Quit"], [280, 210])
    if Menuvar.feeling_button == 1:
        Var.screen.blit(Menuvar.pics["Button_Feel_Borderline"], [280,135])
    elif Menuvar.feeling_button == 2:
        Var.screen.blit(Menuvar.pics["Button_Feel_Borderline"], [280,160])
    elif Menuvar.feeling_button == 3:
        Var.screen.blit(Menuvar.pics["Button_Feel_Borderline"], [280,185])
    elif Menuvar.feeling_button == 4:
        Var.screen.blit(Menuvar.pics["Button_Feel_Borderline"], [280,210])
    elif Menuvar.feeling_button == -1:
        Var.screen.blit(Menuvar.pics["Resume"], [280, 135])
    elif Menuvar.feeling_button == -2:
        Var.screen.blit(Menuvar.pics["Load"], [280, 160])
    elif Menuvar.feeling_button == -3:
        Var.screen.blit(Menuvar.pics["Save"], [280, 185])
    elif Menuvar.feeling_button == -4:
        Var.screen.blit(Menuvar.pics["Quit"], [280, 210])
    pygame.display.flip()


def close_menue():  # wird in menue_eventloop() verwendet (siehe unten)
    Channels.background_music_menue.stop()
    pygame.time.wait(800)
    Menuvar.pics.clear()
    Var.menue = False
    Channels.background_music.unpause()
    if Var.hero.go:
        Var.hero.start_going = True
    for u in Var.units.values():
        if u.go:
            u.start_going = True


def menue_eventloop():
    for e in pygame.event.get():
        if e.type == pygame.MOUSEBUTTONUP:
            if (e.pos[0] in range(280, 361)):
                if (e.pos[1] in range(135, 151)):
                    Var.screen.blit(Menuvar.pics["Button_Confirm_Borderline"], [280,135])
                    pygame.display.flip()
                    pygame.mixer.Sound(Var.path+"\\sound\\Button_Confirm.wav").play()
                    close_menue()
                elif (e.pos[1] in range(160, 176)):
                    Var.screen.blit(Menuvar.pics["Button_Confirm_Borderline"], [280,160])
                    pygame.display.flip()
                    pygame.mixer.Sound(Var.path+"\\sound\\Button_Confirm.wav").play()
                    pygame.time.wait(800)
                    Menuvar.loading = True
                    Menuvar.saving_or_loading_is_starting = True
                elif (e.pos[1] in range(185, 201)):
                    Var.screen.blit(Menuvar.pics["Button_Confirm_Borderline"], [280,185])
                    pygame.display.flip()
                    pygame.mixer.Sound(Var.path+"\\sound\\Button_Confirm.wav").play()
                    pygame.time.wait(800)
                    Menuvar.saving = True
                    Menuvar.saving_or_loading_is_starting = True
                elif (e.pos[1] in range(210, 226)):
                    Var.screen.blit(Menuvar.pics["Button_Confirm_Borderline"], [280,210])
                    pygame.display.flip()
                    pygame.mixer.Sound(Var.path+"\\sound\\Button_Confirm.wav").play()
                    pygame.time.wait(800)
                    Var.done = True
                    
        if e.type == pygame.MOUSEMOTION:
            if ((e.pos[0] in range(280, 361)) and (e.pos[1] in range(135, 151))) or \
                ((e.pos[0] in range(280, 361)) and (e.pos[1] in range(160, 176))) or \
                ((e.pos[0] in range(280, 361)) and (e.pos[1] in range(185, 201))) or \
                ((e.pos[0] in range(280, 361)) and (e.pos[1] in range(210, 226))):
                if (Menuvar.feeling_button == None) or (Menuvar.feeling_button < 0):
                    blub = pygame.mixer.Sound(Var.path+"\\sound\\Button_Feel.wav")
                    blub.set_volume(0.5)
                    blub.play()
                    del blub
                    if e.pos[1] in range(135, 151):
                        Menuvar.feeling_button = 1
                    elif e.pos[1] in range(160, 176):
                        Menuvar.feeling_button = 2
                    elif e.pos[1] in range(185, 201):
                        Menuvar.feeling_button = 3
                    elif e.pos[1] in range(210, 226):
                        Menuvar.feeling_button = 4
            elif Menuvar.feeling_button == 1:
                Menuvar.feeling_button = -1
            elif Menuvar.feeling_button == 2:
                Menuvar.feeling_button = -2
            elif Menuvar.feeling_button == 3:
                Menuvar.feeling_button = -3
            elif Menuvar.feeling_button == 4:
                Menuvar.feeling_button = -4

        if e.type == pygame.KEYUP:
            if (e.key == pygame.K_ESCAPE) and not Menuvar.esc_used:
                close_menue()
    pygame.event.pump()


def blast_menue():
    Var.hero.sounds["footsteps_sound"].stop()
    for u in Var.units.values():
        u.sounds["footsteps_sound"].stop()
    Channels.background_music_menue.play(Menuvar.music, loops=-1)


def handle_menue():
    pygame.mouse.set_visible(True)
    pygame.mouse.set_cursor((8,8), (0,0), Var.hl_standard_cursor[0], Var.hl_standard_cursor[1])
    if (not Menuvar.saving) and (not Menuvar.loading):
        draw_menue()
        menue_eventloop()
        if Menuvar.starting:
            if not Menuvar.saving_or_loading_just_closed:
                blast_menue()
            else:
                Menuvar.saving_or_loading_just_closed = False
            Menuvar.starting = False
        elif Menuvar.esc_used:
            Menuvar.esc_used = False #verhindert doppeltes schließen hintereinander
    else:
        if Menuvar.saving:
            saver.save()
        elif Menuvar.loading:
            loader.load()
        




            
