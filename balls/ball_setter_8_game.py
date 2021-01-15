"""
    Eduardo Rodríguez Sánchez 
    28/12/2020
    Ball Placer
"""
from math import sqrt
from random import choice


def set_balls(main_table, user_ball, Solids, Stripes) -> list:
    """Creates and sets all properties of the ball objects"""
    aviable_positions = calculate_triangle(main_table, user_ball)

    solid_balls = []
    striped_balls = []

    placed_balls = game_musts(
        main_table, solid_balls, striped_balls, aviable_positions, Solids, Stripes
    )
    n_solids = placed_balls[0]
    n_stripes = placed_balls[1]

    for number in n_solids:
        position = choice(aviable_positions)
        solid_balls.append(
            Solids(
                main_table,
                position,
                number,
            )
        )
        # Deletes de aviable position after placing the ball
        aviable_positions.remove(position)

    for number in n_stripes:
        position = choice(aviable_positions)
        solid_balls.append(
            Stripes(
                main_table,
                position,
                number,
            )
        )
        aviable_positions.remove(position)

    return solid_balls, striped_balls


def calculate_triangle(main_table, user_ball) -> list:
    """Creates all the x and y pairs wich the pool
    triangle is made of."""
    start_position = [main_table.width * 0.70, main_table.height / 2]
    positions = [start_position]
    set_of_positions = [start_position]

    n = 15  # Number of balls
    # Recursion where from one point comes a symetrical pair
    for j in set_of_positions:
        positions.append(
            [j[0] + sqrt(3) * user_ball.radius, j[1] - user_ball.radius + 1]
        )
        positions.append(
            [j[0] + sqrt(3) * user_ball.radius, j[1] + user_ball.radius - 1]
        )
        set_of_positions.append(
            [j[0] + sqrt(3) * user_ball.radius, j[1] - user_ball.radius + 1]
        )
        set_of_positions.append(
            [j[0] + sqrt(3) * user_ball.radius, j[1] + user_ball.radius - 1]
        )
        n -= 1
        if n == 0:
            break

    # Elminiates all the repeaded pair values
    final_positions = []
    for position in positions:
        if position not in final_positions:
            final_positions.append(position)

    return final_positions


def game_musts(
    main_table, solid_balls, striped_balls, aviable_positions, Solids, Stripes
) -> list:
    """Places the necessary balls (apex, corners and center) of an 8-ball game
    following the rules arrangement."""
    n_solids = [number for number in range(1, 9)]
    n_stripes = [number for number in range(9, 16)]

    # Solid 1 ball must positions at the apex
    solid_balls.append(Solids(main_table, aviable_positions[0], 1))
    n_solids.remove(1)
    # Black 8 ball must positions at the center (6th)
    solid_balls.append(Solids(main_table, aviable_positions[4], 8))
    n_solids.remove(8)
    # Corner rack balls hav to to be different type
    random_solid = n_solids.pop(n_solids.index(choice(n_solids)))
    random_striped = n_stripes.pop(n_stripes.index(choice(n_stripes)))
    if choice((0, 1)):
        solid_balls.append(Solids(main_table, aviable_positions[10], random_solid))
        striped_balls.append(Stripes(main_table, aviable_positions[14], random_striped))
    else:
        solid_balls.append(Solids(main_table, aviable_positions[14], random_solid))
        striped_balls.append(Stripes(main_table, aviable_positions[10], random_striped))

    # Used positions are removed from aviable positions.
    # The indexes should be 0, 4, 10, 14 but beacuse
    # each iteration aviable_postions reduces its lenght -1
    # it is necessary to adjust the indexes.
    adjust = 0
    for i in (0, 4, 10, 14):
        aviable_positions.pop(i - adjust)
        adjust += 1

    return n_solids, n_stripes
