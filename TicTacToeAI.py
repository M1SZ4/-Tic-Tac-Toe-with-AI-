from math import inf
import random


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        # create empty game board
        self.board = []
        for i in range(3):
            self.board.append([])
            for j in range(3):
                self.board[i].append(" ")

    def print_board(self):
        """Print game board in table format"""
        print("---------")
        for element in self.board:
            print("|", *element, "|")
        print("---------")

    def play_game(self):
        """Main game loop"""
        while True:
            self.choose_field(self.player1, "X")
            if self.check_win(self.board, "X"):
                print("X wins")
                break
            if len(self.empty_fields(self.board)) == 0:
                print("Draw")
                break

            self.choose_field(self.player2, "O")
            if self.check_win(self.board, "O"):
                print("O wins")
                break
            if len(self.empty_fields(self.board)) == 0:
                print("Draw")
                break

        return True

    def choose_field(self, player, mark):
        if player == "user":
            """"Player move"""
            while True:
                try:
                    x, y = [int(n) for n in input("Enter the coordinates: ").split()]
                except ValueError:
                    print('You should enter numbers!')
                else:
                    if 1 <= x <= 3 and 1 <= y <= 3:
                        temp_x = x
                        x = abs(y - 3)
                        y = temp_x - 1
                        if self.board[x][y] == " ":
                            self.move(x, y, mark)
                            break
                        else:
                            print("This cell is occupied! Choose another one!")
                    else:
                        print("Coordinates should be from 1 to 3!")

        elif player == "easy":
            """computer easy AI - random move"""
            print('Making move level "easy"')
            self.random_move(mark)

        elif player == "medium":
            """computer medium AI - makes a move if it is possible to end the game in one move - else choose random"""
            print('Making move level "medium"')
            for coords in self.empty_fields(self.board):
                x = coords[0]
                y = coords[1]

                horizontal = [self.board[coords[0]][0], self.board[coords[0]][1], self.board[coords[0]][2]]
                vertical = [self.board[0][coords[1]], self.board[1][coords[1]], self.board[2][coords[1]]]

                if horizontal.count("X") == 2 or horizontal.count("O") == 2:
                    self.move(x, y, mark)
                    break

                elif vertical.count("X") == 2 or vertical.count("O") == 2:
                    self.move(x, y, mark)
                    break
                # if x == y check main diagonal
                elif coords[0] == coords[1]:
                    diagonal1 = [self.board[0][0], self.board[1][1], self.board[2][2]]
                    if diagonal1.count("X") == 2 or diagonal1.count("O") == 2:
                        self.move(x, y, mark)
                        break
                # if x + y = 2 check secondary diagonal
                elif coords[0] + coords[1] == 2:
                    diagonal2 = [self.board[2][0], self.board[1][1], self.board[0][2]]
                    if diagonal2.count("X") == 2 or diagonal2.count("O") == 2:
                        self.move(x, y, mark)
                        break
            else:
                self.random_move(mark)

        elif player == "hard":
            """computer hard AI move with minmax algorithm"""
            print('Making move level "hard"')
            global ai, hu
            ai = mark
            hu = 'O' if mark == 'X' else 'X'

            depth = len(self.empty_fields(self.board))

            if depth == 9:
                self.random_move(mark)
            else:
                move = self.minimax(self.board, depth, mark)
                x, y = move[0], move[1]
                self.move(x, y, mark)

    def evaluate(self, state):
        if self.check_win(state, ai):
            score = +1
        elif self.check_win(state, hu):
            score = -1
        else:
            score = 0

        return score

    def minimax(self, state, depth, mark):
        if mark == ai:
            best = [-1, -1, -inf]
        else:
            best = [-1, -1, +inf]

        if depth == 0 or self.check_win(state, ai) or self.check_win(state, hu):
            score = self.evaluate(state)
            return [-1, -1, score]

        for cell in self.empty_fields(state):
            x, y = cell[0], cell[1]
            state[x][y] = mark
            score = self.minimax(state, depth - 1, self.opposite(mark))
            state[x][y] = " "
            score[0], score[1] = x, y

            if mark == ai:
                if score[2] > best[2]:
                    best = score  # max value
            else:
                if score[2] < best[2]:
                    best = score  # min value

        return best

    def random_move(self, mark):
        """Select random coords"""
        while True:
            x = random.randint(0, 2)
            y = random.randint(0, 2)
            if self.board[x][y] == " ":
                self.move(x, y, mark)
                break

    def move(self, x, y, mark):
        """Make move [x, y]"""
        self.board[x][y] = mark
        self.print_board()

    def empty_fields(self, state):
        """Return list of empty fields"""
        fields = []
        for i in range(3):
            for j in range(3):
                if state[i][j] == " ":
                    fields.append([i, j])

        return fields

    def opposite(self, ch):
        """Return opposite mark"""
        if ch == "X":
            return "O"
        else:
            return "X"

    def check_win(self, state, mark):
        """checks if the player has won"""
        win_combo = [
            [state[0][0], state[0][1], state[0][2]],
            [state[1][0], state[1][1], state[1][2]],
            [state[2][0], state[2][1], state[2][2]],
            [state[0][0], state[1][0], state[2][0]],
            [state[0][1], state[1][1], state[2][1]],
            [state[0][2], state[1][2], state[2][2]],
            [state[0][0], state[1][1], state[2][2]],
            [state[2][0], state[1][1], state[0][2]],
        ]
        if [mark, mark, mark] in win_combo:
            return True
        else:
            return False


def main():
    available_commands = ["user", "easy", "medium", "hard"]
    while True:
        menu = input("Input command: ").split()
        if menu[0] == "exit":
            exit()
        elif menu[0] == "start" and menu[1] in available_commands and menu[2] in available_commands:
            game = Game(menu[1], menu[2])
            game.play_game()
        else:
            print("Bad parameters!")


if __name__ == "__main__":
    main()
