import pygame
from pool import Var


## class Slotvar
## class Slot
## ... __init__(text)
## class Save_Load_Menue_Button
## ... __init__(text, pos)


class Slotvar():
    slots = []
    slot_font = pygame.font.Font(None, 20)
    slot_text_color = (50,20,35)
    menue_buttons = {}
    yes_no_buttons = []
    menue_button_font = pygame.font.Font(None, 17)
    active_menue_button_text_color = (50, 0, 50)
    inactive_menue_button_text_color = (220, 220, 220)
    pressed_menue_button_text_color = (40, 0, 100)
    

class Slot():
    def __init__(self, text):
        self.text = text
        self.file = Var.path+"\\savegames\\"+text+".txt"
        self.text_image = Slotvar.slot_font.render(self.text, True, Slotvar.slot_text_color)
        self.pos = [0,0]
        self.highlighted = False
        self.choosen = False
        self.removing_light = False
        self.getting_light = False
        if len(Slotvar.slots) <= 8:
            self.pos[0] = 100
            self.pos[1] = 60 + 25*len(Slotvar.slots)
        elif len(Slotvar.slots) <= 17:
            self.pos[0] = 270
            self.pos[1] = 60 + 25*(len(Slotvar.slots)-9)
        elif len(Slotvar.slots) <= 26:
            self.pos[0] = 440
            self.pos[1] = 60 + 25*(len(Slotvar.slots)-18)


class Save_Load_Menue_Button():
    def __init__(self, text, pos):
        self.text = text
        self.pos = pos
        self.active_text_image = Slotvar.menue_button_font.render(self.text, True, Slotvar.active_menue_button_text_color)
        self.inactive_text_image = Slotvar.menue_button_font.render(self.text, True, Slotvar.inactive_menue_button_text_color)
        self.pressed_text_image = Slotvar.menue_button_font.render(self.text, True, Slotvar.pressed_menue_button_text_color)
        self.active = False
        self.pressed = False
        self.changing_status = ""





        
