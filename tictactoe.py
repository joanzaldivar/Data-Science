# Setup winning combinations
winning_index = []
winning_index.append({(0, 0), (1, 0), (2, 0)})
winning_index.append({(0, 1), (1, 1), (2, 1)})
winning_index.append({(0, 2), (1, 2), (2, 2)})
winning_index.append({(0, 0), (1, 1), (2, 2)})
winning_index.append({(0, 2), (1, 1), (2, 0)})
winning_index.append({(0, 0), (0, 1), (0, 2)})
winning_index.append({(1, 0), (1, 1), (2, 0)})
winning_index.append({(2, 0), (2, 1), (2, 2)})

def print_board(board):
    for i in range(3):
        print(board[i])

def setup_game():
    board = [[(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)]]
    print_board(board)
    return board

def set_token():
    token = []
    token.append('  O ')
    token.append('  X ')
    return token

def play(board, moves, player, token):
    my_move = tuple(int(i) for i in (input("Player {}, where will you play? ".format(token[player]))).split(','))

    # Save player's moves
    moves[player].append((my_move))

    # Update board
    for i in range(3):
        for col, val in enumerate(board[i]):
            if val == my_move:
                my_board[i][col] = token[player]
                break

    print_board(board)
    return board, moves

def check_result(moves, player, token):

    win = False
    for i in range(8):
        if set(moves[player]).intersection(winning_index[i]) == winning_index[i]:
            print("Player {} wins!".format(token[player]))
            win = True
            return True
            break

    if turns == 9 and not win:
        print("Game resulted in a tie...like usual.")
        return True

    return False


# Play the game
my_board = setup_game()
my_token = set_token()

my_moves = [[],[]]
game_over, turns = False, 0

while not game_over:
    turns += 1
    my_player = turns % 2
    my_board, my_moves = play(my_board, my_moves, my_player, my_token)
    game_over = check_result(my_moves, my_player, my_token)


