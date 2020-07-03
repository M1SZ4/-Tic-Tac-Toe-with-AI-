import random


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
            if self.check_empty_fields() or self.game_status("X"):
                break

            self.choose_field(self.player2, "O")
            if self.check_empty_fields() or self.game_status("O"):
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
                horizontal = [self.board[coords[0]][0], self.board[coords[0]][1], self.board[coords[0]][2]]
                vertical = [self.board[0][coords[1]], self.board[1][coords[1]], self.board[2][coords[1]]]

                if horizontal.count("X") == 2 or horizontal.count("O") == 2:
                    self.move(mark)
                    break

                elif vertical.count("X") == 2 or vertical.count("O") == 2:
                    self.move(mark)
                    break
                # if x == y check main diagonal
                elif coords[0] == coords[1]:
                    diagonal1 = [self.board[0][0], self.board[1][1], self.board[2][2]]
                    if diagonal1.count("X") == 2 or diagonal1.count("O") == 2:
                        self.move(mark)
                        break
                # if x + y = 2 check secondary diagonal
                elif coords[0] + coords[1] == 2:
                    diagonal2 = [self.board[2][0], self.board[1][1], self.board[0][2]]
                    if diagonal2.count("X") == 2 or diagonal2.count("O") == 2:
                        self.move(mark)
                        break
            else:
                self.random_move(mark)

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

    def check_empty_fields(self):
        self.empty_fields.clear()
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    self.empty_fields.append([i, j])
        # check for draw
        if len(self.empty_fields) == 0:
            print("Draw")
            return True
        else:
            return False

    def game_status(self, mark):
        # check if previous move caused a win on vertical line
        if self.board[0][self.y] == self.board[1][self.y] == self.board[2][self.y]:
            print(mark + " wins")
            return True

        # check if previous move caused a win on horizontal line
        if self.board[self.x][0] == self.board[self.x][1] == self.board[self.x][2]:
            print(mark + " wins")
            return True

        # check if previous move was on the main diagonal and caused a win
        if self.x == self.y and self.board[0][0] == self.board[1][1] == self.board[2][2]:
            print(mark + " wins")
            return True

        # check if previous move was on the secondary diagonal and caused a win
        if self.x + self.y == 2 and self.board[0][2] == self.board[1][1] == self.board[2][0]:
            print(mark + " wins")
            return True

        return False


def main():
    available_commands = ["user", "easy", "medium"]
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