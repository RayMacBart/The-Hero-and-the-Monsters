"""Module with all shared standard variables including sprite lists in class Var and all time related variables in class Count"""

import pygame


## class Var
## class Channels
## class Count
## ... __init__()
## ... start_count(milliseconds, count_name="")
## ... check_if_ending()
## ... check_count_time()


class Var():
    size = [640, 400]   
    screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
    clock = pygame.time.Clock()
    done = False
    path = "C:\\Users\\reinh\\AppData\\Local\\Programs\\Python\\Python38-32\\Game 640x400"
    menue = True
    music = ["Constant Structure"]
    current_music = pygame.mixer.Sound(path+"\\sound\\"+music[0]+".wav")
    current_music_track = 1
    action_cursor = {"start":False, "active":False, "cursor":None, "CPN":1, "TPP":90, "LPT":0}
    cursor_feels = False
    go_point = {"active":False, "start":False,"images":{},"CPN":1,"TPP":80, "LPT":0, "pos":[0,0]}
    main_background = ""
    blitlist = []   # Elemente: Objekte (Im Sinne von Klasseninstanzen)
    sorted_blitlist = []   # Elemente: Tupel mit image & pos
    ref_point = [0,0]
    current_blitmaps = []
    grounds = {}
    backgrounds = {}
    animated_backgrounds = {}
    decorations = {}  # Not mapped pics without collision masks accounted @ blitorder
    animated_decorations = {}
    overlays = {}
    animated_overlays = {}
    borders = {}
    obstacles = {}  # non-character-pics with collision-mask!
    animated_obstacles = {}
    doors = {}
    units = {}
    dead = []
    IDG = 0  # ID-Generator
    frames_since_last_click = 0
    fight = None
    last_fightclick = 0
    mouse_pos = (0,0)
    game_over = None
    canvas_marker = pygame.image.load('C:\\Users\\reinh\\AppData\\Local\\Programs\\Python\\Python38-32\\Game 640x400\\pics\\Canvas_Marker.png').convert()
    screen_scrolling_happened = True
    start_redframe = False

    current_level = 1
    level_upset = False
    level_rising = False


class BS():  # Battle-Symbols
    x_hero = pygame.image.load(Var.path+'\\pics\\Battle_Symbols\\BS_X_hero.png').convert()
    x_hero.set_colorkey([0,0,0], pygame.RLEACCEL)
    x_hero.set_alpha(120, pygame.RLEACCEL)
    o_hero = pygame.image.load(Var.path+'\\pics\\Battle_Symbols\\BS_o_hero.png').convert()
    o_hero.set_colorkey([0,0,0], pygame.RLEACCEL)
    o_hero.set_alpha(120, pygame.RLEACCEL)
    x_enemy = pygame.image.load(Var.path+'\\pics\\Battle_Symbols\\BS_X_enemy.png').convert()
    x_enemy.set_colorkey([0,0,0], pygame.RLEACCEL)
    x_enemy.set_alpha(120, pygame.RLEACCEL)
    o_enemy = pygame.image.load(Var.path+'\\pics\\Battle_Symbols\\BS_o_enemy.png').convert()
    o_enemy.set_colorkey([0,0,0], pygame.RLEACCEL)
    o_enemy.set_alpha(120, pygame.RLEACCEL)
    enemy_flow = pygame.image.load(Var.path+'\\pics\\Battle_Symbols\\Enemy_Flow.png').convert()
    enemy_flow.set_colorkey([0,0,0], pygame.RLEACCEL)
    enemy_flow.set_alpha(150, pygame.RLEACCEL)
    shield_L1 = pygame.image.load(Var.path+'\\pics\\Battle_Symbols\\BS_Shield_L1.png').convert()
    shield_L1.set_colorkey([0,0,0], pygame.RLEACCEL)
    shield_L1.set_alpha(130, pygame.RLEACCEL)
    shield_L2 = pygame.image.load(Var.path+'\\pics\\Battle_Symbols\\BS_Shield_L2.png').convert()
    shield_L2.set_colorkey([0,0,0], pygame.RLEACCEL)
    shield_L2.set_alpha(130, pygame.RLEACCEL)
    shield_L3 = pygame.image.load(Var.path+'\\pics\\Battle_Symbols\\BS_Shield_L3.png').convert()
    shield_L3.set_colorkey([0,0,0], pygame.RLEACCEL)
    shield_L3.set_alpha(130, pygame.RLEACCEL)
    shield_R1 = pygame.image.load(Var.path+'\\pics\\Battle_Symbols\\BS_Shield_R1.png').convert()
    shield_R1.set_colorkey([0,0,0], pygame.RLEACCEL)
    shield_R1.set_alpha(130, pygame.RLEACCEL)
    shield_R2 = pygame.image.load(Var.path+'\\pics\\Battle_Symbols\\BS_Shield_R2.png').convert()
    shield_R2.set_colorkey([0,0,0], pygame.RLEACCEL)
    shield_R2.set_alpha(130, pygame.RLEACCEL)
    shield_R3 = pygame.image.load(Var.path+'\\pics\\Battle_Symbols\\BS_Shield_R3.png').convert()
    shield_R3.set_colorkey([0,0,0], pygame.RLEACCEL)
    shield_R3.set_alpha(130, pygame.RLEACCEL)
    shield_O1 = pygame.image.load(Var.path+'\\pics\\Battle_Symbols\\BS_Shield_O1.png').convert()
    shield_O1.set_colorkey([0,0,0], pygame.RLEACCEL)
    shield_O1.set_alpha(130, pygame.RLEACCEL)
    shield_O2 = pygame.image.load(Var.path+'\\pics\\Battle_Symbols\\BS_Shield_O2.png').convert()
    shield_O2.set_colorkey([0,0,0], pygame.RLEACCEL)
    shield_O2.set_alpha(130, pygame.RLEACCEL)
    shield_O3 = pygame.image.load(Var.path+'\\pics\\Battle_Symbols\\BS_Shield_O3.png').convert()
    shield_O3.set_colorkey([0,0,0], pygame.RLEACCEL)
    shield_O3.set_alpha(130, pygame.RLEACCEL)
    shield_U1 = pygame.image.load(Var.path+'\\pics\\Battle_Symbols\\BS_Shield_U1.png').convert()
    shield_U1.set_colorkey([0,0,0], pygame.RLEACCEL)
    shield_U1.set_alpha(130, pygame.RLEACCEL)
    shield_U2 = pygame.image.load(Var.path+'\\pics\\Battle_Symbols\\BS_Shield_U2.png').convert()
    shield_U2.set_colorkey([0,0,0], pygame.RLEACCEL)
    shield_U2.set_alpha(130, pygame.RLEACCEL)
    shield_U3 = pygame.image.load(Var.path+'\\pics\\Battle_Symbols\\BS_Shield_U3.png').convert()
    shield_U3.set_colorkey([0,0,0], pygame.RLEACCEL)
    shield_U3.set_alpha(130, pygame.RLEACCEL)
    shield_makeup_L1 = pygame.image.load(Var.path+'\\pics\\Battle_Symbols\\BS_Shield_MakeUp_L1.png').convert()
    shield_makeup_L1.set_colorkey([0,0,0], pygame.RLEACCEL)
    shield_makeup_L1.set_alpha(80, pygame.RLEACCEL)
    shield_makeup_L2 = pygame.image.load(Var.path+'\\pics\\Battle_Symbols\\BS_Shield_MakeUp_L2.png').convert()
    shield_makeup_L2.set_colorkey([0,0,0], pygame.RLEACCEL)
    shield_makeup_L2.set_alpha(80, pygame.RLEACCEL)
    shield_makeup_L3 = pygame.image.load(Var.path+'\\pics\\Battle_Symbols\\BS_Shield_MakeUp_L3.png').convert()
    shield_makeup_L3.set_colorkey([0,0,0], pygame.RLEACCEL)
    shield_makeup_L3.set_alpha(80, pygame.RLEACCEL)
    shield_makeup_R1 = pygame.image.load(Var.path+'\\pics\\Battle_Symbols\\BS_Shield_MakeUp_R1.png').convert()
    shield_makeup_R1.set_colorkey([0,0,0], pygame.RLEACCEL)
    shield_makeup_R1.set_alpha(80, pygame.RLEACCEL)
    shield_makeup_R2 = pygame.image.load(Var.path+'\\pics\\Battle_Symbols\\BS_Shield_MakeUp_R2.png').convert()
    shield_makeup_R2.set_colorkey([0,0,0], pygame.RLEACCEL)
    shield_makeup_R2.set_alpha(80, pygame.RLEACCEL)
    shield_makeup_R3 = pygame.image.load(Var.path+'\\pics\\Battle_Symbols\\BS_Shield_MakeUp_R3.png').convert()
    shield_makeup_R3.set_colorkey([0,0,0], pygame.RLEACCEL)
    shield_makeup_R3.set_alpha(80, pygame.RLEACCEL)
    shield_makeup_O1 = pygame.image.load(Var.path+'\\pics\\Battle_Symbols\\BS_Shield_MakeUp_O1.png').convert()
    shield_makeup_O1.set_colorkey([0,0,0], pygame.RLEACCEL)
    shield_makeup_O1.set_alpha(80, pygame.RLEACCEL)
    shield_makeup_O2 = pygame.image.load(Var.path+'\\pics\\Battle_Symbols\\BS_Shield_MakeUp_O2.png').convert()
    shield_makeup_O2.set_colorkey([0,0,0], pygame.RLEACCEL)
    shield_makeup_O2.set_alpha(80, pygame.RLEACCEL)
    shield_makeup_O3 = pygame.image.load(Var.path+'\\pics\\Battle_Symbols\\BS_Shield_MakeUp_O3.png').convert()
    shield_makeup_O3.set_colorkey([0,0,0], pygame.RLEACCEL)
    shield_makeup_O3.set_alpha(80, pygame.RLEACCEL)
    shield_makeup_U1 = pygame.image.load(Var.path+'\\pics\\Battle_Symbols\\BS_Shield_MakeUp_U1.png').convert()
    shield_makeup_U1.set_colorkey([0,0,0], pygame.RLEACCEL)
    shield_makeup_U1.set_alpha(80, pygame.RLEACCEL)
    shield_makeup_U2 = pygame.image.load(Var.path+'\\pics\\Battle_Symbols\\BS_Shield_MakeUp_U2.png').convert()
    shield_makeup_U2.set_colorkey([0,0,0], pygame.RLEACCEL)
    shield_makeup_U2.set_alpha(80, pygame.RLEACCEL)
    shield_makeup_U3 = pygame.image.load(Var.path+'\\pics\\Battle_Symbols\\BS_Shield_MakeUp_U3.png').convert()
    shield_makeup_U3.set_colorkey([0,0,0], pygame.RLEACCEL)
    shield_makeup_U3.set_alpha(80, pygame.RLEACCEL)
    sword_L = pygame.image.load(Var.path+'\\pics\\Battle_Symbols\\BS_Sword_L.png').convert()
    sword_L.set_colorkey([0,0,0], pygame.RLEACCEL)
    sword_R = pygame.image.load(Var.path+'\\pics\\Battle_Symbols\\BS_Sword_R.png').convert()
    sword_R.set_colorkey([0,0,0], pygame.RLEACCEL)
    sword_O = pygame.image.load(Var.path+'\\pics\\Battle_Symbols\\BS_Sword_O.png').convert()
    sword_O.set_colorkey([0,0,0], pygame.RLEACCEL)
    sword_U = pygame.image.load(Var.path+'\\pics\\Battle_Symbols\\BS_Sword_U.png').convert()
    sword_U.set_colorkey([0,0,0], pygame.RLEACCEL)
    

class Frames():
    redframes = []
    for r in range(11):
        redframes.append(pygame.image.load(Var.path+'\\pics\\Overlays\\Redframes\\Redframe_'+str(r+1)+'.png').convert_alpha())
    redframe_CPN = 0
    redframe_TPP = 10
    redframe_LPT = 0
    redframing = False  # start_redframe befindet sich in class Var
    

    
class Channels():
    background_music = pygame.mixer.Channel(0)
    background_music.set_volume(0.1)
    background_music_menue = pygame.mixer.Channel(1)
    background_music_menue.set_volume(0.2)
    signals = pygame.mixer.Channel(6)
    mouse_sounds = pygame.mixer.Channel(7)


class Count():
    def __init__(self):
        self.count_name = ""
        self.counting = False
        self.start = 0
        self.end = 0
    def start_count(self, milliseconds, count_name=""):
        self.start = pygame.time.get_ticks()
        self.end = pygame.time.get_ticks()+milliseconds
        self.count_name = count_name
        self.counting = True
    def check_if_ending(self):
        if (self.end <= pygame.time.get_ticks()) and self.counting:
            self.counting = False
            return True
        else:
            return None
    def check_count_time(self):
        return pygame.time.get_ticks() - self.start
            

