def new_playground(height, width):
    playground = []
    for i in range(height):
        playground.append([])
    return playground


def get(playground, row, col):
    return playground[row][col]


def drop(playground, col, symbol):
    if playground[0][col] != " ":
        return False
    else:
        for i in range(1, len(playground)):
            if playground[i][col] != " ":
                playground[i - 1][col] = symbol
                return playground
        playground[len(playground) - 1][col] = symbol
        return playground


def draw(playground):
    size_rows = len(playground[0])
    print("     ", end="")  # header
    for i in range(size_rows):
        print(str(chr(65 + i)), end="   ")
    print()
    for j in range(len(playground)):  # rows
        print("   +" + "---+" * size_rows)  # lines between rows
        if j < 10:
            print(" " + str(j), end=" |")  # single digit number of rows
        else:
            print(j, end=" |")  # double digit number of rows
        for k in range(size_rows):  # elements of a row
            print(" " + playground[j][k], end=" |")
        print()
    print("   +" + "---+" * size_rows)  # last line.


def who_won(playground):
    for i in range(len(playground)):
        for j in range(len(playground[0]) - 3):
            if (playground[i][0 + j] != " ") and ([i][0 + j] == playground[i][1 + j] == playground[i][2 + j] == playground[i][3 + j]):
                return True


who_won([[" ", " ", "x", "x", "x", "x"], [" ", " ", " ", "x", "o", "x"], ["x", "o", " ", "x", "o", "x"]])
