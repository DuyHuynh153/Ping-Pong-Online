import math
import random
import re
import pygame

REL_VALUE_MULTIPLIER = 10_000


def to_rel(abs_value: int) -> float:
    return abs_value / REL_VALUE_MULTIPLIER


def to_abs(rel_value: float) -> int:
    return int(rel_value * REL_VALUE_MULTIPLIER)




def signum(num) -> int:
    if num > 0:
        return 1
    if num < 0:
        return -1
    return 0



def lerp(start, stop, amt):
    return start + ((stop - start) * amt)


def line_line_intersection(x1, y1, x2, y2, x3, y3, x4, y4) -> tuple:

    # paralell_checking is use to check if 2 lines are parallel
    paralell_checking = ((x1 - x2) * (y3 - y4)) - ((y1 - y2) * (x3 - x4))
    if paralell_checking == 0:
        return None  # 2 duong song song

    """
    t: position where ball will hit paddle (t is the intersection point), t is relative value, 
    example: t = 0.5 -> ball hit at the middle of the of line 1 (from x1, y1 to x2, y2)
    -------------
    u: is using for checking the direction of the ball
    u < 0: The ball is moving away from the paddle. The AI does not move the paddle.
    u >= 0: The ball is moving towards the paddle or is at the same level as the paddle on the y-axis. 
    The AI calculates where the ball will hit the paddle and decides whether to move the paddle up or down.    
    """
    t = (((x1 - x3) * (y3 - y4)) - ((y1 - y3) * (x3 - x4))) / paralell_checking
    u = (((x1 - x3) * (y1 - y2)) - ((y1 - y3) * (x1 - x2))) / paralell_checking


    return t, u


def get_vel_max_total(vel_max_component: float) -> float:
    return 1.4143 * vel_max_component


def reset_ball_rel_vel(rel_vel_max_component: float, direction: int) -> tuple:
    return direction * rel_vel_max_component, 0
# def get_ball_initial_rel_vel(rel_vel_max_component: float, _random: bool,
#                              x_vel_min_factor: float = 0.62,
#                              total_vel_max_variance: float = 0.1) -> tuple:
#
#     if not _random:
#         return random.choice((1, -1)) * rel_vel_max_component, 0  # Right or left
#
#     max_vel_sq = 2 * (rel_vel_max_component ** 2)
#     vel_sq = max_vel_sq * random.uniform(1 - total_vel_max_variance, 1 + total_vel_max_variance)
#
#     # decompose total_vel velocity into components
#     vel_x_sq = vel_sq * random.uniform(x_vel_min_factor ** 2, 0.9)
#     vel_y_sq = vel_sq - vel_x_sq
#
#     return random.choice((1, -1)) * math.sqrt(vel_x_sq), random.choice((1, -1)) * math.sqrt(vel_y_sq)


def blit_text(surface: pygame.Surface, text: str, pos: tuple, font: pygame.font.Font, color=pygame.Color('white')) -> tuple:
    """
    Renders a multiple line text on the surface, wrapping it when necessary

    :return: (width, height) of whole rendered text on the given surface
    """

    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.

    space_width = font.size(' ')[0]  # The width of a space.
    font_height = font.get_height()
    font_linesize = font.get_linesize()

    max_width, max_height = surface.get_size()
    x, y = pos

    word_height = 0
    max_x2 = 0

    for line in words:
        for word in line:
            word_surface = font.render(word, True, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height + font_linesize  # Start on new row.
                max_x2 = max(x, max_x2)
            else:
                max_x2 = max(x + word_width, max_x2)
            surface.blit(word_surface, (x, y))
            x += word_width + space_width
        x = pos[0]  # Reset the x.
        y += max(word_height, font_height) + font_linesize  # Start on new row.

    return max_x2 - pos[0], y - pos[1]