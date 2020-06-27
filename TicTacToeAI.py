def print_field():
    """Print game board in table format"""
    print("---------")
    for element in field:
        print("| " + " ".join(element) + " |")  # '*' wyswietla liste bez [ , , ]
    print("---------")


def game_status():
    """Check if game is finished"""
    not_finished = False
    # sprawdza po przekatnej
    if field[0][0] == field[1][1] == field[2][2] or field[0][2] == field[1][1] == field[2][0]:
        print(field[1][1] + " wins")
        return True

    for element in field:
        # sprawdza wiersze
        if "O" not in element and " " not in element:
            print("X wins")
            return True
        elif "X" not in element and " " not in element:
            print("O wins")
            return True
        # jezeli jest puste pole gra sie nie konczy
        elif " " in element:
            not_finished = True
    # jezeli nie ma pustego pola to remis
    if not_finished:
        print("Game not finished")
        return False
    else:
        print("Draw")
        return True


def set_start_symbol():
    """Set start symbol"""
    if initial_sheet.count("X") > initial_sheet.count("O"):
        return "O"
    else:
        return "X"


initial_sheet = input("Enter cells: ")
initial_sheet = initial_sheet.replace("_", " ")
sheet_list = list(initial_sheet)

# mozna to zrobic lepiej
field = []
field.append(sheet_list[:3])
field.append(sheet_list[3:6])
field.append(sheet_list[6:])

print_field()
symbol = set_start_symbol()

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
                field[x][y] = symbol
                print_field()
                if game_status():
                    break
                # limit dla 1 podpunktu zeby wykonac aby 1 ruch
                break
            else:
                print("This cell is occupied! Choose another one!")
        else:
            print("Coordinates should be from 1 to 3!")