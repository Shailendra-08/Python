
from IPython.display import clear_output
import random


def display_board(board):
    clear_output()
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

    # print(board[7] + '|' +board[8] + '|' +board[9])




# test_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

# display_board(test_board)
# display_board(test_board)



def player_input():
    marker = ''

    while marker != 'X' and marker != 'O':
        marker =input('player1: Choose X or O:').upper()

    if marker == 'X':
        return('X','O')
    else:
        return('O','X')



# player1_marker ,player2_marker = player_input()


def place_marker(board,marker,position):
    board[position] = marker



def win_check(board,mark):
    #all rows and check to see if they all share the same marker
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[1] == mark and board[4] == mark and board[7] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[2] == mark and board[5] == mark and board[8] == mark) or
    (board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[6] == mark and board[3] == mark and board[9] == mark) or
    (board[1] == mark and board[5] == mark and board[9] == mark) or
    (board[7] == mark and board[5] == mark and board[3] == mark))



def choose_first():
    flip = random.randint(0,1)

    if flip ==0:
        return 'player 1'
    else:
        return 'player 2'




def space_check(board,position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False

# Board is Full we return True
    return True


def player_choice(board):
    position =0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('choose a position: (1-9)'))
    return position


def replay():
    choice = input('Play again? Enter Y or N')

    return choice == 'Yes'



# While loop for keep runing the game

print('Welcome to Tic-Tac-Toe')

while True:

    #play the game

    # Set Everything up (Board , Whos First,choose Marker "X" "O")
    the_board =[ ' ']*10
    player1_marker,player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first')
    play_game = input('Ready to Play? y or n')

    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    #agme play

    while game_on:
        if turn == 'player 1':
            #show the board
            display_board(the_board)
            # choose the position
            position = player_choice(the_board)
            place_marker(the_board,player1_marker,position)


            #check if they won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('Player 1 has WON!!')
                game_on = False

            else:
                # or check if there is a tie

                if full_board_check(the_board):
                    display_board(the_board)
                    print("THE game is TIE !!!1")
                    game_on = False
                else:
                    turn = 'Player 2'

        else:

            # show the board
            display_board(the_board)
            # choose the position
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)

            # check if they won
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player 2 has WON!!')

                # player 2 has WON

                game_on = False

            else:
                # or check if there is a tie

                if full_board_check(the_board):
                    display_board(the_board)
                    print("THE game is TIE !!!1")
                    game_on = False
                else:
                    turn = 'player 1'




    if not replay():
        break









































