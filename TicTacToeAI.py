import random


class Game:
    # coordinates of last move
    x = 0
    y = 0

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        # create empty field
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
        while True:
            self.make_move(self.player1, "X")
            if self.game_status("X"):
                break
            self.make_move(self.player2, "O")
            if self.game_status("O"):
                break
        return True

    def make_move(self, player, mark):
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
                            self.board[self.x][self.y] = mark
                            self.print_board()
                            break
                        else:
                            print("This cell is occupied! Choose another one!")
                    else:
                        print("Coordinates should be from 1 to 3!")

        else:
            """computer AI easy move"""
            print('Making move level "easy"')
            while True:
                self.x = random.randint(0, 2)
                self.y = random.randint(0, 2)
                if self.board[self.x][self.y] == " ":
                    self.board[self.x][self.y] = mark
                    self.print_board()
                    break

    def game_status(self, mark):
        draw = True
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

        # check for " " in the board, if there is no " " = draw
        for x in self.board:
            if " " in x:
                draw = False

        if draw:
            print("Draw")
            return True
        else:
            return False


def main():
    while True:
        menu = input("Input command: ").split()
        if menu[0] == "exit":
            exit()
        elif menu[0] == "start" and (menu[1] == "easy" or menu[1] == "user") and (menu[2] == "easy" or menu[2] == "user"):
            game = Game(menu[1], menu[2])
            game.play_game()
        else:
            print("Bad parameters!")


if __name__ == "__main__":
    main()