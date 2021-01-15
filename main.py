"""
    Eduardo Rodríguez Sánchez 
    23/12/2020
    Main Program
"""

import pygame, sys
from assets.display import *
from tables.rect_billiard_table import BilliardTable
from balls.billiard_balls import PlayerBall, Solids, Stripes
from balls.ball_setter_8_game import set_balls
from balls.ball_collision import check_collision

################ Main Program ################
def draw_update():
    screen.blit(background, (0, 0))
    screen.blit(dragon_cue_display, (30, 50))

    main_table.draw()

    for solid in game_balls[0]:
        solid.draw()
    for striped in game_balls[1]:
        striped.draw()

    user_ball.draw()

    # Frames per second
    freesansbold = pygame.font.Font("freesansbold.ttf", 50)
    fps = freesansbold.render(str(int(main_clock.get_fps())), True, red)
    screen.blit(fps, (10, 10))

    pygame.display.flip()  # Updates contents in the display


def physics():
    check_collision(user_ball, game_balls)


def main_loop():
    mainLoop = True
    while mainLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        physics()
        draw_update()
        main_clock.tick(60)


# Pygame initializes
pygame.init()

# Table is created
main_table = BilliardTable()

# Balls are created
user_ball = PlayerBall(main_table, [70, main_table.height / 2])
user_ball.velocity = 10
user_ball.direction = [1, 0]
game_balls = set_balls(main_table, user_ball, Solids, Stripes)

# Game starts
main_loop()
