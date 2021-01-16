#The following file is a practice file composed just to remind myself the very basics of Python syntax and it's practices.
#The code is a little game of submarines that works with I/O and two-dimensional arrays
#16.1.2021, COVID-19 lockdown, Jakub Phan, FIT VUT 2nd semester


#function that draws matrix of n cols and m rows
def matrix_draw(n, m):
    print("Currently printing matrix of " + str(n) + " colums and " + str(m) + " rows\n")
    for i in range(m):
        print("|", end="")
        for j in range(n):
            print("x|", end="")
        print("") #the end of row
    return

#Function that draws the gaming board
def draw_board(board):
    for item in board:
        print(item)
    return

#Initializes game board (two dimensional array of strings)
def make_board(n, m):
    board = []
    for i in range(int(n)):
        tmp = []
        for j in range(int(m)):
            tmp.append(" 0 ")
        board.append(tmp)
    return board

#Function that lets user place a ship in the board
def place(board):
    left = len(board)
    print("You can now place " + str(left) + " ships")
    while (left != 0):
        print("Please select where you want to place a ship:")
        print("col: ")
        n = input()
        print("row: ")
        m = input()
        if (str.isnumeric(n) and str.isnumeric(m) and int(n) < len(board)+1 and int(m) < len(board)+1):
            check = isvalid(board, n, m)
            if check == False:
                print("This place is already taken, please choose another one")
            else:
                board[int(m)-1][int(n)-1] = " X "
                left-=1
                draw_board(board)
        else:
            print("You entered something wrong, please try again")   
    return

#Function that checks if a box is free to be placed upon
def isvalid(board, req_n, req_m):
    if board[int(req_m)-1][int(req_n)-1] != " 0 ":
        return False
    else:
        return True

#The main body of the game
def play():
    print("Welcome, to submarines. Please select size of the play-board (4-10): ")
    size = input()
    if (str.isnumeric(size) and int(size) > 3 and int(size) < 11):
        board = make_board(size, size)
    print("This is the selected default gaming board.")
    draw_board(board)
    place(board)
    return

play()