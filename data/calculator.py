import pygame
from pool import Var
from pool import Frames
# from pool import Count
import figure_functions
import fightpic_functions
import other_functions
import cursors
import levels
import fight


## calculate()
				

def calculate():
    
    if Var.level_rising:
        levels.rise_level()
        
    if not Var.level_upset:
        levels.get_level()

    levels.check_level_progress()

    Var.frames_since_last_click += 1

    # CURSOR/GEHPUNKT
    if not Var.hero.dead:
        cursors.check_cursor()
        if Var.go_point["active"] or Var.go_point["start"]:
            other_functions.go_point_animation()
    else:
        pygame.mouse.set_visible(False) 
    # MARKER
    other_functions.handle_marker_animation()

    # ANIMATIONEN (NON CHARACTER)
    for abg in Var.animated_backgrounds.values():
        other_functions.check_current_animation_pic(abg)
    for ad in Var.animated_decorations.values():
        other_functions.check_current_animation_pic(ad)
    for aov in Var.animated_overlays.values():
        other_functions.check_current_animation_pic(aov)
    for ao in Var.animated_obstacles.values():
        other_functions.check_current_animation_pic(ao)
        
    if Var.start_redframe or Frames.redframing:
        other_functions.redframe()

    # DOORS
    for d in Var.doors.values():
        if d.in_focus:        #kontrolliert, ob Hero mit Vorhaben, das Tor zu betätigen, in Auslöserbereich (Triggerbereich) kommt
            d.check_triggering() #
        if d.status == 'opening':   #betrifft Animation
            d.open()                #
        elif d.status == 'closing': #
            d.close()               

    if not Var.hero.dead:
        if not Var.hero.fighting:
            # HERO - GEHABSICHT
            if Var.hero.go:
                figure_functions.detect_borders(Var.hero)
                if not Var.hero.attention:
                    figure_functions.handle_direction(Var.hero)
                figure_functions.handle_walk_animation(Var.hero)
                if not Var.hero.movement_skip_countdown:   # Verzögerer
                    Var.hero.movement_skip_countdown = Var.hero.movement_skip_at_frame
                else:
                    Var.hero.movement_skip_countdown -= 1
                    figure_functions.handle_movement_purpose(Var.hero)
                    figure_functions.handle_collision(Var.hero)
                    figure_functions.execute_movement(Var.hero)

            if Var.hero.draw_pressed:  # draw/put away (auch nur beim Nicht-Kämpfen möglich)
                fightpic_functions.draw_button(Var.hero)
            if Var.hero.drawing:
                fightpic_functions.draw(Var.hero)
            elif Var.hero.putting_away:
                fightpic_functions.put_away(Var.hero)
        
        # HERO ATTENTION & FOCUS
        Var.hero.check_attention()
        if Var.hero.attention:
            Var.hero.focus()
        
            
        #  GENERAL FIGHTING
        if Var.hero.fighting:
            Var.fight.automatic_align_opponents()
            Var.fight.handle_knockback()
            figure_functions.handle_collision(Var.hero)
            for e in Var.fight.enemies:
                figure_functions.handle_collision(e)
            Var.fight.handle_the_battle()
            figure_functions.execute_movement(Var.hero)
            for e in Var.fight.enemies:
                figure_functions.execute_movement(e)
            if Var.screen_scrolling_happened:
                figure_functions.detect_borders(Var.hero)
                for e in Var.fight.enemies:
                    figure_functions.detect_borders(e)
                                                               

            ###  HERO BATTLE CALCULATOR  ###
            if Var.hero.blocking:
                fightpic_functions.block(Var.hero)
            elif Var.hero.start_blocking:
                fightpic_functions.block(Var.hero)
            
            elif Var.hero.release_defending:
                fightpic_functions.release_defend(Var.hero)
            elif Var.hero.defending:
                fightpic_functions.defend(Var.hero)
            elif Var.hero.defblocking:
                fightpic_functions.defblock(Var.hero)
            elif Var.hero.attacking:
                fightpic_functions.attack(Var.hero)
            elif Var.hero.start_release_defending:
                fightpic_functions.defend_button(Var.hero)
            elif Var.hero.start_defending:
                fightpic_functions.defend_button(Var.hero)
            elif Var.hero.start_defblocking:
                fightpic_functions.defblock(Var.hero)
            elif Var.hero.start_attack:
                fightpic_functions.attack(Var.hero)
    
    if Var.hero.start_being_hitted:
        fightpic_functions.hit(Var.hero)
    elif Var.hero.being_hitted:
        fightpic_functions.hit(Var.hero)
    elif Var.hero.start_dying or Var.hero.dying:   # so "detended" kann auch außerhalb des Nahkampfes gestorben werden.
        fightpic_functions.die(Var.hero)           # (könnte für Hit auch noch interessant/besser werden wegen z.B. Pfeile?)
        Frames.redframing = "grow"
     
                

    # ENEMY 
    for u in Var.blitlist:
        if u in Var.units.values():
            
            if not u.dead:
                # - GEHABSICHT
                if u.go:
                    figure_functions.detect_borders(u)
                    figure_functions.handle_direction(u)
                    figure_functions.handle_walk_animation(u)
                    if not u.movement_skip_countdown:
                        u.movement_skip_countdown = u.movement_skip_at_frame
                    else:
                        u.movement_skip_countdown -= 1
                        figure_functions.handle_movement_purpose(u)
                        figure_functions.handle_collision(u)
                        figure_functions.execute_movement(u)
                u.check_attention()
                u.behavior()
                if u.draw_pressed:    # Units DRAW/PUT AWAY
                    fightpic_functions.draw_button(u)   #
                if u.drawing:         #
                    fightpic_functions.draw(u)          #
                elif u.putting_away:  #
                    fightpic_functions.put_away(u)      #

                ###  ENEMY BATTLE CALCULATOR  ###
                if u.fighting:
                    if u.start_attack or u.attacking:
                        fightpic_functions.attack(u)
                    elif u.start_defending or u.start_release_defending:
                        fightpic_functions.defend_button(u)
                    elif u.defending:
                        fightpic_functions.defend(u)
                    elif u.release_defending:
                        fightpic_functions.release_defend(u)
                    elif u.start_blocking or u.blocking:
                        fightpic_functions.block(u)
                    elif u.start_defblocking or u.defblocking:
                        fightpic_functions.defblock(u)
            if u.start_being_hitted or u.being_hitted:
                fightpic_functions.hit(u)
            elif u.start_dying or u.dying:
                fightpic_functions.die(u)

    if (Var.hero.hitpoints <= 0) and not (Var.hero.dead or Var.hero.start_dying or Var.hero.start_being_hitted or Var.hero.being_hitted):
        Var.hero.start_dying = True
    for u in Var.units.values():
        if (u.hitpoints <= 0) and not (u.dead or u.start_dying):
            #or u.start_being_hitted or u.being_hitted):
            #print(str(pygame.time.get_ticks())+":", "Enemy real start_dying - call @ Calculator.")
            u.start_dying = True
            if u in Var.hero.other_blitted_masktypes:
                Var.hero.other_blitted_masktypes.remove(u)
        elif (u.hitpoints <= 0) and u.dead and (u.die_CPN >= 25):
            Var.blitlist.remove(u)

                
    if Var.hero.fighting and not Var.fight.enemies:
        Var.hero.fighting = False
        Var.fight = None

    if Var.dead:
        other_functions.check_dead()
            
##    Count.testduration = pygame.time.get_ticks() - Count.testlasttime
##    if Count.testduration >= 500:
##        Count.testduration = 0
##        Count.testlasttime = pygame.time.get_ticks()

        
