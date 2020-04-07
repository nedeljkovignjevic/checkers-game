import numpy as np
from src.board import init_board
from src.checkers import play_move, Turn


dic = {1: (7, 6),
       2: (7, 4),
       3: (7, 2),
       4: (7, 0),
       5: (6, 7),
       6: (6, 5),
       7: (6, 3),
       8: (6, 1),
       9: (5, 6),
       10: (5, 4),
       11: (5, 2),
       12: (5, 0),
       13: (4, 7),
       14: (4, 5),
       15: (4, 3),
       16: (4, 1),
       17: (3, 6),
       18: (3, 4),
       19: (3, 2),
       20: (3, 0),
       21: (2, 7),
       22: (2, 5),
       23: (2, 3),
       24: (2, 1),
       25: (1, 6),
       26: (1, 4),
       27: (1, 2),
       28: (1, 0),
       29: (0, 7),
       30: (0, 5),
       31: (0, 3),
       32: (0, 1)}


def get_state(board: dict):
    state = np.empty(32, int)
    for key in dic.keys():
        if board[dic[key]] == 'w':
            state[key-1] = -1
        elif board[dic[key]] == 'b':
            state[key-1] = 1
        elif board[dic[key]] == 'W':
            state[key-1] = -2
        elif board[dic[key]] == "B":
            state[key-1] = 2
        else:
            state[key-1] = 0

    return state


def get_dataset(n_samples=None):
    """
    Parse checkers OCA dataset and save

    values:
        draw        1/2-1/2: 0
        black wins  0-1: 1
        white wins  1-0: -1
    """

    states, values = [], []
    value = {'1/2-1/2': 0, '0-1': 1, '1-0': -1}
    n_games = {'1/2-1/2': 0, '0-1': 0, '1-0': 0}
    parsed_game = 0
    with open('data/OCA_2.0.txt') as file:
        for part in file.read().split('\n\n'):
            tokens = part.split()
            val = tokens[-1]
            n_games[val] = n_games[val] + 1
            print(f'Parsing game {parsed_game}')

            board = init_board()
            skiping = True
            turn = Turn.BLACK
            for token in tokens:
                if skiping is True:
                    if token == '1.':
                        skiping = False
                    continue
                else:
                    if '.' in token or token == val:
                        continue
                    if 'x' in token:  # multiple jump
                        new_token = token.split('x')
                        n = len(new_token)
                        for i in range(n - 1):
                            try: move = [dic[int(new_token[i])], dic[int(new_token[i + 1])]]
                            except: break
                            play_move(board, move, turn)
                            # show_board(board)
                    else:
                        t = token.split('-')
                        try: move = [dic[int(t[0])], dic[int(t[1])]]
                        except: break
                        play_move(board, move, turn)
                        # show_board(board)

                    states.append(get_state(board))
                    values.append(value[val])
                    turn = Turn.BLACK if turn == Turn.WHITE else Turn.WHITE

            parsed_game += 1

    print(f'1/2-1/2 -> {n_games["1/2-1/2"]}')
    print(f'0-1     -> {n_games["0-1"]}')
    print(f'1-0     -> {n_games["1-0"]}')

    x, y = np.array(states), np.array(values)
    np.savez("data/processed.npz", x, y)
