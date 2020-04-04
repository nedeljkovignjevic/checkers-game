# DATASET -> http://www.fierz.ch/download.php
# format -> http://www.bobnewell.net/filez/reinfeld2ndedition.pdf
# ML update -> http://www.bobnewell.net/nucleus/checkers.php?itemid=1177
# TODO: update rules, bitboard states, train

from flask import Flask, request
from chess import Board as ChessBoard
from chess import Piece, QUEEN, Color, WHITE, BLACK

from src.board import init_board, init_gui_board, print_board, game_over
from src.state import State, Turn
from src.checkers import move_function, play_move, game_loop


BOARD = ChessBoard(None)
init_gui_board(BOARD)
state_board = init_board()

app = Flask(__name__)


def human_move(src, dest):
    piece = BOARD.remove_piece_at(src)
    if dest > 55:
        BOARD.set_piece_at(dest, Piece(QUEEN, Color(WHITE)))
    else:
        BOARD.set_piece_at(dest, piece)

    jump = play_move(state_board, [src, dest], Turn.WHITE)
    if jump is not None:
        BOARD.remove_piece_at(jump)

    print_board(state_board)


def computer_move(move):
    jump = play_move(state_board, move, Turn.BLACK)

    piece = BOARD.remove_piece_at(move[0])
    if move[1] < 8:
        BOARD.set_piece_at(move[1], Piece(QUEEN, BLACK))
    else:
        BOARD.set_piece_at(move[1], piece)

    if jump is not None:
        BOARD.remove_piece_at(jump)

    print_board(state_board)


@app.route('/')
def hello():
    index_html = open("static/index.html").read()
    return index_html.replace('start', BOARD.fen())


@app.route("/self-play")
def self_play():
    turn = Turn.WHITE
    ret = '<html><head>'
    # while not game_over(state_board):
    #     state = State(state_board, turn, [])
    #     move = move_function(state)
    #     computer_move(move)
    #     turn = Turn.BLACK if turn == Turn.WHITE else Turn.WHITE
    #     ret += BOARD
    return ret


@app.route("/move")
def move():

    if game_over(state_board):
        print("GAME IS OVER")
        response = app.response_class(
            response="game over",
            status=200
        )
        return response

    source = int(request.args.get('from', default=''))
    destination = int(request.args.get('to', default=''))

    # human move
    human_move(source, destination)

    # computer_move
    state = State(state_board, Turn.BLACK, [])
    move = move_function(state)
    computer_move(move)

    response = app.response_class(
        response=BOARD.fen(),
        status=200
    )

    return response


@app.route("/new-game")
def new_game():
    BOARD.clear_board()
    init_gui_board(BOARD)
    state_board.clear()
    temp = init_board()
    for i in range(64):
        state_board.append(temp[i])

    response = app.response_class(
        response=BOARD.fen(),
        status=200
    )
    return response


if __name__ == '__main__':

    app.run(debug=True)