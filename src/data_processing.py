import numpy as np
from src.board import init_board, print_board
from src.checkers import play_move, Turn
from src.util import mapa, map_state


def get_dataset():
    """
    Parse checkers OCA dataset and save as numpy array

    1/2-1/2: 0  -> draw
    0-1: 1      -> black wins
    1-0: -1     -> white wins
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
            turn = Turn.WHITE
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
                            try:
                                move = [mapa[int(new_token[i])], mapa[int(new_token[i + 1])]]
                            except:
                                break
                            play_move(board, move, turn)
                            # print_board(board)
                            # print()
                    else:
                        t = token.split('-')
                        try:
                            move = [mapa[int(t[0])], mapa[int(t[1])]]
                        except:
                            break
                        play_move(board, move, turn)
                        # print_board(board)
                        # print()

                    states.append(map_state(board))
                    values.append(value[val])
                    turn = Turn.BLACK if turn == Turn.WHITE else Turn.WHITE

            parsed_game += 1

    print(f'1/2-1/2 -> {n_games["1/2-1/2"]}')
    print(f'0-1     -> {n_games["0-1"]}')
    print(f'1-0     -> {n_games["1-0"]}')

    x, y = np.array(states), np.array(values)
    np.savez("data/processed.npz", x, y)
