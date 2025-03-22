import pygame
from pool import Var


## check_cursor()
## set_cursors()


def check_cursor():
    if Var.action_cursor["start"] or Var.action_cursor["active"]:
        if Var.action_cursor["start"]:
            Var.action_cursor["active"] = True
            Var.action_cursor["CPN"] = 0
            Var.action_cursor["LPT"] = pygame.time.get_ticks()-Var.action_cursor["TPP"]
            Var.action_cursor["start"] = False
        if Var.action_cursor["active"]:
            if Var.action_cursor["LPT"] + Var.action_cursor["TPP"] < pygame.time.get_ticks():
                Var.action_cursor["LPT"] = pygame.time.get_ticks()
                Var.action_cursor["CPN"] += 1
                if Var.action_cursor["CPN"] <= 4:
                    if Var.action_cursor["cursor"] == "open_door":
                        if Var.action_cursor["CPN"] in [1,3]:
                            pygame.mouse.set_cursor((24,16), (0,0), Var.hl_open_door_cursor[0], Var.hl_open_door_cursor[1])
                        elif Var.action_cursor["CPN"] in [2,4]:
                            pygame.mouse.set_cursor((24,16), (0,0), Var.open_door_cursor[0], Var.open_door_cursor[1])
                    elif Var.action_cursor["cursor"] == "close_door":
                        if Var.action_cursor["CPN"] in [1,3]:
                            pygame.mouse.set_cursor((16,16), (0,0), Var.hl_close_door_cursor[0], Var.hl_close_door_cursor[1])
                        elif Var.action_cursor["CPN"] in [2,4]:
                            pygame.mouse.set_cursor((16,16), (0,0), Var.close_door_cursor[0], Var.close_door_cursor[1])
                else:
                    Var.action_cursor["active"] = False
                    Var.action_cursor["cursor"] = None
                    
    else:
        curpos = pygame.mouse.get_pos()
        Var.cursor_feels = False
        curpress = 0
        for p in pygame.mouse.get_pressed():
            if p:
                curpress += 1
        for do in Var.doors.values():
            if do in Var.blitlist:
                try:
                    if do.click_mask.get_at([curpos[0]-do.pos[0], curpos[1]-do.pos[1]]):
                        Var.cursor_feels = True
                        if do.status in ["open", "opening"]:
                            if not do.in_focus:
                                pygame.mouse.set_cursor((16,16), (0,0), Var.close_door_cursor[0], Var.close_door_cursor[1])
                            else:
                                pygame.mouse.set_cursor((16,16), (0,0), Var.hl_close_door_cursor[0], Var.hl_close_door_cursor[1])
                        else:
                            if not do.in_focus:
                                pygame.mouse.set_cursor((24,16), (0,0), Var.open_door_cursor[0], Var.open_door_cursor[1])
                            else:
                                pygame.mouse.set_cursor((24,16), (0,0), Var.hl_open_door_cursor[0], Var.hl_open_door_cursor[1])
                except IndexError:
                    pass

        for u in Var.units.values():
            if u in Var.blitlist:
                if u.typ == "Monster":
                    try:
                        if u.click_mask.get_at([curpos[0]-u.pos[0], curpos[1]-u.pos[1]]):
                            Var.cursor_feels = True
                            if (pygame.time.get_ticks() > Var.last_fightclick+300):
                                pygame.mouse.set_cursor((32,24), (0,0), Var.fight_cursor[0], Var.fight_cursor[1])
                            else:
                                pygame.mouse.set_cursor((32,24), (0,0), Var.hl_fight_cursor[0], Var.hl_fight_cursor[1])
                    except IndexError:
                        pass
                
        if not Var.cursor_feels:
            if not curpress:
                pygame.mouse.set_cursor((8,8), (0,0), Var.standard_cursor[0], Var.standard_cursor[1])
            else:
                pygame.mouse.set_cursor((8,8), (0,0), Var.hl_standard_cursor[0], Var.hl_standard_cursor[1])

def set_cursors():
    scs = (
        "X       ",
        "XX      ",
        "XoX     ",
        "X..X    ",
        "X...X   ",
        "X.Xo.X  ",
        "XoXXooX ",
        "XoXoXooX")
    Var.standard_cursor = pygame.cursors.compile(scs)
    pygame.mouse.set_cursor((8,8), (0,0), Var.standard_cursor[0], Var.standard_cursor[1])
    
    scas = (
        "o       ",
        "oo      ",
        "o.o     ",
        "o..o    ",
        "o...o   ",
        "o....o  ",
        "o.....o ",
        "o.o.o..o")
    Var.hl_standard_cursor = pygame.cursors.compile(scas)
    
    odcs = (
        "  ...                   ",
        " .XXX.                  ",
        "..XXXX.                 ",
        ".XXXXXX.                ",
        " ...XXXX.               ",
        "  .XXXXXX.              ",
        "   ...XXXX.             ",
        "      .XXXX.....        ",
        "      ..XXXXXXXX..      ",
        "      .XXX....XXXX.     ",
        "     .XXX..  ...XXX.    ",
        "     .XXX..   ..XXX.    ",
        "     ..XXX.....XXX..    ",
        "      ..XXXXXXXXX..     ",
        "       ..XXXXXX...      ",
        "        ........        ")
    Var.open_door_cursor = pygame.cursors.compile(odcs)

    odcas = (
        "  ooo                   ",
        " o...o                  ",
        "oo....o                 ",
        "o......o                ",
        " ooo....o               ",
        "  o......o              ",
        "   ooo....o             ",
        "      o....ooooo        ",
        "      oo........oo      ",
        "      o...oooo....o     ",
        "     o...oo  ooo...o    ",
        "     o...oo   oo...o    ",
        "     oo...ooooo...oo    ",
        "      oo.........oo     ",
        "       oo......ooo      ",
        "        oooooooo        ")
    Var.hl_open_door_cursor = pygame.cursors.compile(odcas)

    fcs = (
        ".                               ",
        ".X.                             ",
        " .X .                           ",
        "  .XX.                          ",
        "   .XX.                         ",
        "    .XX .                       ",
        "     .XXX.                      ",
        "      .XXX.                     ",
        "       .XXX.                    ",
        "        .XXX .                  ", 
        "         .XXXX.                 ",
        "          .XX.X.                ",
        "           .XX.X.               ",
        "            .XX.XX.             ",
        "             .XX..X.   .        ",
        "              .XX..X. .X.       ",
        "               .XXXXX..X.       ",
        "            ..........XX.       ",
        "           .XXXXXXXXXX...       ",
        "            ..........XX.       ",
        "                    .XXXX.      ",
        "                     .XXXX.     ",
        "                      .XXX.     ",
        "                       ...      ")
    Var.fight_cursor = pygame.cursors.compile(fcs)

    fcas = (
        "oo                              ",
        "o.o                             ",
        " o.oo                           ",
        "  o..o                          ",
        "   o..o                         ",
        "    o..oo                       ",
        "     o...o                      ",
        "      o...o                     ",
        "       o...o                    ",
        "        o...oo                  ", 
        "         o....o                 ",
        "          o..o.o                ",
        "           o..o.oo              ",
        "            o..o..o             ",
        "             o..oo.o   o        ",
        "              o..oo.o o.o       ",
        "               o.....oo.o       ",
        "            oooooooooo..o       ",
        "           o..........ooo       ",
        "            oooooooooo..o       ",
        "                    o....o      ",
        "                     o....o     ",
        "                      o...o     ",
        "                       ooo      ")
    Var.hl_fight_cursor = pygame.cursors.compile(fcas)

    cdcs = (
        ".....           ",
        ".XX.   .....    ",
        ".X.   .XXXXX.   ",
        "..   .X.....X.  ",
        ".   .X.     .X. ",
        "    .X.     .X. ",
        "    .X.     .X. ",
        "    .X.     .X. ",
        "   .............",
        "   .XXXXXXXXXXX.",
        "   .XXXXXXXXXXX.",
        "   .XXXXX.XXXXX.",
        "   .XXXXX.XXXXX.",
        "   .XXXXXXXXXXX.",
        "   .XXXXXXXXXXX.",
        "   .............")
    Var.close_door_cursor = pygame.cursors.compile(cdcs)

    cdcas = (
        "ooooo           ",
        "o..o   ooooo    ",
        "o.o   o.....o   ",
        "oo   o.ooooo.o  ",
        "o   o.o     o.o ",
        "    o.o     o.o ",
        "    o.o     o.o ",
        "    o.o     o.o ",
        "   ooooooooooooo",
        "   o...........o",
        "   o...........o",
        "   o.....o.....o",
        "   o.....o.....o",
        "   o...........o",
        "   o...........o",
        "   ooooooooooooo")
    Var.hl_close_door_cursor = pygame.cursors.compile(cdcas)
    
    nocs = (
        " X            X ",
        "X.X          X.X",
        " X.X        X.X ",
        "  X.X      X.X  ",
        "   X.X    X.X   ",
        "    X.X  X.X    ",
        "     X.XX.X     ",
        "      X..X      ",
        "      X..X      ",
        "     X.XX.X     ",
        "    X.X  X.X    ",
        "   X.X    X.X   ",
        "  X.X      X.X  ",
        " X.X        X.X ",
        "X.X          X.X",
        " X            X ")
    Var.no_cursor = pygame.cursors.compile(nocs)

    nocas = (
        " .            . ",
        ".o.          .o.",
        " .o.        .o. ",
        "  .o.      .o.  ",
        "   .o.    .o.   ",
        "    .o.  .o.    ",
        "     .o..o.     ",
        "      .oo.      ",
        "      .oo.      ",
        "     .o..o.     ",
        "    .o.  .o.    ",
        "   .o.    .o.   ",
        "  .o.      .o.  ",
        " .o.        .o. ",
        ".o.          .o.",
        " .            . ")
    Var.hl_no_cursor = pygame.cursors.compile(nocas)
