"""
    Eduardo Rodríguez Sánchez 
    29/12/2020
    All assets
"""
import pygame

window_width, window_height = 1200, 700
window_size = window_width, window_height
screen = pygame.display.set_mode(window_size)
# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # -> Fullscreen mode
# Nothing will be resized correctly
# screen = pygame.display.set_mode(window_size, RESIZABLE)  # -> Resizable mode

pygame.mouse.set_visible(False)

background = pygame.image.load("assets/images/background_floor.png")

# Clock
main_clock = pygame.time.Clock()

# Upper left corner game icon
game_icon = pygame.image.load("assets/images/game_icon.png").convert_alpha()
pygame.display.set_icon(game_icon)
pygame.display.set_caption("Pool!")


def resize_cue(image):
    ratio = (screen.get_size()[1] - 120) / image.get_size()[1]
    widht = ratio * image.get_size()[0]
    height = ratio * image.get_size()[1]
    resized_image = pygame.transform.scale(
        image,
        (
            int(widht),
            int(height),
        ),
    ).convert_alpha()
    return resized_image


# All cue skins
dragon_cue = pygame.image.load("assets/images/dragon_long_cue.png").convert_alpha()
dragon_cue_display = pygame.image.load("assets/images/dragon_long_cue_display.png")
dragon_cue_display = resize_cue(dragon_cue_display)


# Sets up colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
green_cyan = (32, 52, 40)
brown_wood = (133, 94, 66)
redish_brown = (87, 25, 25)
olimpic_green = (54, 89, 74)
ball_yellow = (248, 205, 1)
ball_blue = (1, 45, 182)
ball_red = (254, 61, 9)
ball_purple = (76, 1, 115)
ball_orange = (253, 179, 43)
ball_green = (1, 115, 53)
ball_maroon = (147, 31, 1)