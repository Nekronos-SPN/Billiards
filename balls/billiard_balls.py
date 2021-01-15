"""
    Eduardo Rodríguez Sánchez 
    28/12/2020
    Ingame Balls
"""
import pygame
from assets.display import *
from abc import ABC, abstractmethod
from math import sqrt, dist, acos, pi
from random import randint, choice
from cues.billiard_cues import Cue


class BilliardBall(ABC):
    def __init__(self, table, position, number=None):
        self.table = table

        self.radius = 14.5
        self.identifier = number
        self.color = eval(self.__color_picker())

        self.velocity = 0
        self.direction = [0, 0]

        self.x_pos = self.table.top_left_corner[0] + position[0]
        self.y_pos = self.table.top_left_corner[1] + position[1]
        # self.__x_ratio = self.x_pos / self.table.width
        # self.__y_ratio = self.y_pos / self.table.height

    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction):
        if type(direction) == list or type(direction) == tuple:
            # Direction gets normalized
            norm = sqrt(sum([i ** 2 for i in direction]))
            if norm != 0:
                normalized_dir = map(lambda i: i / norm, direction)
                self.__direction = list(normalized_dir)
            else:
                self.__direction = [0, 0]
        else:
            self.__direction = [0, 0]

    @property
    def velocity(self) -> float:
        return self.__velocity

    @velocity.setter
    def velocity(self, velocity):
        if velocity <= 0:
            self.__velocity = 0
        elif velocity > 10:
            self.__velocity = 20
        else:
            self.__velocity = velocity

    @property
    def identifier(self) -> int:
        return self.__identifier

    @identifier.setter
    def identifier(self, number):
        if type(number) != int or number < 1 or number > 15:
            self.__identifier = None
        else:
            self.__identifier = number

    @property
    def x_pos(self) -> float:
        return self.__x_pos

    @x_pos.setter
    def x_pos(self, x_pos):
        if x_pos - self.radius <= self.table.top_left_corner[0]:
            self.__x_pos = self.table.top_left_corner[0] + self.radius
            self.direction[0] = (
                self.direction[0] * -1
            )  # Direction is changed conservating the angle
        elif x_pos + self.radius >= self.table.top_left_corner[0] + self.table.width:
            self.__x_pos = (
                self.table.top_left_corner[0] + self.table.width - self.radius
            )
            self.direction[0] = self.direction[0] * -1
        else:
            self.__x_pos = x_pos

    @property
    def y_pos(self) -> float:
        return self.__y_pos

    @y_pos.setter
    def y_pos(self, y_pos):
        if y_pos - self.radius <= self.table.top_left_corner[1]:
            self.__y_pos = self.table.top_left_corner[1] + self.radius
            self.direction[1] = self.direction[1] * -1
        elif y_pos + self.radius >= self.table.top_left_corner[1] + self.table.height:
            self.__y_pos = (
                self.table.top_left_corner[1] + self.table.height - self.radius
            )
            self.direction[1] = self.direction[1] * -1
        else:
            self.__y_pos = y_pos

    @abstractmethod
    def draw(self):
        # self.__reposition()

        self.__movement()

        pygame.draw.circle(
            screen,
            self.color,
            [self.x_pos, self.y_pos],
            self.radius,
        )

        pygame.draw.circle(
            screen,
            white,
            [self.x_pos, self.y_pos],
            self.radius * 2 / 3,
        )

        # Number will not be drawn if it is not inputted
        if type(self.identifier) == int:
            freesansbold = pygame.font.Font("freesansbold.ttf", int(self.radius - 3))
            number = freesansbold.render(f"{self.identifier}", True, black)
            screen.blit(
                number,
                (
                    self.x_pos - number.get_rect().width / 2,
                    self.y_pos - number.get_rect().height / 2,
                ),
            )

    def __movement(self):
        self.x_pos += self.velocity * self.direction[0]
        self.y_pos += self.velocity * self.direction[1]
        self.velocity -= self.table.friction

    def __color_picker(self) -> str:
        """Returns the color of the ball depending on its number.
        If no number is inputted white will be chosen."""
        colors = {
            "ball_yellow": (1, 9),
            "ball_blue": (2, 10),
            "ball_red": (3, 11),
            "ball_purple": (4, 12),
            "ball_orange": (5, 13),
            "ball_green": (6, 14),
            "ball_maroon": (7, 15),
            "black": (8,),
        }
        for color, numbers in colors.items():
            if self.identifier in numbers:
                return color
        else:
            return "white"

    # def __reposition(self):
    #     """Repositions the ball depending on the table width and height."""
    #     self.x_pos = self.__x_ratio * self.table.width
    #     self.y_pos = self.__y_ratio * self.table.height


class PlayerBall(BilliardBall):
    """The ball that the player will use throughout the game."""

    def __init__(self, table, position):
        super().__init__(table, position)
        self.cue = Cue(self, dragon_cue)

    def draw(self):
        super().draw()
        if self.velocity == 0:
            self.cue.draw(screen)


class Solids(BilliardBall):
    """Solid balls"""

    def draw(self):
        super().draw()


class Stripes(BilliardBall):
    """Striped balls"""

    def draw(self):
        super().draw()