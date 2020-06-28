import random


def print_field():
    """Print game board in table format"""
    print("---------")
    for element in field:
        print("| " + " ".join(element) + " |")  # '*' wyswietla liste bez [ , , ]
    print("---------")


def game_status():
    """Check if game is finished"""
    draw = True
    # check diagonal
    if field[0][0] == field[1][1] == field[2][2] != " " or field[0][2] == field[1][1] == field[2][0] != " ":
        print(field[1][1] + " wins")
        return True

    for element in field:
        # check rows
        if "O" not in element and " " not in element:
            print("X wins")
            return True
        elif "X" not in element and " " not in element:
            print("O wins")
            return True
        # if there is empty field game is continued
        elif " " in element:
            draw = False
    # if all fields are filled and no one wins, game is finished with draw
    if draw:
        print("Draw")
        return True
    else:
        return False


# create empty field
field = []
for i in range(3):
    field.append([])
    for j in range(3):
        field[i].append(" ")

print_field()

while True:
    try:
        x, y = [int(n) for n in input("Enter the coordinates: ").split()]
    except ValueError:
        print('You should enter numbers!')
        continue
    else:
        if 1 <= x <= 3 and 1 <= y <= 3:
            temp_x = x
            x = abs(y - 3)
            y = temp_x - 1
            if field[x][y] == " ":
                field[x][y] = "X"
                print_field()
                if game_status():
                    break
                # computer move
                print('Making move level "easy"')
                while True:
                    x = random.randint(0, 2)
                    y = random.randint(0, 2)
                    if field[x][y] == " ":
                        field[x][y] = "O"
                        print_field()
                        break

                if game_status():
                    break
            else:
                print("This cell is occupied! Choose another one!")
        else:
            print("Coordinates should be from 1 to 3!")