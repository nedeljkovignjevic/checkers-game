import torch
from math import floor

from src.neural_network import Net
from src.util import map_state


MODEL = Net()
MODEL.load_state_dict(torch.load('model/model_test.pth', map_location=torch.device('cpu')))
MODEL.eval()


def alpha_beta(state, depth, a, b, max_player):
    """
    Minimax with alpha–beta pruning implementation
    """

    if depth == 0 or state.is_terminal_state():
        return value_network(state)

    if max_player is True:
        value = -10000
        for s in state.get_states():
            value = max(value, alpha_beta(s, depth - 1, a, b, False))
            a = max(a, value)
            if a >= b:
                break
        return value

    else:
        value = 10000
        for s in state.get_states():
            value = min(value, alpha_beta(s, depth - 1, a, b, True))
            b = min(b, value)
            if b <= a:
                break
        return value


def heuristic_value(state):
    """"
    Using heurustic method to evaluate board sate
    """

    board = state.board

    value = 0
    b2 = 0
    for i in range(63, -1, -1):
        if b2 == 8: b2 = 0

        if board[i] == '-':
            b2 += 1
            if b2 == 8: b2 = 0
            continue

        b1 = floor(i / 8)
        if board[i] == 'w':
            value -= 5 + 7 - b1 + abs(b2 - 4 + abs(b1 - 4))
        elif board[i] == 'b':
            value += 5 + b1 + abs(b2 - 4) + abs(b1 - 4)
        elif board[i] == 'W':
            value -= 14 + abs(b2 - 4) + abs(b1 - 4)
        elif board[i] == 'B':
            value += 14 + abs(b2 - 4) + abs(b1 - 4)
        b2 += 1

    return value


def value_network(state):
    """
    Using neural network to evaluate board state
    """

    board = state.board
    state = map_state(board)
    state = torch.FloatTensor(state).unsqueeze(0)
    prediction = MODEL(state)
    return prediction

