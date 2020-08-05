from math import inf
import random
from os import system
import platform


def opposite(ch):
    if ch == "X":
        return "O"
    else:
        return "X"


def game_status(state, mark):
    # # check if previous move caused a win on vertical line
    # if self.board[0][self.y] == self.board[1][self.y] == self.board[2][self.y]:
    #     print(mark + " wins")
    #     return True
    #
    # # check if previous move caused a win on horizontal line
    # if self.board[self.x][0] == self.board[self.x][1] == self.board[self.x][2]:
    #     print(mark + " wins")
    #     return True
    #
    # # check if previous move was on the main diagonal and caused a win
    # if self.x == self.y and self.board[0][0] == self.board[1][1] == self.board[2][2]:
    #     print(mark + " wins")
    #     return True
    #
    # # check if previous move was on the secondary diagonal and caused a win
    # if self.x + self.y == 2 and self.board[0][2] == self.board[1][1] == self.board[2][0]:
    #     print(mark + " wins")
    #     return True
    #
    # return False
    win_state = [
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],
        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[0][0], state[1][1], state[2][2]],
        [state[2][0], state[1][1], state[0][2]],
    ]
    if [mark, mark, mark] in win_state:
        return True
    else:
        return False


class Game:
    # coordinates of last move
    x = 0
    y = 0
    empty_fields = []

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
            if self.check_empty_fields(self.board):
                break
            if game_status(self.board, "X"):
                print("X wins")
                break

            self.choose_field(self.player2, "O")

            if self.check_empty_fields(self.board):
                break
            if game_status(self.board, "O"):
                print("O wins")
                break

        return True

    def choose_field(self, player, mark):
        if player == "user":
            """"Player move"""
            while True:
                try:
                    self.x, self.y = [int(n) for n in input("Enter the coordinates: ").split()]
                except ValueError:
                    print('You should enter numbers!')
                else:
                    if 1 <= self.x <= 3 and 1 <= self.y <= 3:
                        temp_x = self.x
                        self.x = abs(self.y - 3)
                        self.y = temp_x - 1
                        if self.board[self.x][self.y] == " ":
                            self.move(mark)
                            break
                        else:
                            print("This cell is occupied! Choose another one!")
                    else:
                        print("Coordinates should be from 1 to 3!")

        elif player == "easy":
            """computer AI easy move"""
            print('Making move level "easy"')
            self.random_move(mark)

        elif player == "medium":
            """computer AI medium move"""
            print('Making move level "medium"')
            for coords in self.empty_fields:
                self.x = coords[0]
                self.y = coords[1]

                # SET ZROBI TO SZYBCIEJ
                possible_wins = [
                    [self.board[self.x][0], self.board[self.x][1], self.board[self.x][2]],  # horizontal
                    [self.board[0][self.y], self.board[1][self.y], self.board[2][self.y]]  # vertical
                ]
                # diagonal1
                if self.x == self.y:
                    possible_wins.append([self.board[0][0], self.board[1][1], self.board[2][2]])
                # diagonal2
                if self.x + self.y == 2:
                    possible_wins.append([self.board[2][0], self.board[1][1], self.board[0][2]])

                for line in possible_wins:
                    if line.count("X") == 2 or line.count("O") == 2:
                        self.move(mark)
                        break

                # horizontal = [self.board[coords[0]][0], self.board[coords[0]][1], self.board[coords[0]][2]]
                # vertical = [self.board[0][coords[1]], self.board[1][coords[1]], self.board[2][coords[1]]]
                #
                # if horizontal.count("X") == 2 or horizontal.count("O") == 2:
                #     self.move(mark)
                #     break
                #
                # elif vertical.count("X") == 2 or vertical.count("O") == 2:
                #     self.move(mark)
                #     break
                # # if x == y check main diagonal
                # elif coords[0] == coords[1]:
                #     diagonal1 = [self.board[0][0], self.board[1][1], self.board[2][2]]
                #     if diagonal1.count("X") == 2 or diagonal1.count("O") == 2:
                #         self.move(mark)
                #         break
                # # if x + y = 2 check secondary diagonal
                # elif coords[0] + coords[1] == 2:
                #     diagonal2 = [self.board[2][0], self.board[1][1], self.board[0][2]]
                #     if diagonal2.count("X") == 2 or diagonal2.count("O") == 2:
                #         self.move(mark)
                #         break
            else:
                self.random_move(mark)
                
        elif player == "hard":
            print('Making move level "hard"')
            global ai, hu
            ai = mark
            hu = 'O' if mark == 'X' else 'X'

            depth = len(self.empty_fields)
            # or self.game_over(self.board)

            if depth == 9:
                self.random_move(mark)
            else:
                move = self.minimax(self.board, depth, mark)
                self.x, self.y = move[0], move[1]
                self.move(mark)


    # def mini_max(self, player):
    #     if game_status(hu):
    #         return -10, None
    #     elif game_status(ai):
    #         return 10, None
    #     elif len(self.empty_fields) == 0:
    #         return 0, None
    #
    #     moves = []
    #     for cell in self.empty_fields:
    #         x, y = cell[0], cell[1]
    #         self.board[x][y] = player
    #         res = self.mini_max(hu) if player == ai else self.mini_max(ai)
    #         move = (res[0])
    #         self.board[x][y] = ' '
    #
    #     moves.append(move)
    #
    #     return min(moves) if player == hu else max(moves)





    def evaluate(self, state):
        """
        Function to heuristic evaluation of state.
        :param state: the state of the current board
        :return: +1 if the computer wins; -1 if the human wins; 0 draw
        """
        if game_status(state, ai):
            score = +1
        elif game_status(state, hu):
            score = -1
        else:
            score = 0

        return score

    def minimax(self, state, depth, mark):
        """
        AI function that choice the best move
        :param mark:
        :param state: current state of the board
        :param depth: node index in the tree (0 <= depth <= 9),
        but never nine in this case (see iaturn() function)
        :return: a list with [the best row, best col, best score]
        """
        if mark == ai:
            best = [-1, -1, -inf]
        else:
            best = [-1, -1, +inf]

        if depth == 0 or game_status(state, ai) or game_status(state, hu):
            score = self.evaluate(state)
            return [-1, -1, score]

        #self.check_empty_fields(state)
        self.check_empty_fields(state)
        for cell in self.empty_fields:
            x, y = cell[0], cell[1]
            state[x][y] = mark
            score = self.minimax(state, depth - 1, opposite(mark))
            state[x][y] = " "
            score[0], score[1] = x, y

            if mark == ai:
                if score[2] > best[2]:
                    best = score  # max value
            else:
                if score[2] < best[2]:
                    best = score  # min value
            self.check_empty_fields(state)

        return best


    def random_move(self, mark):
        while True:
            self.x = random.randint(0, 2)
            self.y = random.randint(0, 2)
            if self.board[self.x][self.y] == " ":
                self.move(mark)
                break

    def move(self, mark):
        self.board[self.x][self.y] = mark
        self.print_board()

    def check_empty_fields(self, state):
        self.empty_fields.clear()
        for i in range(3):
            for j in range(3):
                if state[i][j] == " ":
                    self.empty_fields.append([i, j])
        # check for draw
        if len(self.empty_fields) == 0:
            print("Draw")
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