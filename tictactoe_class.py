class Board:

    def __init__(self, size):
        self._size = size
        self._setup()
        self._define_winning_combination()

    def _setup(self):
        self._game_board = []
        for x in range(self._size):
            board_row = []
            for y in range(self._size):
                board_row.append((x, y))
            self._game_board.append(board_row)

    def _define_winning_combination(self):
        self.winning_index = []
        self.winning_index.append({(0, 0), (1, 0), (2, 0)})
        self.winning_index.append({(0, 1), (1, 1), (2, 1)})
        self.winning_index.append({(0, 2), (1, 2), (2, 2)})
        self.winning_index.append({(0, 0), (1, 1), (2, 2)})
        self.winning_index.append({(0, 2), (1, 1), (2, 0)})
        self.winning_index.append({(0, 0), (0, 1), (0, 2)})
        self.winning_index.append({(1, 0), (1, 1), (2, 0)})
        self.winning_index.append({(2, 0), (2, 1), (2, 2)})

    def print_board(self):
        for i in range(self._size):
            print(self._game_board[i])

    def update_board(self, player):
         for i, board_row in enumerate(self._game_board):
            for col, val in enumerate(board_row):
                if val == player._moves[-1]:
                    self._game_board[i][col] = str(' ' + player._token + '  ')
                    break

    def check_result(self, player, game):
        win = False
        for i in range(8):
            if set(player._moves).intersection(self.winning_index[i]) == self.winning_index[i]:
                print("{} wins!".format(player._name))
                win = True
                return True
                break

        if game.my_turns == 9 and not win:
            print("Game resulted in a tie...like usual.")
            return True

        return False

class Player:

    def __init__(self, name, token):
        self._name  = name          # int
        self._token = token         # X OR O
        self._moves = []

    def add_move(self, move):
        self._moves.append(move)    # list

    def __str__(self):
        return '{} ({})'.format(self._name, self._token)


class Game:

    def __init__(self):
        self.my_board = Board(3)
        self.my_player = []
        self.my_player.append(Player('Joan', 'X'))
        self.my_player.append(Player('Other', 'O'))
        self.my_turns = 0
        self.my_board.print_board()

    def _validate_move(my_move, player):
        if my_move.count(',') != 1:
            return 1  #not enough parameters

        if my_move in player[0]._moves or my_move in player[1]._moves:
            return 2  #already taken

    def _get_move(self, player_index):
        my_move, first_time = '', True
        while my_move.count(',') != 1:
            if first_time:
                my_move = input("Player {} ({}), where will you play? ".format(self.my_player[player_index]._name,
                                                                               self.my_player[player_index]._token))
            else:
                my_move = input("Invalid input. Player {} ({}), where will you play? ".format(self.my_player[player_index]._name,
                                                                               self.my_player[player_index]._token))
            first_time = False

        my_move = tuple(int(x) for x in my_move.split(','))
        self.my_player[player_index].add_move(my_move)

    def play(self):
        self.my_turns += 1
        player_index = self.my_turns % 2
        self._get_move(player_index)
        self.my_board.update_board(self.my_player[player_index])
        self.my_board.print_board()
        return self.my_board.check_result(self.my_player[player_index], self)

if __name__ == '__main__':
    my_game = Game()
    game_over = False
    while not game_over:
        game_over = my_game.play()