import pygame
from pool import Var
from pool import Channels


## blast()
## setup_hero_sounds(hero)
## setup_ork_sounds(ork)


def blast():
    if not Channels.background_music.get_busy():
        if Var.current_music_track <= len(Var.music):
            Var.current_music = pygame.mixer.Sound(Var.path+"\\sound\\"+Var.music[Var.current_music_track - 1]+".wav")
            Channels.background_music.play(Var.current_music)
            Var.current_music_track += 1
        else:
            Var.current_music = pygame.mixer.Sound(Var.path+"\\sound\\"+Var.music[0]+".wav")
            Channels.background_music.play(Var.current_music)
            Var.current_music_track = 2
    if Var.hero.go:
        if Var.hero.start_going:
            if not Var.hero.drawn:
                Var.hero.sounds["footsteps_sound"].play(loops=-1)
                Var.hero.footstep_sound_active = True
            Var.hero.start_going = False
    for u in Var.units.values():
        if u.go and (u in Var.blitlist) and ((662 > u.realpos[0] > -22) and (445 > u.realpos[1] > -45)):
            if u.start_going:
                if not u.drawn:
                    u.sounds["footsteps_sound"].play(loops=-1)
                    u.footstep_sound_active = True
                u.start_going = False
        elif u.go and u.footstep_sound_active: #  = if u not visible on screen!
            u.sounds["footsteps_sound"].stop()
            u.footstep_sound_active = False
            

def setup_hero_sounds(hero):
    hero.sounds["footsteps_sound"] = pygame.mixer.Sound(Var.path+"\\sound\\footsteps.wav")
    hero.sounds["footsteps_sound"].set_volume(0.2)
    hero.sounds["draw_sound"] = pygame.mixer.Sound(Var.path+"\\sound\\draw.wav")
    hero.sounds["draw_sound"].set_volume(0.4)
    hero.sounds["put_away_sound"] = pygame.mixer.Sound(Var.path+"\\sound\\put_away.wav")
    hero.sounds["put_away_sound"].set_volume(0.6)
    hero.sounds["hit_L_sound"] = pygame.mixer.Sound(Var.path+"\\sound\\hit_L.wav")
    hero.sounds["hit_L_sound"].set_volume(0.8)
    hero.sounds["hit_R_sound"] = pygame.mixer.Sound(Var.path+"\\sound\\hit_R.wav")
    hero.sounds["hit_R_sound"].set_volume(0.5)
    hero.sounds["hit_O_sound"] = pygame.mixer.Sound(Var.path+"\\sound\\hit_O.wav")
    hero.sounds["hit_O_sound"].set_volume(1.0)
    hero.sounds["hit_U_sound"] = pygame.mixer.Sound(Var.path+"\\sound\\hit_U.wav")
    hero.sounds["hit_U_sound"].set_volume(0.9)
    hero.sounds["aua_1_sound"] = pygame.mixer.Sound(Var.path+"\\sound\\hero_aua_1.wav")
    hero.sounds["aua_1_sound"].set_volume(0.5)
    hero.sounds["aua_2_sound"] = pygame.mixer.Sound(Var.path+"\\sound\\hero_aua_2.wav")
    hero.sounds["aua_2_sound"].set_volume(0.5)
    hero.sounds["slash_L_sound"] = pygame.mixer.Sound(Var.path+"\\sound\\hero_slash_L.wav")
    hero.sounds["slash_L_sound"].set_volume(0.9)
    hero.sounds["slash_R_sound"] = pygame.mixer.Sound(Var.path+"\\sound\\hero_slash_R.wav")
    hero.sounds["slash_R_sound"].set_volume(0.4)
    hero.sounds["slash_O_sound"] = pygame.mixer.Sound(Var.path+"\\sound\\hero_slash_O.wav")
    hero.sounds["slash_O_sound"].set_volume(0.6)
    hero.sounds["slash_U_sound"] = pygame.mixer.Sound(Var.path+"\\sound\\hero_slash_U.wav")
    hero.sounds["slash_U_sound"].set_volume(0.4)
    hero.sounds["die_sound"] = pygame.mixer.Sound(Var.path+"\\sound\\hero_die.wav")
    hero.sounds["die_sound"].set_volume(0.6)

def setup_ork_sounds(ork):
    ork.sounds["footsteps_sound"] = pygame.mixer.Sound(Var.path+"\\sound\\footsteps.wav")
    ork.sounds["footsteps_sound"].set_volume(0.2)
    ork.sounds["draw_sound"] = pygame.mixer.Sound(Var.path+"\\sound\\draw.wav")
    ork.sounds["draw_sound"].set_volume(0.4)
    ork.sounds["put_away_sound"] = pygame.mixer.Sound(Var.path+"\\sound\\put_away.wav")
    ork.sounds["put_away_sound"].set_volume(0.6)
    ork.sounds["attention_sound"] = pygame.mixer.Sound(Var.path+"\\sound\\ork_attention.wav")
    ork.sounds["attention_sound"].set_volume(1.0)
    ork.sounds["hit_L_sound"] = pygame.mixer.Sound(Var.path+"\\sound\\hit_L.wav")
    ork.sounds["hit_L_sound"].set_volume(0.7)
    ork.sounds["hit_R_sound"] = pygame.mixer.Sound(Var.path+"\\sound\\hit_R.wav")
    ork.sounds["hit_R_sound"].set_volume(0.4)
    ork.sounds["hit_O_sound"] = pygame.mixer.Sound(Var.path+"\\sound\\hit_O.wav")
    ork.sounds["hit_O_sound"].set_volume(0.9)
    ork.sounds["hit_U_sound"] = pygame.mixer.Sound(Var.path+"\\sound\\hit_U.wav")
    ork.sounds["hit_U_sound"].set_volume(0.8)
    ork.sounds["aua_1_sound"] = pygame.mixer.Sound(Var.path+"\\sound\\ork_aua_1.wav")
    ork.sounds["aua_1_sound"].set_volume(0.9)
    ork.sounds["aua_2_sound"] = pygame.mixer.Sound(Var.path+"\\sound\\ork_aua_2.wav")
    ork.sounds["aua_2_sound"].set_volume(1.0)
    ork.sounds["slash_L_sound"] = pygame.mixer.Sound(Var.path+"\\sound\\ork_slash_L.wav")
    ork.sounds["slash_L_sound"].set_volume(0.8)
    ork.sounds["slash_R_sound"] = pygame.mixer.Sound(Var.path+"\\sound\\ork_slash_R.wav")
    ork.sounds["slash_R_sound"].set_volume(0.7)
    ork.sounds["slash_O_sound"] = pygame.mixer.Sound(Var.path+"\\sound\\ork_slash_O.wav")
    ork.sounds["slash_O_sound"].set_volume(0.7)
    ork.sounds["slash_U_sound"] = pygame.mixer.Sound(Var.path+"\\sound\\ork_slash_U.wav")
    ork.sounds["slash_U_sound"].set_volume(1.0)
    ork.sounds["die_sound"] = pygame.mixer.Sound(Var.path+"\\sound\\ork_die.wav")
    ork.sounds["die_sound"].set_volume(0.6)
