import sys
import random

BOARD_WIDTH = 7
BOARD_HEIGHT = 6


#TODO: FIX CHECK MOVE TO RETURN ROW MOVE WILL BE PLAYED IN
#TODO: PASS PLAYER IN FOR ALL MOVES
#TODO: CLEAN UP THIS MESS OF CODE
#TODO: GAAAAAAHHHHHHHHHHHH

class Player:
    def __init__(self, user_name, id, classic=False):
        self.name = user_name
        self.id = id
        if not classic:
            self.powerups = {'scramble': True,
                             'seize': True,
                             'detonate': True,
                             'warp': True}
        else:
            self.powerups = {'scramble': False,
                             'seize': False,
                             'detonate': False,
                             'warp': False}

class Game_Board:
    def __init__(self):
        self.game_space = [0 for x in range(BOARD_WIDTH)] [0 for y in range(BOARD_HEIGHT)]

def game_start():
    random.seed()
    move_counter = 0
    global game_board = Game_Board()
    global prev_boards = []
    player_array = []

    while True:
        try:
            game_type = int(input('Select game type(1. Classic, 2. Battle Royale): '))
        except ValueError:
            print('\nNot a valid option\n')
            continue
        else:
            if game_type == 1:
                classic = True
                break
            elif game_type == 2:
                classic = False
                break
            else:
                print('\nNot a valid option\n')
                continue

    while True:
        try:
            num_players = int(input('Enter number of players: '))
        except ValueError:
            print('\n Invalid number of players\n')
            continue
        else:
            break

    for player in range(num_players):
        name = input('Enter name for Player ' + (player+1) + ': ')
        player_array.append(Player(name, (player+1),  classic))

    while not check_winner(game_board):
       make_move(player_array[move_counter % num_players], game_board, prev_boards)
       move_counter += 1

def display_board(game_board):
    print('  1   2   3   4   5   6   7')
    for y in range(BOARD_WIDTH):
        print('--------------------------------')
        for x in range(BOARD_HEIGHT):
            sys.stdout.write('|  ')
            sys.stdout.flush()
            if game_board[x][y] == 0:
                sys.stdout.write('   ')
                sys.stdout.flush()
            else:
                sys.stdout.write(str(game_board[x][y]) + '  ')
                sys.stdout.flush()
            if x == 6:
                print('|')

    print('--------------------------------\n')

def check_winner(game_board):
    # diofjsdajf

def make_move(player, game_board, prev_boards):
    display_board(game_board)
    print("it's " + player.name + "'s turn')
    if not any(player.powerups):
        while True:
            try:
                column_select = int(input('Select column to make move (1-7): '))
            except ValueError:
                print('That is not a valid move')
                continue
            else:
                if column_select < 1 || column_select > 7:
                    print('That is not a valid move')
                    continue
                if not check_move(column_select):
                    print('That is not a valid move')
                    continue
                break
    update_board(game_board, prev_boards, (column_select-1))

    else:
        while True:
            try:
                move_option = int(input('Select move type (1. Normal move, 2. Use Power-up): '))
            except ValueError:
                print('Not a valid option')
                continue
            else:
                if (move_option < 1) || (move_option > 2):
                    print('Not a valid option')
                    continue

                elif move_option == 1:
                    while True:
                        try:
                            move_column = int(input('Select column to make move(1-7): '))
                        except ValueError:
                            print ('That is not a valid move')
                            continue
                        else:
                            if ((move_column < 1) || (move_column > 7) || not check_move(move_column)):
                                print ('That is not a valid move')
                                continue
                            else:
                                update_board(game_board, prev_boards, (move_column-1))
                                break

                elif move_option == 2:
                    while True:
                        try:
                            power_option = int(input('Select Power-up (1. Sieze, 2. Detonate, 3. Warp, 4. Scramble, 5. Back): '))
                        except ValueError:
                            print('Not a valid option')
                            continue
                        else:
                            if (power_option < 1) || (power_option > 5):
                                print('Not a valid option')
                            elif power_option == 1:
                                if not player.powerup['sieze']
                                    print('Power-up not available')
                                    continue
                                else:
                                    while True:
                                        try:
                                            seize_column = int(input('Select column to make move (1-7): '))
                                        except ValueError:
                                            print('That is not a valid move')
                                            continue
                                        else:
                                            if ((seize_column < 1) || (seize_column > 7) || (not check_move(sieze_column)))
                                                print('That is not a valid move')
                                                continue
                                            else:
                                                update_board(game_board, prev_boards, (sieze_column-1), seize=True)
                                                break

                            elif power_option == 2:
                                if not player.powerup['detonate']:
                                    print('Power-up not available')
                                    continue
                                else:
                                    while True:
                                        try:
                                            detonate_column = int(input('Select column to make move (1-7): '))
                                        except ValueError:
                                            print('That is not a valid move')
                                            continue
                                        else:
                                            if ((detonate_column < 1) || (detonate_column > 7) || (not check_move(detonate_column))):
                                                print('That is not a valid move')
                                                continue
                                            else:
                                                update_board(game_board, prev_boards, (detonate_column-1), detonate=True)
                                                break

                            elif power_option == 3:
                                if not player.powerup['warp']:
                                    print('Power-up not available')
                                    continue
                                else:
                                    update_board(game_board, prev_boards, warp=True)
                                    break

                            elif power_option == 4:
                                if not player.powerup['scramble']:
                                    print('Power-up not available')
                                    continue
                                else:
                                    update_board(game_board, prev_boards, scramble=True)
                                    break

                            elif power_option == 5:
                                while True:
                                    try:
                                        move_column = int(input('Select column to make move(1-7): '))
                                    except ValueError:
                                        print ('That is not a valid move')
                                        continue
                                    else:
                                        if ((move_column < 1) || (move_column > 7) || check_move(move_column - 1) < 0):
                                            print ('That is not a valid move')
                                            continue
                                        else:
                                            row = check_move(move_column - 1)
                                            update_board(game_board, prev_boards, (move_column-1))
                                            break

def randomize(player, game_board, num_players=2):
    player.powerups['scramble'] = False
    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            if not game_board[x][y]:
                game_board[x][y] = random.randint(1,2)

def sieze_opponent_piece(player, game_board, column, row):
    player.powerups['sieze'] = False

    while True:
        direction = random.randint(1,8)
        if direction == 1:
            if ((column-1) < 0) || ((row-1) < 0):
                continue
            elif game_board[column - 1][row - 1] == player.id:
                continue
            else:
                game_board[column - 1][row - 1] = player.id
                break
        if direction == 2:
            if (row - 1) < 0:
                continue
            elif game_board[column][row - 1] == player.id:
                continue
            else:
                 game_board[column][row - 1] == player.id
                 break
        if direction == 3:
            if ((column + 1) < BOARD_WIDTH) || ((row - 1) < 0):
                continue
            elif game_board[column + 1][row - 1] == player.id:
                continue
            else:
                game_board[column + 1][row - 1] = player.id
                break
        if direction == 4:
            if (column + 1) < BOARD_WIDTH:
                continue
            elif game_board[column + 1][row] == player.id:
                continue
            else:
                game_board[column + 1][row] = player.id
                break
        if direction == 5:
            if ((column + 1) < BOARD_WIDTH) || ((row + 1) < BOARD_HEIGHT):
                continue
            elif game_board[column + 1][row + 1] == player.id:
                continue
            else:
                game_board[column + 1][row + 1] = player.id
                break
        if direction == 6:
            if (row + 1) < BOARD_HEIGHT:
                continue
            elif game_board[column][row + 1] == player.id:
                continue
            else:
                game_board[column][row + 1] = player.id
                break
        if direction == 7:
            if ((column - 1) < 0) || ((row + 1) < BOARD_HEIGHT):
                continue
            elif game_board[column - 1][row + 1] == player.id:
                continue
            else:
                game_board[column - 1][row + 1] = player.id
                break
        if direction == 8:
            if (column-1) < 0:
                continue
            elif game_board[column - 1][row] == player.id:
                continue
            else:
                game_board[column - 1][row] = player.id
                break

def detonate(player, game_board, column, row):
    player.powerups['detonate'] = False
    if ((column - 1) < 0) && ((row - 1) < 0):
        game_board[column + 1][row] = 0
        game_board[column + 1][row + 1] = 0
        game_board[column][row + 1] = 0
    elif ((column - 1) < 0) && ((row + 1) > BOARD_HEIGHT):
        game_board[column][row - 1] = 0
        game_board[column + 1][row - 1] = 0
        game_board[column + 1][row] = 0
    elif ((column + 1) > BOARD_WIDTH && ((row - 1) < 0):
        game_board[column - 1][row] = 0
        game_board[column - 1][row + 1] = 0
        game_board[column][row + 1] = player.id
    elif ((column + 1) > BOARD_WIDTH) && ((row + 1) > BOARD_HEIGHT):
        game_board[column][row - 1] = 0
        game_board[column - 1][row - 1] = 0
        game_board[column - 1][row] = 0
    elif (column - 1) < 0:
        game_board[column][row - 1] = 0
        game_board[column + 1][row - 1] = 0
        game_board[column + 1][row] = 0
        game_board[column + 1][row + 1] = 0
        game_board[column][row + 1] = player.id

    elif (column + 1) > BOARD_WIDTH:
        game_board[column][row - 1] = 0
        game_board[column - 1][row - 1] = 0
        game_board[column - 1][row] = 0
        game_board[column - 1][row + 1] = 0
        game_board[column][row + 1] = player.id
    elif (row - 1) < 0:
        game_board[column - 1][row] = 0
        game_board[column - 1][row + 1] = 0
        game_board[column + 1][row + 1] = 0
        game_board[column + 1][row] = 0
        game_board[column][row + 1] = player.id
    elif (row + 1) > BOARD_HEIGHT:
        game_board[column - 1][row] = 0
        game_board[column - 1][row - 1] = 0
        game_board[column][row - 1] = 0
        game_board[column + 1][row - 1] = 0
        game_board[column + 1][row] = 0
    else:
        game_board[column - 1][row - 1] = 0
        game_board[column][row - 1] = 0
        game_board[column + 1][row - 1] = 0
        game_board[column + 1][row] = 0
        game_board[column + 1][row + 1] = 0
        game_board[column - 1][row + 1] = 0
        game_board[column - 1][row] = 0
        game_board[column][row + 1] = player.id

    return game_board

def time_warp(player, game_board, prev_boards):
    player.powerups['warp'] = False
    game_board = prev_boards.pop(3)

    return game_board

def check_move(game_board, column):
    row_counter = 5
    while row_counter >= 0:
        if not game_board[column][row_counter]:
            return row_counter
        row_counter -= 1
    return -1

def update_board(player, game_board, prev_boards, column_select=0, sieze=False, detonate=False, warp=False, scramble=False):

def update_moves(game_board, prev_boards):
    prev_boards.append(game_board)
    if len(prev_boards) > 3:
        prev_boards.pop()

def main():
    # dkljskldf
