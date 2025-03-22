import pygame
import pool
from pool import Var
from pool import Channels
import eventlooper
import calculator
import drawer
import blaster
import hero
import basic_types
import menuehandler
import pickle
import cursors


## rootfunction()


def rootfunction():
    pygame.display.init()
    pygame.mixer.init(frequency=48000, size=-16, channels=2, buffer=2048)
    pygame.key.set_repeat(332,17)

    cursors.set_cursors()
    for i in range(8):
        Var.go_point["images"][i+1] = pygame.image.load(Var.path+"\\pics\\Go-point\\Go-point_"+str(i+1)+".png").convert()
        Var.go_point["images"][i+1].set_colorkey([0,0,0], pygame.RLEACCEL)
        Var.go_point["images"][i+1].set_alpha(128-(i*8), pygame.RLEACCEL)
    try:
        file = open("ID_Count.txt", "rb")
        Var.IDG = pickle.load(file)
        file.close()
    except:
        print("ERROR: Could not continue ID-Count when starting!")

    Var.hero = hero.Hero("Hero", "Hero", [175, 100])  # Mitte bei screen: 640x400, Bild: 290x200
    Var.blitlist.append(Var.hero)

    drawer.check_layer_adjust()

    pygame.mixer.set_reserved(4)  # die Hälfte der Channels sind somit "sicher"
                                  # vor pygame.mixer.find_channel(), welches Channels/Sounds zu
                                  # sogar zu unterbrechen vermag.
    Channels.background_music.play(Var.current_music)
    Channels.background_music.pause()

    framecounter = 0
    print("Hero's ID:", Var.hero.ID, sep=" ")

    Var.canvas_marker.set_colorkey([0,0,0], pygame.RLEACCEL)
    
    while not Var.done:

        if not Var.menue:
            eventlooper.eventloop()
            calculator.calculate()
            drawer.draw()
            blaster.blast()  # blast() betrifft nur über längere Zeit gehende mehrfache Sound-Loops (z.B. Musik)
        else:
            menuehandler.handle_menue()

        
        framecounter += 1
        if framecounter % 150 == 0:
            pass
                

        
        Var.clock.tick(50)
        pygame.time.wait(5)

    file = open("ID_Count.txt", "wb")
    pickle.dump(Var.IDG, file)
    file.close()
    
    pygame.display.quit()

