"""
    Eduardo Rodríguez Sánchez 
    13/01/2021
    Cues
"""
from math import dist, acos, asin, pi
import pygame


class Cue:
    """Cue that the player will be able to choose"""

    def __init__(self, ball, cue_skin, screen):
        self.x_pos, self.y_pos = ball.x_pos, ball.y_pos
        self.att_ball = ball
        self.skin = self.__resize(cue_skin, screen)
        self.angle = 0

    def __calc_pos(self, ball):
        """Transform the given angle to a point of a circumference"""

        sep = 2
        # Contiguous cathetus / hypotenuse
        cosine = dist(
            [ball.x_pos, ball.y_pos],
            [pygame.mouse.get_pos()[0], ball.y_pos],
        ) / dist(
            [ball.x_pos, ball.y_pos],
            [pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]],
        )
        # Opposite cathetus / hypotenuse
        sine = dist(
            [ball.x_pos, ball.y_pos],
            [ball.x_pos, pygame.mouse.get_pos()[1]],
        ) / dist(
            [ball.x_pos, ball.y_pos],
            [pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]],
        )

        if (
            pygame.mouse.get_pos()[0] < ball.x_pos
            and pygame.mouse.get_pos()[1] < ball.y_pos
        ):
            cue_x = -cosine * (ball.radius + sep) + ball.x_pos
            cue_y = -sine * (ball.radius + sep) + ball.y_pos
            self.angle = -acos(cosine) * 180 / pi - 90
        elif pygame.mouse.get_pos()[0] < ball.x_pos:
            cue_x = -cosine * (ball.radius + sep) + ball.x_pos
            cue_y = sine * (ball.radius + sep) + ball.y_pos
            self.angle = -acos(sine) * 180 / pi

        elif pygame.mouse.get_pos()[1] < ball.y_pos:
            cue_x = cosine * (ball.radius + sep) + ball.x_pos
            cue_y = -sine * (ball.radius + sep) + ball.y_pos
            self.angle = acos(cosine) * 180 / pi + 90

        else:
            cue_x = cosine * (ball.radius + sep) + ball.x_pos + 2
            cue_y = sine * (ball.radius + sep) + ball.y_pos + 2
            self.angle = acos(sine) * 180 / pi
        return cue_x, cue_y

    def draw(self, screen):
        cue = self.__rotate(self.skin, self.__calc_pos(self.att_ball), self.angle)
        screen.blit(cue[0], cue[1])  # Draws the cue arround the cue ball

    def __rotate(self, image, pos, angle):
        """Rotate an image using its apex as de center of rotation"""
        w, h = image.get_size()
        box = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
        box_rotate = [p.rotate(angle) for p in box]
        min_box = (
            min(box_rotate, key=lambda p: p[0])[0],
            min(box_rotate, key=lambda p: p[1])[1],
        )
        max_box = (
            max(box_rotate, key=lambda p: p[0])[0],
            max(box_rotate, key=lambda p: p[1])[1],
        )
        origin = (pos[0] + min_box[0], pos[1] - max_box[1])

        rotated_image = pygame.transform.rotate(image, angle)
        return rotated_image, origin

    def __resize(self, image, screen):
        """Resizes game cue to the screen resolution"""
        ratio = (screen.get_size()[1] - 400) / image.get_size()[1]
        widht = ratio * image.get_size()[0]
        height = ratio * image.get_size()[1]
        resized_image = pygame.transform.scale(
            image,
            (
                int(widht),
                int(height),
            ),
        )
        resized_image = pygame.transform.rotate(resized_image, 10)
        return resized_image
