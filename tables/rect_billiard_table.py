"""
    Eduardo Rodríguez Sánchez 
    23/12/2020
    Rectangular Billiard Table
"""
import pygame, sys
from assets.display import *


class BilliardTable:
    """Pool table where the game takes place"""

    def __init__(self):
        self.__resize()
        self.friction = 0.02

    def draw(self):
        """Draws the pool table:
        - Surface
        - Holes
        - Frames"""

        # Inner frame
        pygame.draw.rect(
            screen,
            green_cyan,
            [
                self.top_left_corner[0],
                self.top_left_corner[1],
                self.width,
                self.height,
            ],
        )

        # Outer frame
        frame_thickness = 10
        pygame.draw.rect(
            screen,
            redish_brown,
            [
                self.top_left_corner[0] - 2 * frame_thickness,
                self.top_left_corner[1] - 2 * frame_thickness,
                self.width + 4 * frame_thickness,
                self.height + 4 * frame_thickness,
            ],
            frame_thickness,
            border_radius=3,
        )

        # Surface of the table
        pygame.draw.rect(
            screen,
            olimpic_green,
            [
                self.top_left_corner[0] - frame_thickness,
                self.top_left_corner[1] - frame_thickness,
                self.width + 2 * frame_thickness,
                self.height + 2 * frame_thickness,
            ],
            frame_thickness,
            border_radius=3,
        )

        self.holes = self.__set_holes()
        self.__draw_holes()

    def __draw_holes(self):
        for hole in self.holes:
            hole.draw()

    def __resize(self):
        """Places the pool table on the center of the window and
        resizes depending on the windows width and height."""
        table_scale = 0.5
        window_width = pygame.display.get_surface().get_size()[0]
        window_height = pygame.display.get_surface().get_size()[1]
        self.width = window_width * table_scale
        self.height = window_height * table_scale

        self.top_left_corner = [
            (window_width - self.width) / 2,
            (window_height - self.height) / 2,
        ]

    def __set_holes(self) -> list:
        """Returns a list whit a number of Hole objects"""
        holes = []
        hole_radius = 16
        first_row = self.top_left_corner[1]
        second_row = self.top_left_corner[1] + self.height
        for x in range(
            int(self.top_left_corner[0]),
            int(self.top_left_corner[0]) + int(self.width) + 1,
            int(self.width / 2),
        ):
            # First row of holes
            holes.append(Hole(x, first_row, hole_radius))
            # Second row of holes
            holes.append(Hole(x, second_row, hole_radius))

        return holes


class Hole:
    def __init__(self, x_pos, y_pos, radius):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.radius = radius

    def draw(self):
        coord = self.x_pos, self.y_pos
        pygame.draw.circle(screen, black, coord, self.radius)