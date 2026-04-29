import random
import os
import platform


MINE = "💣"
HIDDEN = "♦"
EXPOSED = "v"


def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def make_grid(height, width, fill):
    return [[fill for _ in range(width)] for _ in range(height)]


def print_board(board, visible):
    clear_screen()

    height = len(board)
    width = len(board[0])

    print("   ", end="")
    for col in range(width):
        print(f"{col:2d}", end="  ")
    print()

    print("    " + "- - -" + " - - " * (width - 1))

    for row in range(height):
        print(row, end=" | ")

        for col in range(width):
            if visible[row][col] == HIDDEN:
                print(HIDDEN, end=" | ")
            elif visible[row][col] == MINE:
                print(MINE, end=" | ")
            else:
                value = board[row][col]
                if value == 0:
                    print(" ", end=" | ")
                else:
                    print(value, end=" | ")

        print()
        print("    " + "- - -" + " - - " * (width - 1))


def get_setup():
    while True:
        try:
            height = int(input("\nBoard height (2 - 10) : "))
            while height < 1 or height > 10:
                height = int(input("Please enter board height (2 -10) : "))
            break
        except ValueError:
            print("You must enter an integer (2 - 10) : ")

    while True:
        try:
            width = int(input("Board width (2 - 10) : "))
            while width < 1 or width > 10:
                width = int(input("Please enter board width (2 -10) : "))
            break
        except ValueError:
            print("You must enter an integer (2 - 10)")

    total_cells = height * width

    while True:
        try:
            mines = int(input(f"How many mines (less then {total_cells}) : "))
            while mines < 0 or mines >= total_cells:
                mines = int(input("Invalid number of mines, please re-enter : )"))
            break
        except ValueError:
            print("You must enter a whole number")

    return height, width, mines


def plant_mines(board, mines):
    height = len(board)
    width = len(board[0])

    planted = 0
    while planted < mines:
        row = random.randrange(height)
        col = random.randrange(width)

        if board[row][col] != MINE:
            board[row][col] = MINE
            planted += 1


def is_on_board(board, row, col):
    return 0 <= row < len(board) and 0 <= col < len(board[0])


def is_mine(board, row, col):
    return board[row][col] == MINE


def fill_numbers(board):
    height = len(board)
    width = len(board[0])

    for row in range(height):
        for col in range(width):
            if board[row][col] == MINE:
                continue

            count = 0

            for r in range(row - 1, row + 2):
                for c in range(col - 1, col + 2):
                    if is_on_board(board, r, c) and is_mine(board, r, c):
                        count += 1

            board[row][col] = count


def all_safe_cells_exposed(board, visible):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] != MINE and visible[row][col] == HIDDEN:
                return False
    return True


def expose_cell(board, visible, row, col):
    if not is_on_board(board, row, col):
        return

    if visible[row][col] != HIDDEN:
        return

    visible[row][col] = EXPOSED

    if board[row][col] != 0:
        return

    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if is_on_board(board, r, c):
                if board[r][c] != MINE and visible[r][c] == HIDDEN:
                    expose_cell(board, visible, r, c)


def reveal_full_board(board, visible):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == MINE:
                visible[row][col] = MINE
            else:
                visible[row][col] = EXPOSED


def get_move(width, height):
    while True:
        try:
            over = int(input("\nHow many over would you like to dig? : "))
            while over < 0 or over >= width:
                over = int(input(f"please enter an integer between 0 and {width - 1} : "))
            break
        except ValueError:
            print("pleasse enter a valid integer : ")

    while True:
        try:
            down = int(input("How many down would you like to dig? : "))
            while down < 0 or down >= height:
                down = int(input(f"please enter an integer between 0 and {height - 1} : "))
            break
        except ValueError:
            print("pleasse enter a valid integer : ")

    return down, over


def play_game():
    while True:
        height, width, mines = get_setup()

        board = make_grid(height, width, 0)
        visible = make_grid(height, width, HIDDEN)

        plant_mines(board, mines)
        fill_numbers(board)

        while True:
            print_board(board, visible)

            row, col = get_move(width, height)

            if visible[row][col] != HIDDEN:
                print("That cell already exposed! Try again")
                continue

            if board[row][col] == MINE:
                reveal_full_board(board, visible)
                print_board(board, visible)
                return

            expose_cell(board, visible, row, col)

            if all_safe_cells_exposed(board, visible):
                print_board(board, visible)
                print("Congratulations! You won.")
                return


play_game()