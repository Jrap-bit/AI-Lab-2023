s = [" " for x in range(9)]

board = [
    [s[0], s[1], s[2]],
    [s[3], s[4], s[5]],
    [s[6], s[7], s[8]]
]


def display():
    print("-" * 15)
    print(f' | ' + board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2] + ' | ')
    print("-" * 15)
    print(f' | ' + board[1][0] + ' | ' + board[1][1] + ' | ' + board[1][2] + ' | ')
    print("-" * 15)
    print(f' | ' + board[2][0] + ' | ' + board[2][1] + ' | ' + board[2][2] + ' | ')
    print("-" * 15)


def strength():
    print('Your Input Currently is: ')
    display()
    dom_x = 0
    dom_o = 0
    num_x_L = 0
    num_o_L = 0
    num_x_R = 0
    num_o_R = 0
    for i in range(3):
        num_x_Rows = 0
        num_o_Rows = 0
        num_x_Columns = 0
        num_o_Columns = 0
        for j in range(3):  # Rows
            if board[i][j] == 'X':
                num_x_Rows += 1
            elif board[i][j] == 'O':
                num_o_Rows += 1

            if board[j][i] == 'X':  # Columns
                num_x_Columns += 1
            elif board[j][i] == 'O':
                num_o_Columns += 1

            if i == j:  # Left Diagonal
                if board[i][j] == 'X':
                    num_x_L += 1
                elif board[i][j] == 'O':
                    num_o_L += 1

            if (i + j) == 2:  # Right Diagonal
                if board[i][j] == 'X':
                    num_x_R += 1
                elif board[i][j] == 'O':
                    num_o_R += 1

        if num_x_Rows == 0:
            dom_o += num_o_Rows
        elif num_o_Rows == 0:
            dom_x += num_x_Rows
        if num_x_Columns == 0:
            dom_o += num_o_Columns
        elif num_o_Columns == 0:
            dom_x += num_x_Columns

    if num_x_L == 0:
        dom_o += num_o_L
    elif num_o_L == 0:
        dom_x += num_x_L

    if num_x_R == 0:
        dom_o += num_o_R
    elif num_o_R == 0:
        dom_x += num_x_R

    print("Total Domination of X: {}".format(dom_x))
    print("Total Domination of O: {}".format(dom_o))
    print("Strength of X: {}".format(dom_x - dom_o))
    print("Strength of O: {}".format(dom_o - dom_x))


done = False
count = 0
while not done:
    coordinates = input("Enter the Coordinates or Enter 'check' to get the strength: ")
    if coordinates == 'check':
        strength()
        done = True
        break
    elif len(coordinates) != 3:
        print("Enter exactly two coordinates")
    else:
        x, y = coordinates.split(" ")
        print(y)
        if not x.isdigit or not y.isdigit:
            print("Please Enter Digits Only")
        elif int(x) < 1 or int(x) > 3 or int(y) < 1 or int(y) > 3:
            print("Enter Coordinates between 1 and 3")
        else:
            x = int(x)
            y = int(y)
            if count % 2 == 0:
                board[x - 1][y - 1] = 'X'
            else:
                board[x - 1][y - 1] = 'O'
            count += 1
            display()
        if count == 9:
            strength()