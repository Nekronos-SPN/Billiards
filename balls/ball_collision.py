"""
    Eduardo Rodríguez Sánchez
    30/12/2020
    Collision and physics
"""
from math import dist
from random import uniform


def check_collision(user_ball, game_balls):
    """Goes over every existing pair of balls cheking if they are colliding"""
    all_balls = [user_ball] + game_balls[0] + game_balls[1]
    n_balls = len(all_balls)
    for i in range(n_balls):
        for j in range(n_balls):
            if i != j:
                if is_colliding(all_balls[i], all_balls[j]):
                    bounce(all_balls[i], all_balls[j])


def is_colliding(b1, b2) -> bool:
    distance = dist((b1.x_pos, b1.y_pos), (b2.x_pos, b2.y_pos))
    if distance < b1.radius + b2.radius:
        return True
    else:
        return False


def bounce(b1, b2):
    """Uses vectors to calculate the resulting direction of a collision and
    its velocity"""
    if b1.velocity > b2.velocity:
        b2.direction = [
            b2.x_pos - b1.x_pos,
            b2.y_pos - b1.y_pos,
        ]

        b2.velocity = b1.velocity - b1.velocity / 8
        b1.velocity = b2.velocity
        momentum = b1.direction[0] + uniform(-0.01, 0.01), b1.direction[1] + uniform(
            -0.01, 0.01
        )
        b1.direction = [x[0] - x[1] for x in zip(momentum, b2.direction)]
    elif b1.velocity <= b2.velocity:
        b1.direction = [
            b1.x_pos - b2.x_pos,
            b1.y_pos - b2.y_pos,
        ]
        b1.velocity = b2.velocity - b1.velocity / 8
        b2.velocity = b1.velocity
        momentum = b2.direction[0] + uniform(-0.01, 0.01), b2.direction[1] + uniform(
            -0.01, 0.01
        )
        b2.direction = [x[0] - x[1] for x in zip(momentum, b1.direction)]