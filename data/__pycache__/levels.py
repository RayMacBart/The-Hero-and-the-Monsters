import pygame
from pool import Var
import basic_types
import ork
import random


## set_main_background(BG_name)
## setup_Level_1()


def get_level():
    if Var.current_level == 1:
        setup_Level_1()
    elif Var.current_level == 2:
        setup_Level_2()
    elif Var.current_level == 3:
        setup_Level_3()
    Var.level_upset = True

def rise_level():
    Var.current_level += 1
    Var.level_upset = False
    Var.level_rising = False
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


def set_main_background(BG_name):
    Var.current_blitmaps.append(basic_types.Basic(BG_name, "", [0,0]))
    Var.current_blitmaps.append(basic_types.Basic(BG_name, "", [320,0]))
    Var.current_blitmaps.append(basic_types.Basic(BG_name, "", [0,200]))
    Var.current_blitmaps.append(basic_types.Basic(BG_name, "", [320,200]))
    Var.main_background = BG_name
##    Var.decorations[Var.IDG-1] = basic_types.Basic("Outer_Darkness", "", [0, 0])
##    Var.decorations[Var.IDG-1].image.set_colorkey([0,0,0], pygame.RLEACCEL)
##    Var.decorations[Var.IDG-1].image.set_alpha(20, pygame.RLEACCEL)
##    Var.decorations[Var.IDG-1] = basic_types.Basic("Middle_Darkness", "", [0, 0])
##    Var.decorations[Var.IDG-1].image.set_colorkey([0,0,0], pygame.RLEACCEL)
##    Var.decorations[Var.IDG-1].image.set_alpha(15, pygame.RLEACCEL)
##    Var.decorations[Var.IDG-1] = basic_types.Basic("Inner_Darkness", "", [94, 59])
##    Var.decorations[Var.IDG-1].image.set_colorkey([0,0,0], pygame.RLEACCEL)
##    Var.decorations[Var.IDG-1].image.set_alpha(10, pygame.RLEACCEL)
##    Var.decorations[Var.IDG-1] = basic_types.Basic("Near_Darkness", "", [161, 101])
##    Var.decorations[Var.IDG-1].image.set_colorkey([0,0,0], pygame.RLEACCEL)
##    Var.decorations[Var.IDG-1].image.set_alpha(5, pygame.RLEACCEL)

    
def setup_Level_1():
    set_main_background("Fog")
    msp = [95-320, 119-210]  # map-screen-pos!

    Var.borders[Var.IDG-1] = basic_types.Border("Wall_edge_UR", "Border", [0-msp[0], 0-msp[1]])
    Var.borders[Var.IDG-1] = basic_types.Border("Wall_OU", "Border", [0-msp[0], 100-msp[1]])
    Var.borders[Var.IDG-1] = basic_types.Border("Wall_OU", "Border", [0-msp[0], 200-msp[1]])
    Var.borders[Var.IDG-1] = basic_types.High_border("Wall_edge_OR", "High_border", [0-msp[0], 300-msp[1]])
    Var.borders[Var.IDG-1] = basic_types.Border("Wall_LR", "Border", [100-msp[0], 0-msp[1]])
    Var.borders[Var.IDG-1] = basic_types.Border("Wall_LR", "Border", [200-msp[0], 0-msp[1]])
    Var.borders[Var.IDG-1] = basic_types.Border("Wall_LR", "Border", [300-msp[0], 0-msp[1]])
    Var.borders[Var.IDG-1] = basic_types.Border("Wall_LR", "Border", [400-msp[0], 0-msp[1]])
    Var.borders[Var.IDG-1] = basic_types.Border("Wall_LR", "Border", [500-msp[0], 0-msp[1]])
    Var.borders[Var.IDG-1] = basic_types.Border("Wall_edge_UL", "Border", [600-msp[0], 0-msp[1]])
    Var.borders[Var.IDG-1] = basic_types.Border("Wall_+_W", "Border", [600-msp[0], 100-msp[1]])
    Var.doors[Var.IDG-1] = basic_types.Door("Door_OU", "Door", [600-msp[0], 200-msp[1]])
    Var.borders[Var.IDG-1] = basic_types.High_border("Wall_+_S", "High_border", [600-msp[0], 300-msp[1]])
    Var.borders[Var.IDG-1] = basic_types.High_border("Wall_LR", "High_border", [100-msp[0], 300-msp[1]])
    Var.borders[Var.IDG-1] = basic_types.High_border("Wall_LR", "High_border", [200-msp[0], 300-msp[1]])
    Var.borders[Var.IDG-1] = basic_types.High_border("Wall_LR", "High_border", [300-msp[0], 300-msp[1]])
    Var.borders[Var.IDG-1] = basic_types.High_border("Wall_LR", "High_border", [400-msp[0], 300-msp[1]])
    Var.borders[Var.IDG-1] = basic_types.High_border("Wall_LR", "High_border", [500-msp[0], 300-msp[1]])
    Var.borders[Var.IDG-1] = basic_types.Border("Wall_LR-UL", "Border", [700-msp[0], 100-msp[1]])
    Var.borders[Var.IDG-1] = basic_types.Border("Wall_OR-LR", "Border", [800-msp[0], 200-msp[1]])
    Var.borders[Var.IDG-1] = basic_types.Border("Wall_edge_OL", "Border", [1000-msp[0], 200-msp[1]])
    Var.borders[Var.IDG-1] = basic_types.Border("Wall_OU", "Border", [1000-msp[0], 100-msp[1]])
    Var.borders[Var.IDG-1] = basic_types.Border("Wall_edge_UR", "Border", [1000-msp[0], 0-msp[1]])
    Var.borders[Var.IDG-1] = basic_types.Border("Wall_edge_UL", "Border", [1100-msp[0], 0-msp[1]])
    Var.borders[Var.IDG-1] = basic_types.Border("Wall_OU", "Border", [1100-msp[0], 100-msp[1]])
    Var.borders[Var.IDG-1] = basic_types.Border("Wall_OU", "Border", [1100-msp[0], 200-msp[1]])
    Var.borders[Var.IDG-1] = basic_types.High_border("Wall_edge_OL", "High_border", [1100-msp[0], 300-msp[1]])
    Var.borders[Var.IDG-1] = basic_types.High_border("Wall_LR", "High_border", [700-msp[0], 300-msp[1]])
    Var.borders[Var.IDG-1] = basic_types.High_border("Wall_LR", "High_border", [800-msp[0], 300-msp[1]])
    Var.borders[Var.IDG-1] = basic_types.High_border("Wall_LR", "High_border", [900-msp[0], 300-msp[1]])
    Var.borders[Var.IDG-1] = basic_types.High_border("Wall_LR", "High_border", [1000-msp[0], 300-msp[1]])
    
    Var.grounds[Var.IDG-1] = basic_types.Basic("Meadow_edge_UR_NW", "Ground", [0-msp[0], 0-msp[1]])
    Var.grounds[Var.IDG-1] = basic_types.Basic("Meadow_LR_N", "Ground", [100-msp[0], 0-msp[1]])
    Var.grounds[Var.IDG-1] = basic_types.Basic("Meadow_LR_N", "Ground", [200-msp[0], 0-msp[1]])
    Var.grounds[Var.IDG-1] = basic_types.Basic("Meadow_LR_N", "Ground", [300-msp[0], 0-msp[1]])
    Var.grounds[Var.IDG-1] = basic_types.Basic("Meadow_LR_N", "Ground", [400-msp[0], 0-msp[1]])
    Var.grounds[Var.IDG-1] = basic_types.Basic("Meadow_LR_N", "Ground", [500-msp[0], 0-msp[1]])
    Var.grounds[Var.IDG-1] = basic_types.Basic("Meadow_edge_UL_NE", "Ground", [600-msp[0], 0-msp[1]])
    Var.grounds[Var.IDG-1] = basic_types.Basic("Meadow_OU_W", "Ground", [0-msp[0], 100-msp[1]])
    Var.grounds[Var.IDG-1] = basic_types.Basic("Meadow", "Ground", [100-msp[0], 100-msp[1]])
    Var.grounds[Var.IDG-1] = basic_types.Basic("Meadow", "Ground", [200-msp[0], 100-msp[1]])
    Var.grounds[Var.IDG-1] = basic_types.Basic("Meadow", "Ground", [300-msp[0], 100-msp[1]])
    Var.grounds[Var.IDG-1] = basic_types.Basic("Meadow", "Ground", [400-msp[0], 100-msp[1]])
    Var.grounds[Var.IDG-1] = basic_types.Basic("Meadow", "Ground", [500-msp[0], 100-msp[1]])
    Var.grounds[Var.IDG-1] = basic_types.Basic("Stone_LR_N", "Ground", [600-msp[0], 100-msp[1]]) # eigentlich edge, aber für Schönheit von Wiese überlagert
    Var.grounds[Var.IDG-1] = basic_types.Basic("Meadow_OU_E", "Ground", [600-msp[0], 100-msp[1]])
    Var.grounds[Var.IDG-1] = basic_types.Basic("Meadow_OU_W", "Ground", [0-msp[0], 200-msp[1]])
    Var.grounds[Var.IDG-1] = basic_types.Basic("Meadow", "Ground", [100-msp[0], 200-msp[1]])
    Var.grounds[Var.IDG-1] = basic_types.Basic("Meadow", "Ground", [200-msp[0], 200-msp[1]])
    Var.grounds[Var.IDG-1] = basic_types.Basic("Meadow", "Ground", [300-msp[0], 200-msp[1]])
    Var.grounds[Var.IDG-1] = basic_types.Basic("Meadow", "Ground", [400-msp[0], 200-msp[1]])
    Var.grounds[Var.IDG-1] = basic_types.Basic("Meadow", "Ground", [500-msp[0], 200-msp[1]])
    Var.grounds[Var.IDG-1] = basic_types.Basic("Meadow_OU_E", "Ground", [600-msp[0], 200-msp[1]])
    Var.grounds[Var.IDG-1] = basic_types.Basic("Meadow_edge_OR_SW", "Ground", [0-msp[0], 300-msp[1]])
    Var.grounds[Var.IDG-1] = basic_types.Basic("Meadow_LR_S", "Ground", [100-msp[0], 300-msp[1]])
    Var.grounds[Var.IDG-1] = basic_types.Basic("Meadow_LR_S", "Ground", [200-msp[0], 300-msp[1]])
    Var.grounds[Var.IDG-1] = basic_types.Basic("Meadow_LR_S", "Ground", [300-msp[0], 300-msp[1]])
    Var.grounds[Var.IDG-1] = basic_types.Basic("Meadow_LR_S", "Ground", [400-msp[0], 300-msp[1]])
    Var.grounds[Var.IDG-1] = basic_types.Basic("Meadow_LR_S", "Ground", [500-msp[0], 300-msp[1]])
    Var.grounds[Var.IDG-1] = basic_types.Basic("Meadow_edge_OL_SE", "Ground", [600-msp[0], 300-msp[1]])
    Var.grounds[Var.IDG-1] = basic_types.Basic("Stone_LR-UL_NE", "Ground", [700-msp[0], 100-msp[1]])
    Var.grounds[Var.IDG-1] = basic_types.Basic("Stone_OU_W", "Ground", [600-msp[0], 200-msp[1]])
    Var.grounds[Var.IDG-1] = basic_types.Basic("Stone", "Ground", [700-msp[0], 200-msp[1]])
    Var.grounds[Var.IDG-1] = basic_types.Basic("Stone_OR-LR_NE", "Ground", [800-msp[0], 200-msp[1]])
    Var.grounds[Var.IDG-1] = basic_types.Basic("Stone_edge_OR_SW", "Ground", [600-msp[0], 300-msp[1]])
    Var.grounds[Var.IDG-1] = basic_types.Basic("Stone_LR_S", "Ground", [700-msp[0], 300-msp[1]])
    Var.grounds[Var.IDG-1] = basic_types.Basic("Stone_LR_S", "Ground", [800-msp[0], 300-msp[1]])
    Var.grounds[Var.IDG-1] = basic_types.Basic("Stone_LR_S", "Ground", [900-msp[0], 300-msp[1]])
    Var.grounds[Var.IDG-1] = basic_types.Basic("Parquet_edge_UR_NW", "Ground", [1000-msp[0], 0-msp[1]])
    Var.grounds[Var.IDG-1] = basic_types.Basic("Parquet_edge_UL_NE", "Ground", [1100-msp[0], 0-msp[1]])
    Var.grounds[Var.IDG-1] = basic_types.Basic("Parquet_OU_W", "Ground", [1000-msp[0], 100-msp[1]])
    Var.grounds[Var.IDG-1] = basic_types.Basic("Parquet_OU_E", "Ground", [1100-msp[0], 100-msp[1]])
    Var.grounds[Var.IDG-1] = basic_types.Basic("Parquet_edge_OL_NW", "Ground", [1000-msp[0], 200-msp[1]])
    Var.grounds[Var.IDG-1] = basic_types.Basic("Parquet_OU_E", "Ground", [1100-msp[0], 200-msp[1]])
    Var.grounds[Var.IDG-1] = basic_types.Basic("Parquet_LR_S", "Ground", [1000-msp[0], 300-msp[1]])
    Var.grounds[Var.IDG-1] = basic_types.Basic("Parquet_edge_OL_SE", "Ground", [1100-msp[0], 300-msp[1]])

    Var.units[Var.IDG-1] = ork.Ork("Ork", "Monster", [610-145-msp[0], 277-126-msp[1]])
    Var.animated_obstacles[Var.IDG-1] = basic_types.Animated_obstacle("Tree", "Animated_obstacle", [128-msp[0],0-msp[1]], [106,178], 4, 850, True)
    Var.animated_decorations[Var.IDG-1] = basic_types.Animated_Notmasked("Walltorch_NE", "Animated_Decoration", [808-msp[0], 166-msp[1]], 5, 120, True)
    Var.animated_overlays[Var.IDG-1] = basic_types.Animated_Notmasked("Fireshine", "Animated_Overlay", [808-110-msp[0], 166-20-msp[1]], 8, 160, True, 10)
    Var.animated_decorations[Var.IDG-1] = basic_types.Animated_Notmasked("Walltorch_NE", "Animated_Decoration", [827-msp[0], 184-msp[1]], 5, 120, True)
    Var.animated_overlays[Var.IDG-1] = basic_types.Animated_Notmasked("Fireshine", "Animated_Overlay", [827-110-msp[0], 184-20-msp[1]], 8, 160, True, 10)
    Var.animated_decorations[Var.IDG-1] = basic_types.Animated_Notmasked("Walltorch_NE", "Animated_Decoration", [847-msp[0], 202-msp[1]], 5, 120, True)
    Var.animated_overlays[Var.IDG-1] = basic_types.Animated_Notmasked("Fireshine", "Animated_Overlay", [847-110-msp[0], 202-20-msp[1]], 8, 160, True, 10)
    Var.decorations[Var.IDG-1] = basic_types.Basic("Wallhole_N", "Decoration", [1077-msp[0], 35-msp[1]])
    
    
    
    
    
    



    
