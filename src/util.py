"""
Getting all legal steps for 'get_states' function from State class
"""


def non_legal_positions():
    return [1, 3, 5, 7,
            8, 10, 12, 14,
            17, 19, 21, 23,
            24, 26, 28, 30,
            33, 35, 37, 39,
            40, 42, 44, 46,
            49, 51, 53, 55,
            56, 58, 60, 62]


def black_steps():
    return [-7, -9]


def black_jump_steps():
    return [-14, -18]


def white_steps():
    return [7, 9]


def white_jump_steps():
    return [14, 18]


def king_steps():
    return [7, 9, -7, -9]


def king_jump_steps():
    return [14, 18, -14, 18]
