from IPython.display import clear_output
import random

def ttt_board(board):
    clear_output()
    print(' ' + board[7] + '|' + board[8] + '|' + board[9])
    print('-------')
    print(' ' + board[4] + '|' + board[5] + '|' + board[6])
    print('-------')
    print(' ' + board[1] + '|' + board[2] + '|' + board[3])

def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
            marker = input('Would you like to be Xs or Os?')

    if marker == 'X':
        return ('X', 'O')
    else:
        return('O', 'X')

def place_marker(board, marker, position):
        board[position] = marker

def check_winner(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

def choose_first():
    if random.randint(0, 1) == 0:
        return 'player 1'
    else:
        return 'player 2'

def check_square(board, position):
    return board[position] == ' '

def check_board(board):
    for i in range(1, 10):
        if check_square(board, i):
            return False
    return True

def player_choice(board):
    position = ' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not check_square(board, int(position)):
        position = input('Choose your next position: (1-9)')
    return int(position)

def play_again():
    return input('Would you like to play again?').lower().startswith('y')

while True:
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    start_game = True

    while start_game:
        if turn == 'Player 1':
            ttt_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if check_winner(theBoard, player1_marker):
                ttt_board(theBoard)
                print('You won the game')
                start_game = False
            else:
                if check_board(theBoard):
                    ttt_board(theBoard)
                    print('Tie game')
                    break
                else:
                    turn = 'Player 2'

        else:
            ttt_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if check_winner(theBoard, player2_marker):
                ttt_board(theBoard)
                print('You won the game')
                start_game = False
            else:
                if check_board(theBoard):
                    ttt_board(theBoard)
                    print('Tie game')
                    break
                else:
                    turn = 'Player 1'

    if not play_again():
        break




# ttt_board(board)
# player_input()
# place_marker(board, marker, position)
# check_winner(board)
# choose_first()
# check_square(board, position)
# check_board(board)
# player_choice(board)
