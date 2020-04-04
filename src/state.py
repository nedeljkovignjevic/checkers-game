import enum
from copy import deepcopy
from src.util import black_steps, black_jump_steps, white_steps, white_jump_steps, king_steps, king_jump_steps, non_legal_positions


class Turn(enum.Enum):
    WHITE = 0
    BLACK = 1


class State(object):
    """
    Modelling state on checkers board
    """

    def __init__(self, board: list, turn: Turn, move: list):
        self.board = board
        self.turn = turn
        self.move = move

    def change_turn(self):
        if self.turn == Turn.BLACK:
            self.turn = Turn.WHITE
        else:
            self.turn = Turn.BLACK

    def is_terminal_state(self):
        b_counter = 0
        w_counter = 0
        for i in range(63):
            if self.board[i] == "b" or self.board[i] == "B":
                b_counter += 1
            elif self.board[i] == "w" or self.board[i] == "W":
                w_counter += 1

        if b_counter == 0 or w_counter == 0 or len(self.get_states()) == 0:
            return True
        elif b_counter > 3 and w_counter == 1 or w_counter > 3 and b_counter == 1:
            return True

    def get_states(self):
        if self.turn == Turn.BLACK:
            player = "b"
        else:
            player = "w"

        states = []
        for i in range(64):
            if self.board[i].lower() == player:
                get_legal_jumps(self.board, i, self.turn, states)

        if len(states) == 0:
            for i in range(64):
                if self.board[i].lower() == player:
                    get_legal_moves(self.board, i, self.turn, states)

        return states


""" 
-----------------------------------------------------------------------------------------------------------------
Getting all legal moves for 'get_states' function from State class
-----------------------------------------------------------------------------------------------------------------
"""


def get_legal_jumps(board: list, i: int, turn: Turn, states: list):

    if turn == Turn.BLACK:

        if board[i] == "B":
            jumps(board, i, turn, states, king_jump_steps(), 55, 64, "w")
        elif board[i] == "b":
            jumps(board, i, turn, states, black_jump_steps(), 55, 64, "w")

    elif turn == Turn.WHITE:

        if board[i] == "W":
            jumps(board, i, turn, states, king_jump_steps(), 0, 8, "b")
        elif board[i] == "w":
            jumps(board, i, turn, states, white_jump_steps(), 0, 8, "b")


def get_legal_moves(board: list, i: int, turn: Turn, states: list):

    if turn == Turn.BLACK:

        if board[i] == "B":
            moves(board, i, turn, states, king_steps(), 55, 64)
        elif board[i] == "b":
            moves(board, i, turn, states, black_steps(), 55, 64)

    elif turn == Turn.WHITE:

        if board[i] == "W":
            moves(board, i, turn, states, king_steps(), 0, 8)
        elif board[i] == "w":
            moves(board, i, turn, states, white_steps(), 0, 8)


def moves(board, i, turn, states, steps, lower_border, upper_border):
    """
    Fill the list 'states' with legal moves
    """

    legal_positions = non_legal_positions()
    for step in steps:
        index = step + i
        if index in legal_positions:
            continue
        if 63 >= index >= 0 and board[index] == '-':
            board_copy = deepcopy(board)
            board_copy[index], board_copy[i] = board_copy[i], '-'
            if lower_border < i < upper_border:
                board_copy[index] = board_copy[index].upper()
            s = State(board_copy, turn, [i, index])
            states.append(s)


def jumps(board, i, turn, states, steps, lower_border, upper_border, value):
    """
    Fill the list 'states' with jump moves
    """

    legal_positions = non_legal_positions()
    for step in steps:
        index = step + i
        if index in legal_positions:
            continue

        mid_i = int(step/2) + i
        if 63 >= index >= 0 and board[index] == '-' and board[mid_i].lower() == value:
            board_copy = deepcopy(board)
            board_copy[index], board_copy[i] = board_copy[i], '-'
            board_copy[mid_i] = '-'
            if lower_border < i < upper_border:
                board_copy[index] = board_copy[index].upper()
            states.append(State(board_copy, turn, [i, index]))