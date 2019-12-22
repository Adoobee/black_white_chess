print(chr(0x25cb))
print(chr(0x25cf))
print(chr(0x2640))
print(chr(0x2642))
#line = [0 for i in range(0,10)]


def PrintBoard(line, n):
    if (n % 2 == 1):
        n = n - 1 + 2
    else:
        n += 2
    line1 = [[0 for i in range(0, n)] for i in range(0, n)]
    for i in range(0, n):
        for j in range(0, n):
            if (line[i][j] == 1):
                line1[i][j] = 0x25cf
            elif (line[i][j] == -1):
                line1[i][j] = 0x25cb
            elif (line[i][j] == 0):
                line1[i][j] = 0x2219
            '''
            else:
                line1[i][j] = 0x0021'''
    for i in range(1, n - 1):
        print(
            ''.join([chr(line1[i][j]) + ' ' for j in range(1, n - 1)]) + str(i))
    for i in range(1, n - 1):
        if (i < 10):
            print(str(i) + ' ', end='')
        else:
            print(str(i) + '', end='')
    print()
    countblack = 0
    countwhite = 0
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if (board[i][j] == 1):
                countblack += 1
            elif (board[i][j] == -1):
                countwhite += 1
    print('黑色棋子数：', countblack)
    print('白色棋子数：', countwhite)
    pass


def InitBoard(n):
    if (n % 2 == 1):
        n = n - 1 + 2
    else:
        n += 2
    board = [[0 for i in range(0, n)] for i in range(0, n)]
    board[int(n / 2 - 1)][int(n / 2 - 1)] = 1
    board[int(n / 2 - 1)][int(n / 2)] = -1
    board[int(n / 2)][int(n / 2 - 1)] = -1
    board[int(n / 2)][int(n / 2)] = 1
    return board
    pass


def BlackChangeBoard(board, able, line, row):
    i = 1
    flag = 0
    if (able):
        board[line][row] = 1
        while(True):
            if (board[line][row - i] == 1):
                if (flag > 0):
                    for j in range(1, i):
                        board[line][row - j] = 1
                    i = 1
                    flag = 0
                    break
                else:
                    i = 1
                    flag = 0
                    break
            elif (board[line][row - i] == 0):
                i = 1
                flag = 0
                break
            else:
                flag += 1
            i += 1
        while(True):
            if (board[line - i][row - i] == 1):
                if (flag > 0):
                    for j in range(1, i):
                        board[line - j][row - j] = 1
                    i = 1
                    flag = 0
                    break
                else:
                    i = 1
                    flag = 0
                    break
            elif (board[line - i][row - i] == 0):
                i = 1
                flag = 0
                break
            else:
                flag += 1
            i += 1
        while(True):
            if (board[line - i][row] == 1):
                if (flag > 0):
                    for j in range(1, i):
                        board[line - j][row] = 1
                    i = 1
                    flag = 0
                    break
                else:
                    i = 1
                    flag = 0
                    break
            elif (board[line - i][row] == 0):
                i = 1
                flag = 0
                break
            else:
                flag += 1
            i += 1
        while(True):
            if (board[line - i][row + i] == 1):
                if (flag > 0):
                    for j in range(1, i):
                        board[line - j][row + j] = 1
                    i = 1
                    flag = 0
                    break
                else:
                    i = 1
                    flag = 0
                    break
            elif (board[line - i][row + i] == 0):
                i = 1
                flag = 0
                break
            else:
                flag += 1
            i += 1
        while(True):
            if (board[line][row + i] == 1):
                if (flag > 0):
                    for j in range(1, i):
                        board[line][row + j] = 1
                    i = 1
                    flag = 0
                    break
                else:
                    i = 1
                    flag = 0
                    break
            elif (board[line][row + i] == 0):
                i = 1
                flag = 0
                break
            else:
                flag += 1
            i += 1
        while(True):
            if (board[line + i][row + i] == 1):
                if (flag > 0):
                    for j in range(1, i):
                        board[line + j][row + j] = 1
                    i = 1
                    flag = 0
                    break
                else:
                    i = 1
                    flag = 0
                    break
            elif (board[line + i][row + i] == 0):
                i = 1
                flag = 0
                break
            else:
                flag += 1
            i += 1
        while(True):
            if (board[line + i][row] == 1):
                if (flag > 0):
                    for j in range(1, i):
                        board[line + j][row] = 1
                    i = 1
                    flag = 0
                    break
                else:
                    i = 1
                    flag = 0
                    break
            elif (board[line + i][row] == 0):
                i = 1
                flag = 0
                break
            else:
                flag += 1
            i += 1
        while(True):
            if (board[line + i][row - i] == 1):
                if (flag > 0):
                    for j in range(1, i):
                        board[line + j][row - j] = 1
                    i = 1
                    flag = 0
                    break
                else:
                    i = 1
                    flag = 0
                    break
            elif (board[line + i][row - i] == 0):
                i = 1
                flag = 0
                break
            else:
                flag += 1
            i += 1
    else:
        print('不可以下在这里~\n')
    pass


def WhiteChangeBoard(board, able, line, row):
    i = 1
    flag = 0
    if (able):
        board[line][row] = -1
        while(True):
            if (board[line][row - i] == -1):
                if (flag > 0):
                    for j in range(1, i):
                        board[line][row - j] = -1
                    i = 1
                    flag = 0
                    break
                else:
                    i = 1
                    flag = 0
                    break
            elif (board[line][row - i] == 0):
                i = 1
                flag = 0
                break
            else:
                flag += 1
            i += 1
        while(True):
            if (board[line - i][row - i] == -1):
                if (flag > 0):
                    for j in range(1, i):
                        board[line - j][row - j] = -1
                    i = 1
                    flag = 0
                    break
                else:
                    i = 1
                    flag = 0
                    break
            elif (board[line - i][row - i] == 0):
                i = 1
                flag = 0
                break
            else:
                flag += 1
            i += 1
        while(True):
            if (board[line - i][row] == -1):
                if (flag > 0):
                    for j in range(1, i):
                        board[line - j][row] = -1
                    i = 1
                    flag = 0
                    break
                else:
                    i = 1
                    flag = 0
                    break
            elif (board[line - i][row] == 0):
                i = 1
                flag = 0
                break
            else:
                flag += 1
            i += 1
        while(True):
            if (board[line - i][row + i] == -1):
                if (flag > 0):
                    for j in range(1, i):
                        board[line - j][row + j] = -1
                    i = 1
                    flag = 0
                    break
                else:
                    i = 1
                    flag = 0
                    break
            elif (board[line - i][row + i] == 0):
                i = 1
                flag = 0
                break
            else:
                flag += 1
            i += 1
        while(True):
            if (board[line][row + i] == -1):
                if (flag > 0):
                    for j in range(1, i):
                        board[line][row + j] = -1
                    i = 1
                    flag = 0
                    break
                else:
                    i = 1
                    flag = 0
                    break
            elif (board[line][row + i] == 0):
                i = 1
                flag = 0
                break
            else:
                flag += 1
            i += 1
        while(True):
            if (board[line + i][row + i] == -1):
                if (flag > 0):
                    for j in range(1, i):
                        board[line + j][row + j] = -1
                    i = 1
                    flag = 0
                    break
                else:
                    i = 1
                    flag = 0
                    break
            elif (board[line + i][row + i] == 0):
                i = 1
                flag = 0
                break
            else:
                flag += 1
            i += 1
        while(True):
            if (board[line + i][row] == -1):
                if (flag > 0):
                    for j in range(1, i):
                        board[line + j][row] = -1
                    i = 1
                    flag = 0
                    break
                else:
                    i = 1
                    flag = 0
                    break
            elif (board[line + i][row] == 0):
                i = 1
                flag = 0
                break
            else:
                flag += 1
            i += 1
        while(True):
            if (board[line + i][row - i] == -1):
                if (flag > 0):
                    for j in range(1, i):
                        board[line + j][row - j] = -1
                    i = 1
                    flag = 0
                    break
                else:
                    i = 1
                    flag = 0
                    break
            elif (board[line + i][row - i] == 0):
                i = 1
                flag = 0
                break
            else:
                flag += 1
            i += 1
    else:
        print('不可以下在这里~\n')
    pass


def CheckBlack(board, line, row):
    able = False
    i = 1
    flag = 0
    if (board[line][row] != 0):
        return able
    while(True):
        if (board[line][row - i] == 1):
            if (flag > 0):
                i = 1
                flag = 0
                able = True
                break
            else:
                i = 1
                flag = 0
                able = False
                break
        elif (board[line][row - i] == 0):
            i = 1
            flag = 0
            able = False
            break
        else:
            flag += 1
        i += 1
    if (able == True):
        return able
    while(True):
        if (board[line - i][row - i] == 1):
            if (flag > 0):
                i = 1
                flag = 0
                able = True
                break
            else:
                i = 1
                flag = 0
                able = False
                break
        elif (board[line - i][row - i] == 0):
            i = 1
            flag = 0
            able = False
            break
        else:
            flag += 1
        i += 1
    if (able == True):
        return able
    while(True):
        if (board[line - i][row] == 1):
            if (flag > 0):
                i = 1
                flag = 0
                able = True
                break
            else:
                i = 1
                flag = 0
                able = False
                break
        elif (board[line - i][row] == 0):
            i = 1
            flag = 0
            able = False
            break
        else:
            flag += 1
        i += 1
    if (able == True):
        return able
    while(True):
        if (board[line - i][row + i] == 1):
            if (flag > 0):
                i = 1
                flag = 0
                able = True
                break
            else:
                i = 1
                flag = 0
                able = False
                break
        elif (board[line - i][row + i] == 0):
            i = 1
            flag = 0
            able = False
            break
        else:
            flag += 1
        i += 1
    if (able == True):
        return able
    while(True):
        if (board[line][row + i] == 1):
            if (flag > 0):
                i = 1
                flag = 0
                able = True
                break
            else:
                i = 1
                flag = 0
                able = False
                break
        elif (board[line][row + i] == 0):
            i = 1
            flag = 0
            able = False
            break
        else:
            flag += 1
        i += 1
    if (able == True):
        return able
    while(True):
        if (board[line + i][row + i] == 1):
            if (flag > 0):
                i = 1
                flag = 0
                able = True
                break
            else:
                i = 1
                flag = 0
                able = False
                break
        elif (board[line + i][row + i] == 0):
            i = 1
            flag = 0
            able = False
            break
        else:
            flag += 1
        i += 1
    if (able == True):
        return able
    while(True):
        if (board[line + i][row] == 1):
            if (flag > 0):
                i = 1
                flag = 0
                able = True
                break
            else:
                i = 1
                flag = 0
                able = False
                break
        elif (board[line + i][row] == 0):
            i = 1
            flag = 0
            able = False
            break
        else:
            flag += 1
        i += 1
    if (able == True):
        return able
    while(True):
        if (board[line + i][row - i] == 1):
            if (flag > 0):
                i = 1
                flag = 0
                able = True
                break
            else:
                i = 1
                flag = 0
                able = False
                break
        elif (board[line + i][row - i] == 0):
            i = 1
            flag = 0
            able = False
            break
        else:
            flag += 1
        i += 1
    if (able == True):
        return able
    return able
    pass


def CheckWhite(board, line, row):
    able = False
    i = 1
    flag = 0
    if (board[line][row] != 0):
        return able
    while(True):
        if (board[line][row - i] == -1):
            if (flag > 0):
                i = 1
                flag = 0
                able = True
                break
            else:
                i = 1
                flag = 0
                able = False
                break
        elif (board[line][row - i] == 0):
            i = 1
            flag = 0
            able = False
            break
        else:
            flag += 1
        i += 1
    if (able == True):
        return able
    while(True):
        if (board[line - i][row - i] == -1):
            if (flag > 0):
                i = 1
                flag = 0
                able = True
                break
            else:
                i = 1
                flag = 0
                able = False
                break
        elif (board[line - i][row - i] == 0):
            i = 1
            flag = 0
            able = False
            break
        else:
            flag += 1
        i += 1
    if (able == True):
        return able
    while(True):
        if (board[line - i][row] == -1):
            if (flag > 0):
                i = 1
                flag = 0
                able = True
                break
            else:
                i = 1
                flag = 0
                able = False
                break
        elif (board[line - i][row] == 0):
            i = 1
            flag = 0
            able = False
            break
        else:
            flag += 1
        i += 1
    if (able == True):
        return able
    while(True):
        if (board[line - i][row + i] == -1):
            if (flag > 0):
                i = 1
                flag = 0
                able = True
                break
            else:
                i = 1
                flag = 0
                able = False
                break
        elif (board[line - i][row + i] == 0):
            i = 1
            flag = 0
            able = False
            break
        else:
            flag += 1
        i += 1
    if (able == True):
        return able
    while(True):
        if (board[line][row + i] == -1):
            if (flag > 0):
                i = 1
                flag = 0
                able = True
                break
            else:
                i = 1
                flag = 0
                able = False
                break
        elif (board[line][row + i] == 0):
            i = 1
            flag = 0
            able = False
            break
        else:
            flag += 1
        i += 1
    if (able == True):
        return able
    while(True):
        if (board[line + i][row + i] == -1):
            if (flag > 0):
                i = 1
                flag = 0
                able = True
                break
            else:
                i = 1
                flag = 0
                able = False
                break
        elif (board[line + i][row + i] == 0):
            i = 1
            flag = 0
            able = False
            break
        else:
            flag += 1
        i += 1
    if (able == True):
        return able
    while(True):
        if (board[line + i][row] == -1):
            if (flag > 0):
                i = 1
                flag = 0
                able = True
                break
            else:
                i = 1
                flag = 0
                able = False
                break
        elif (board[line + i][row] == 0):
            i = 1
            flag = 0
            able = False
            break
        else:
            flag += 1
        i += 1
    if (able == True):
        return able
    while(True):
        if (board[line + i][row - i] == -1):
            if (flag > 0):
                i = 1
                flag = 0
                able = True
                break
            else:
                i = 1
                flag = 0
                able = False
                break
        elif (board[line + i][row - i] == 0):
            i = 1
            flag = 0
            able = False
            break
        else:
            flag += 1
        i += 1
    if (able == True):
        return able
    return able
    pass


n = int(input("请输入棋盘大小："))
board = InitBoard(n)
PrintBoard(board, n)
player = 1
while(True):
    giveup = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            tips = CheckBlack(board, i, j)
            if (tips):
                giveup += 1
    if (giveup == 0):
        player = 0

    if (player == 1):
        line = input('请输入黑方行数：')
        while not line.isdigit():
            line = input('请输入数字：')
        line = int(line)
        if (line > n):
            line = n
        if (line < 0):
            line = 0
        row = input('请输入黑方列数：')
        while not row.isdigit():
            row = input('请输入数字：')
        row = int(row)
        if (row > n):
            row = n
        if (row < 0):
            row = 0

        able = CheckBlack(board, line, row)
        BlackChangeBoard(board, able, line, row)
        if able:
            PrintBoard(board, n)
            player = 0
        else:
            player = 1

    giveup = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            tips = CheckBlack(board, i, j)
            if (tips):
                giveup += 1
    if (giveup == 0):
        player = 1

    if (player == 0):
        '''
        for i in range(1,n+1):
            for j in range(1,n+1):
                tips = CheckWhite(board,i,j)
                if (tips):board[i][j]=2
        PrintBoard(board,n)
        for i in range(1,n+1):
            for j in range(1,n+1):
                if (board[i][j]==2):board[i][j]==0
        '''
        line = input('请输入白方行数：')
        while not line.isdigit():
            line = input('请输入数字：')
        line = int(line)
        if (line > n):
            line = n
        if (line < 0):
            line = 0
        row = input('请输入白方列数：')
        while not row.isdigit():
            row = input('请输入数字：')
        row = int(row)
        if (row > n):
            row = n
        if (row < 0):
            row = 0
        able = CheckWhite(board, line, row)
        WhiteChangeBoard(board, able, line, row)
        if able:
            PrintBoard(board, n)
            player = 1
        else:
            player = 0
