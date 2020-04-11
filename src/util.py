import numpy as np

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


mapa = {1: 6,  # Dictionary for data processing
        2: 4,
        3: 2,
        4: 0,
        5: 15,
        6: 13,
        7: 11,
        8: 9,
        9: 22,
        10: 20,
        11: 18,
        12: 16,
        13: 31,
        14: 29,
        15: 27,
        16: 25,
        17: 38,
        18: 36,
        19: 34,
        20: 32,
        21: 47,
        22: 45,
        23: 43,
        24: 41,
        25: 54,
        26: 52,
        27: 50,
        28: 48,
        29: 63,
        30: 61,
        31: 59,
        32: 57}


def map_state(board: list):
    state = np.empty(32, int)
    for key in mapa.keys():
        if board[mapa[key]] == 'w':
            state[key - 1] = -1
        elif board[mapa[key]] == 'b':
            state[key - 1] = 1
        elif board[mapa[key]] == 'W':
            state[key - 1] = -2
        elif board[mapa[key]] == "B":
            state[key - 1] = 2
        else:
            state[key - 1] = 0

    return state
