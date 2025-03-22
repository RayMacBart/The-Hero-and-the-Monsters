"""module with all basic drawable type class definitions without complex gameplay affecting attributes and functions. For player figure's' class definition see hero.py and for all the other more complex, specific sprite's class definitions see unit.py"""

import pygame
from pool import Var
import figure_functions
import other_functions
import checker


## class Basic
## ... __init__(name, typ, pos, transparency=255, ID=0)
## class Animated_Notmasked
## ... __init__(name, typ, pos, quantity, rate_duration, chaos=False, transparency=255, ID=0)
## class Character
## ... __init__(name, typ, pos, transparency=255, ID=0)
## class Dead
## ... __init__(name, typ, die_typ, direction, pos, transparency=255, ID=0)
## class Obstacle
## ... __init__(name, typ, pos, realpos_offsets, transparency=255, ID=0)
## class Animated_obstacle
## ... __init__(name, typ, pos, realpos_offsets, quantity, rate_duration, chaos=False, transparency=255, ID=0)
## class High_obstacle
## ... __init__(name, typ, pos, realpos_offsets, transparency=255, ID=0)
## class Inclined_high_obstacle
## ... __init__(name, typ, pos, L_y_offset, R_y_offset, x_offset, transparency=255, ID=0)
## class Animated_high_obstacle
## ... __init__(name, typ, pos, realpos_offsets, quantity, rate_duration, chaos=False, transparency=255, ID=0)
## class Border
## ... __init__(name, typ, pos, transparency=255, ID=0)
## class High_border
## ... __init__(name, typ, pos, transparency=255, ID=0)
## class Door
## ... __init__(name, typ, pos, realpos_offsets, quantity, rate_duration, chaos=False, transparency=255, ID=0)
## ... check_dir_name_for_start_pics()
## ... reload_maskpic()
## ... open()
## ... close()
## ... check_triggering()
## ... check_action(clickpos)


class Basic(object):
    def __init__(self, name, typ, pos, transparency=255, ID=0):
        checker.check_basic_init(name, pos)
        if not ID:
            self.ID = Var.IDG
            Var.IDG += 1
        else:
            self.ID = ID
        self.name = name
        self.typ = typ
        self.pos = pos
        self.realpos = [pos[0], pos[1]]
        self.layerpos = [pos[0], pos[1]]
        self.transparency = transparency
        if self.typ not in ["Hero", "Char", "Monster", "Border", "High_border", "Door", \
                            "Obstacle", "High_obstacle", "Animated_obstacle", "Animated_Background", "Animated_Decoration", "Animated_Overlay"]:
            if self.typ == "Ground":
                self.image = pygame.image.load(Var.path+'\\pics\\Grounds\\'+name.split('_')[0]+'\\'+name+'.png').convert()
            elif self.typ == "Background":
                self.image = pygame.image.load(Var.path+'\\pics\\Backgrounds\\'+name.split('_')[0]+'\\'+name+'.png').convert()
            elif self.typ == "Decoration":
                self.image = pygame.image.load(Var.path+'\\pics\\Decorations\\'+name.split('_')[0]+'\\'+name+'.png').convert()
            elif self.typ == "Overlay":
                self.image = pygame.image.load(Var.path+'\\pics\\Overlays\\'+name.split('_')[0]+'\\'+name+'.png').convert()
            elif self.typ == "dead_Monster":
                self.image = pygame.image.load(Var.path+"\\pics\\Monsters\\"+name.split('_')[0]+'\\'+name+"_empty.png").convert()
            else:
                self.image = pygame.image.load(Var.path+'\\pics\\'+name+'.png').convert()
            self.image.set_colorkey([0,0,0], pygame.RLEACCEL)
            self.image.set_alpha(transparency, pygame.RLEACCEL)
            self.width = self.image.get_rect().width
            self.height = self.image.get_rect().height
            self.rect = pygame.Rect([pos[0], pos[1]], [self.width, self.height])
            self.realpos = [pos[0]+self.width//2, pos[1]+self.height]
            self.layerpos = [pos[0]+self.width//2, pos[1]+self.height]
        



class Animated_Notmasked(Basic):
    def __init__(self, name, typ, pos, quantity, rate_duration, chaos=False, transparency=255, ID=0):
        Basic.__init__(self, name, typ, pos, transparency, ID)
        self.quantity = quantity
        self.current_pic = 1
        self.rate_duration = rate_duration
        self.chaos = chaos
        self.blit_now = True
        self.last_pictime = pygame.time.get_ticks()
        self.images = {}
        for i in range(self.quantity):
            if self.typ == "Animated_Background":
                self.images[i+1] = pygame.image.load(Var.path+'\\pics\\Backgrounds\\'+self.name+'\\'+self.name+'_'+str(i+1)+'.png').convert()
            elif self.typ == "Animated_Decoration":
                self.images[i+1] = pygame.image.load(Var.path+'\\pics\\Decorations\\'+self.name+'\\'+self.name+'_'+str(i+1)+'.png').convert()
            elif self.typ == "Animated_Overlay":
                self.images[i+1] = pygame.image.load(Var.path+'\\pics\\Overlays\\'+self.name+'\\'+self.name+'_'+str(i+1)+'.png').convert()
            self.images[i+1].set_colorkey([0,0,0], pygame.RLEACCEL)
            self.images[i+1].set_alpha(self.transparency, pygame.RLEACCEL)
        self.width = self.images[1].get_rect().width
        self.height = self.images[1].get_rect().height
        self.rect = pygame.Rect([pos[0], pos[1]], [self.width, self.height])
        self.realpos = [pos[0]+self.width//2, pos[1]+self.height]
        self.layerpos = [pos[0]+self.width//2, pos[1]+self.height]


		
class Character(Basic):
    def __init__(self, name, typ, pos, transparency=255, ID=0):
        Basic.__init__(self, name, typ, pos, transparency, ID)
        self.dir = "S"
        if self.typ == "Hero":
            self.image = pygame.image.load(Var.path+'\\pics\\Hero\\'+name+'_'+self.dir+'_Stand.png').convert_alpha()
        elif self.typ == "Char":
            self.image = pygame.image.load(Var.path+'\\pics\\Chars\\'+name.split('_')[0]+'\\'+name+'.png').convert_alpha()
        elif self.typ == "Monster":
            self.image = pygame.image.load(Var.path+'\\pics\\Monsters\\'+name.split('_')[0]+'\\'+name+'.png').convert_alpha()
        self.image.set_colorkey([0,0,0], pygame.RLEACCEL)
        self.sounds = {}
        self.last_sound_played = 0  # = um sehr schnelle Soundabspielungen hintereinander zu verhindern
        self.width = self.image.get_rect().width
        self.height = self.image.get_rect().height
        self.rect = pygame.Rect([pos[0], pos[1]], [self.width, self.height])
        self.realpos = [self.pos[0]+self.width//2, self.pos[1]+self.height//2+10]
        self.layerpos = [self.pos[0]+self.width//2, self.pos[1]+self.height//2+10]
        self.current_absolute_pos = [self.realpos[0] - Var.ref_point[0], self.realpos[1] - Var.ref_point[1]]
        self.absolute_destination = [self.realpos[0] - Var.ref_point[0], self.realpos[1] - Var.ref_point[1]]
        if not self.name in ["Ork"]:
            self.maskpic = pygame.image.load(Var.path+'\\pics\\Character_Mask.png').convert()
            self.maskpic.set_colorkey([0,0,0], pygame.RLEACCEL)
            self.mask = pygame.mask.from_surface(self.maskpic, 10)
            self.straight_maskpic = pygame.image.load(Var.path+'\\pics\\Straight_Character_Mask.png').convert()
            self.straight_maskpic.set_colorkey([0,0,0], pygame.RLEACCEL)
            self.straight_mask = pygame.mask.from_surface(self.straight_maskpic, 10)
            self.x_maskpic = pygame.image.load(Var.path+'\\pics\\X-Character_Mask.png').convert()
            self.x_maskpic.set_colorkey([0,0,0], pygame.RLEACCEL)
            self.x_mask = pygame.mask.from_surface(self.x_maskpic, 10)
            self.click_maskpic = pygame.image.load(Var.path+'\\pics\\Character_Clickmask.png').convert()
            self.click_maskpic.set_colorkey([0,0,0], pygame.RLEACCEL)
            self.click_mask = pygame.mask.from_surface(self.click_maskpic, 10)
            self.marker = pygame.image.load(Var.path+'\\pics\\Marker.png').convert()
            self.marker.set_colorkey([0,0,0], pygame.RLEACCEL)
            self.marker.set_alpha(100, pygame.RLEACCEL)
            self.defmarker = pygame.image.load(Var.path+'\\pics\\Defmarker.png').convert()
            self.defmarker.set_colorkey([0,0,0], pygame.RLEACCEL)
            self.defmarker.set_alpha(100, pygame.RLEACCEL)
            self.attackmarker = pygame.image.load(Var.path+'\\pics\\Attackmarker.png').convert()
            self.attackmarker.set_colorkey([0,0,0], pygame.RLEACCEL)
            self.attackmarker.set_alpha(100, pygame.RLEACCEL)
            self.fight_feelmask_pic = pygame.image.load(Var.path+'\\pics\\Character_Fightfeel_Mask.png').convert() # Kampfbereitschafts-Fühlmaske
            self.fight_feelmask_pic.set_colorkey([0,0,0], pygame.RLEACCEL)
            self.fight_feelmask = pygame.mask.from_surface(self.fight_feelmask_pic, 10)
            self.bigmask_pic = pygame.image.load(Var.path+'\\pics\\Character_Big_Mask.png').convert() # Abstandhaltermaske für mehrere Feinde!
            self.bigmask_pic.set_colorkey([0,0,0], pygame.RLEACCEL)
            self.bigmask = pygame.mask.from_surface(self.bigmask_pic, 10)
        self.current_way = [0, 0]
        self.border_dir = ""
        self.collision_direction = None
        self.walk_animation_progress = 0
        self.current_pics = {}
        folder = ""
        if self.typ == "Monster":
            folder = "Monsters\\"
        self.current_pics["Stand"] = pygame.image.load(Var.path+"\\pics\\"+folder+self.name.split('_')[0]+'\\'+self.name+"_"+self.dir+"_Stand.png").convert_alpha()
        self.current_pics["Go_R1"] = pygame.image.load(Var.path+"\\pics\\"+folder+self.name.split('_')[0]+'\\'+self.name+"_"+self.dir+"_Go_R1.png").convert_alpha()
        self.current_pics["Go_R2"] = pygame.image.load(Var.path+"\\pics\\"+folder+self.name.split('_')[0]+'\\'+self.name+"_"+self.dir+"_Go_R2.png").convert_alpha()
        self.current_pics["Go_L1"] = pygame.image.load(Var.path+"\\pics\\"+folder+self.name.split('_')[0]+'\\'+self.name+"_"+self.dir+"_Go_L1.png").convert_alpha()
        self.current_pics["Go_L2"] = pygame.image.load(Var.path+"\\pics\\"+folder+self.name.split('_')[0]+'\\'+self.name+"_"+self.dir+"_Go_L2.png").convert_alpha()
        
        #figure_functions.reload_pics(self)
        self.go = False
        self.start_going = False  # used in blast
        self.fighting = False
        self.dead = False
        
        self.frameway = [0, 0]
        self.movement_skip_at_frame = 1 #je niedriger desto langsamer, used in execute_movement
        self.movement_skip_countdown = self.movement_skip_at_frame  # used in execute_movement
        self.other_blitted_masktypes = [] # used in handle_collision
        self.last_frameways = [[2,2],[2,2],[2,2],[2,2],[2,2]]
        self.footstep_sound_active = False


class Dead(Basic):
    def __init__(self, name, typ, die_typ, direction, pos, transparency=255, ID=0):
        Basic.__init__(self, name, typ, pos, transparency, ID)
        self.name = name
        self.typ = typ
        self.die_typ = die_typ
        self.dir = direction
        self.pos = pos
        self.alpha = 245
        self.ID = ID
        self.TPP = 266  # 266 ist ca. 1 Minute FADE-AWAY-TIME
        self.LPT = 0
        self.die_time = pygame.time.get_ticks()
        if self.name == "Hero":
            self.image = pygame.image.load(Var.path+"\\pics\\Hero\\Die\\"+self.name+"_"+self.dir+"_Die"+str(self.die_typ)+"_26.png").convert()
        elif self.typ == "dead_Monster":
            self.image = pygame.image.load(Var.path+"\\pics\\Monsters\\"+self.name.split('_')[0]+"\\Die\\"+self.name+"_"+self.dir+"_Die"+self.die_typ+"_26.png").convert()
            self.image.set_colorkey([0,0,0], pygame.RLEACCEL)
            self.image.set_alpha(self.alpha, pygame.RLEACCEL)
            


class Obstacle(Basic):
    def __init__(self, name, typ, pos, realpos_offsets, transparency=255, ID=0):
        Basic.__init__(self, name, typ, pos, transparency, ID)
        if self.typ == "Obstacle" or self.typ == "High_obstacle" or self.typ == "Animated_obstacle":
            if self.typ == "Obstacle" or self.typ == "High_obstacle":
                self.image = pygame.image.load(Var.path+'\\pics\\Obstacles\\'+name.split('_')[0]+'\\'+name+'.png').convert()
                self.image.set_colorkey([0,0,0], pygame.RLEACCEL)
                self.width = self.image.get_rect().width
                self.height = self.image.get_rect().height
                self.rect = pygame.Rect([pos[0], pos[1]], [self.width, self.height])
            self.maskpic = pygame.image.load(Var.path+'\\pics\\Obstacles\\'+name.split('_')[0]+'\\'+name+'_Mask.png').convert()
            self.maskpic.set_colorkey([0,0,0], pygame.RLEACCEL)
            self.mask = pygame.mask.from_surface(self.maskpic, 10)
        self.realpos = [self.pos[0]+realpos_offsets[0], self.pos[1]+realpos_offsets[1]]
        self.layerpos = [self.pos[0]+realpos_offsets[0], self.pos[1]+realpos_offsets[1]]


class Animated_obstacle(Obstacle):
    def __init__(self, name, typ, pos, realpos_offsets, quantity, rate_duration, chaos=False, transparency=255, ID=0):
        Obstacle.__init__(self, name, typ, pos, realpos_offsets, transparency, ID)
        self.quantity = quantity
        self.current_pic = 1
        self.rate_duration = rate_duration
        self.chaos = chaos
        self.blit_now = True
        self.last_pictime = pygame.time.get_ticks()
        self.images = {}
        
        for i in range(self.quantity):
            if not self.typ == "Door":
                self.images[i+1] = pygame.image.load(Var.path+'\\pics\\Obstacles\\'+name.split('_')[0]+'\\'+name+'_'+str(i+1)+'.png').convert()
                self.images[i+1].set_colorkey([0,0,0], pygame.RLEACCEL)
                self.images[i+1].set_alpha(self.transparency, pygame.RLEACCEL)
            else:
                self.images[1] = pygame.image.load(Var.path+'\\pics\\Objects\\'+name.split('_')[0]+'\\'+name+'.png').convert()
        self.width = self.images[1].get_rect().width
        self.height = self.images[1].get_rect().height
        self.rect = pygame.Rect([pos[0], pos[1]], [self.width, self.height])

		
class High_obstacle(Obstacle):
    def __init__(self, name, typ, pos, realpos_offsets, transparency=255, ID=0):
        Obstacle.__init__(self, name, typ, pos, realpos_offsets, transparency, ID)
        if self.typ in ["High_obstacle", "Inclined_high_obstacle"]:
            self.image_shiny = pygame.image.load(Var.path+'\\pics\\Obstacles\\'+name.split('_')[0]+'\\'+name+'_Shiny.png').convert()
            self.image_shiny.set_colorkey([0,0,0], pygame.RLEACCEL)
            self.image_shiny.set_alpha(170, pygame.RLEACCEL)
        self.transparent = False

		
class Inclined_high_obstacle(High_obstacle):
    def __init__(self, name, typ, pos, L_y_offset, R_y_offset, x_offset, transparency=255, ID=0):
        High_obstacle.__init__(self, name, typ, pos, [x_offset, (((L_y_offset+((R_y_offset-L_y_offset)//2)) if (L_y_offset<R_y_offset) else (R_y_offset+(L_y_offset-R_y_offset)//2)))], transparency, ID)
        self.L_y_offset = L_y_offset
        self.R_y_offset = R_y_offset
        self.x_offset = x_offset


class Animated_high_obstacle(Animated_obstacle):
    def __init__(self, name, typ, pos, realpos_offsets, quantity, rate_duration, chaos=False, transparency=255, ID=0):
        Animated_obstacle.__init__(self, name, typ, pos, realpos_offsets, quantity, rate_duration, chaos, transparency, ID)
        self.images_shiny = {}
        if self.typ == "Animated_high_obstacle":
            for i in range(self.quantity):
                self.images_shiny[i+1] = pygame.image.load(Var.path+'\\pics\\Obstacles\\'+name.split('_')[0]+'\\'+name+'_'+str(i+1)+'_Shiny.png.png').convert()
                self.images_shiny[i+1].set_colorkey([0,0,0], pygame.RLEACCEL)
                self.images_shiny[i+1].set_alpha(170, pygame.RLEACCEL)
        self.transparent = False


class Border(Basic):
    def __init__(self, name, typ, pos, transparency=255, ID=0):
        Basic.__init__(self, name, typ, pos, transparency, ID)
#        self.location = location  # = welche Richtung vom Character aus gesehen begrenzt wird, z.B. "_NW"
        self.image = pygame.image.load(Var.path+'\\pics\\Borders\\'+name.split('_')[0]+'\\'+name+'.png').convert()
        self.image.set_colorkey([0,0,0], pygame.RLEACCEL)
        self.width = self.image.get_rect().width
        self.height = self.image.get_rect().height
        self.rect = pygame.Rect([pos[0], pos[1]], [self.width, self.height])
        self.maskpic = pygame.image.load(Var.path+'\\pics\\Borders\\Bordermasks\\Bordermask'+name.lstrip(name.split('_')[0])+'.png').convert()
        self.maskpic.set_colorkey([0,0,0], pygame.RLEACCEL)
        self.mask = pygame.mask.from_surface(self.maskpic, 10)
#        self.image_fog = pygame.image.load(Var.path+'\\pics\\Fogs\\Fog'+name.lstrip(name.split("_")[0])+'_'+location+'.png').convert()
#        self.image_fog.set_colorkey([0,0,0], pygame.RLEACCEL)
#        self.image_fog.set_alpha(200, pygame.RLEACCEL)
        self.realpos = [pos[0]+self.width//2, pos[1]]
        self.layerpos = [pos[0]+self.width//2, pos[1]]
        


class High_border(Border):
    def __init__(self, name, typ, pos, transparency=255, ID=0):
        Border.__init__(self, name, typ, pos, transparency, ID)
        self.image_shiny = pygame.image.load(Var.path+'\\pics\\Borders\\'+name.split('_')[0]+'\\'+name+'_Shiny.png').convert()
        self.image_shiny.set_colorkey([0,0,0], pygame.RLEACCEL)
        self.image_shiny.set_alpha(170, pygame.RLEACCEL)
        self.transparent = False



class Door(Animated_obstacle):
    def __init__(self, name, typ, pos, realpos_offsets=[50,94], quantity=6, rate_duration=160, chaos=False, transparency=255, ID=0):
        Animated_obstacle.__init__(self, name, typ, pos, realpos_offsets, quantity, rate_duration, chaos, transparency, ID)
        self.dir = self.check_dir_name_for_start_pics()
        self.images.clear()
        for i in range(self.quantity):
            self.images[i+1] = pygame.image.load(Var.path+'\\pics\\Objects\\'+name.split('_')[0]+'\\'+name+'_'+self.dir+'-'+str(i+1)+'.png').convert()
            self.images[i+1].set_colorkey([0,0,0], pygame.RLEACCEL)
            self.images[i+1].set_alpha(self.transparency, pygame.RLEACCEL)
        self.width = self.images[1].get_rect().width
        self.height = self.images[1].get_rect().height
        self.rect = pygame.Rect([pos[0], pos[1]], [self.width, self.height])
        self.open_sound = pygame.mixer.Sound(Var.path+"\\sound\\door_opening.wav")
        self.open_sound.set_volume(0.4)
        self.close_sound = pygame.mixer.Sound(Var.path+"\\sound\\door_closing.wav")
        self.close_sound.set_volume(0.4)
        self.click_sound = pygame.mixer.Sound(Var.path+"\\sound\\clicksound_2.wav")
        self.status = "closed" #weitere: "opening", "closing", "open"
        self.current_pic = 1
        self.in_focus = False  # True, wenn Tür durch hero per Click anvisiert wurde und dieser auf dem Weg zu ihr ist.
        self.welcome_point = [-1, -1]
        self.blitcopydone = False  # Nur fürs Blitting offener OU-Doors verwendet in Drawer
        self.doorcopy = 0          # -"-
        self.I_am_doorcopy = False #

        self.maskpic = pygame.image.load(Var.path+'\\pics\\Objects\\'+name.split('_')[0]+'\\'+name+'_'+self.status+'_Mask.png').convert()
        self.maskpic.set_colorkey([0,0,0], pygame.RLEACCEL)
        self.mask = pygame.mask.from_surface(self.maskpic, 10)

        #Mask, wo Hero reinkommen muss, um Tür betätigen zu können (Nach Mausklick!):
        self.trigger_maskpic = pygame.image.load(Var.path+'\\pics\\Objects\\'+name.split('_')[0]+'\\'+name+'_Triggermask.png').convert() #####
        self.trigger_maskpic.set_colorkey([0,0,0], pygame.RLEACCEL) #####
        self.trigger_mask = pygame.mask.from_surface(self.trigger_maskpic, 10) #####

        #Mask, wo Rechtsklick stattfinden muss (Mausposition) - quasi die Tür selbst:
        self.click_maskpic = pygame.image.load(Var.path+'\\pics\\Objects\\'+name.split('_')[0]+'\\'+name+'_Clickmask.png').convert() #####
        self.click_maskpic.set_colorkey([0,0,0], pygame.RLEACCEL) #####
        self.click_mask = pygame.mask.from_surface(self.click_maskpic, 10) #####

    def check_dir_name_for_start_pics(self):  #nur damit erstes Bilderladen funktioniert (eher unwichtig)
        if 'LR' in self.name:
            return 'O'
        elif 'OU' in self.name:
            return 'L'
        elif 'OR-UL' in self.name:
            return 'UL'
        elif 'UR-OL' in self.name:
            return 'UR'

    def reload_maskpic(self):   # Nur beim Laden notwendig
        self.maskpic = pygame.image.load(Var.path+'\\pics\\Objects\\'+self.name.split('_')[0]+'\\'+self.name+'_'+self.status+'_Mask.png').convert()
        self.maskpic.set_colorkey([0,0,0], pygame.RLEACCEL)
        self.mask = pygame.mask.from_surface(self.maskpic, 10)
    
    def open(self):    # in Calculator aufgerufen, wenn status 'opening' ist
        if not (self.current_pic == self.quantity):
            if self.last_pictime + self.rate_duration < pygame.time.get_ticks():
                self.last_pictime = pygame.time.get_ticks()
                self.current_pic += 1
                self.blit_now = True
        else:
            self.status = 'open'
            self.maskpic = pygame.image.load(Var.path+'\\pics\\Objects\\'+self.name.split('_')[0]+'\\'+self.name+'_open_Mask.png').convert()
            self.maskpic.set_colorkey([0,0,0], pygame.RLEACCEL)
            self.mask = pygame.mask.from_surface(self.maskpic, 10)

    def close(self):
        if not (self.current_pic == 1):
            if self.last_pictime + self.rate_duration < pygame.time.get_ticks():
                self.last_pictime = pygame.time.get_ticks()
                self.current_pic -= 1
                self.blit_now = True
        else:
            self.status = 'closed'
            self.maskpic = pygame.image.load(Var.path+'\\pics\\Objects\\'+self.name.split('_')[0]+'\\'+self.name+'_closed_Mask.png').convert()
            self.maskpic.set_colorkey([0,0,0], pygame.RLEACCEL)
            self.mask = pygame.mask.from_surface(self.maskpic, 10)

    def check_triggering(self):
        try:
            if self.trigger_mask.get_at([Var.hero.realpos[0]-self.pos[0], Var.hero.realpos[1]-self.pos[1]]):
                self.in_focus = False
                if self.status == "closed":
                    self.status = "opening"
                    self.open_sound.play()
                elif self.status == "open":
                    self.status = "closing"
                    self.close_sound.play()
        except IndexError:
            pass
            
    def check_action(self, clickpos): # wird nur bei Rechtsklick ausgelöst
        if (self in Var.blitlist) and ((self.status != 'opening') and (self.status != 'closing')):
            try:
                if self.click_mask.get_at([clickpos[0]-self.pos[0], clickpos[1]-self.pos[1]]):
                    self.click_sound.play()
                    Var.action_cursor["start"] = True
                    Var.action_cursor["cursor"] = "open_door" if (self.status == "closed") else "close_door"
                    self.in_focus = True
                    Var.hero.go = True
                    Var.hero.start_going = True
                    Var.hero.sounds["footsteps_sound"].stop()
                    if 'LR' in self.name:
                        if Var.hero.realpos[1] < self.pos[1]+80:
                            self.dir = 'U'
                            Var.hero.absolute_destination = [(self.pos[0]+50)-Var.ref_point[0], (self.pos[1]+60)-Var.ref_point[1]]
                        elif Var.hero.realpos[1] > self.pos[1]+80:
                            self.dir = 'O'
                            Var.hero.absolute_destination = [(self.pos[0]+50)-Var.ref_point[0], (self.pos[1]+100)-Var.ref_point[1]]
                    elif 'OU' in self.name:
                        if Var.hero.realpos[0] < self.pos[0]+50:
                            self.dir = 'R'
                            Var.hero.absolute_destination = [(self.pos[0]+15)-Var.ref_point[0], (self.pos[1]+69)-Var.ref_point[1]]
                        elif Var.hero.realpos[0] > self.pos[0]+50:
                            self.dir = 'L'
                            Var.hero.absolute_destination = [(self.pos[0]+84)-Var.ref_point[0], (self.pos[1]+69)-Var.ref_point[1]]
                    elif 'OR-UL' in self.name:
                        if (Var.hero.realpos[0]-self.pos[0])-(Var.hero.realpos[1]-self.pos[1]) < 20:
                            self.dir = 'OR'
                            Var.hero.absolute_destination = [(self.pos[0]+67)-Var.ref_point[0], (self.pos[1]+109)-Var.ref_point[1]]
                        elif (Var.hero.realpos[0]-self.pos[0])-(Var.hero.realpos[1]-self.pos[1]) > 20:
                            self.dir = 'UL'
                            Var.hero.absolute_destination = [(self.pos[0]+120)-Var.ref_point[0], (self.pos[1]+68)-Var.ref_point[1]]
                    elif 'UR-OL' in self.name:
                        if (Var.hero.realpos[0]-self.pos[0])+(Var.hero.realpos[1]-self.pos[1]) < 182:
                            self.dir = 'UR'
                            Var.hero.absolute_destination = [(self.pos[0]+81)-Var.ref_point[0], (self.pos[1]+68)-Var.ref_point[1]]
                        elif (Var.hero.realpos[0]-self.pos[0])+(Var.hero.realpos[1]-self.pos[1]) > 182:
                            self.dir = 'OL'
                            Var.hero.absolute_destination = [(self.pos[0]+132)-Var.ref_point[0], (self.pos[1]+109)-Var.ref_point[1]]
                    if not self.current_pic == 6:
                        for i in range(self.quantity):
                            self.images[i+1] = pygame.image.load(Var.path+'\\pics\\Objects\\'+self.name.split('_')[0]+'\\'+self.name+'_'+self.dir+'-'+str(i+1)+'.png').convert()
                            self.images[i+1].set_colorkey([0,0,0], pygame.RLEACCEL)
                            self.images[i+1].set_alpha(self.transparency, pygame.RLEACCEL)
            except IndexError:
                #print("IndexError @ Door-Rightclick", [clickpos[0]-self.pos[0], clickpos[1]-self.pos[1]])
                pass

                
