rows = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
current = 'X'
count = 0
game_on = True


def print_board():
    if game_on:
        print(f'\nPlayer {current}')
    print('=======\n')
    for row in reversed(rows):
        print(row)


def valid_check(x, y):
    if -1 < x < 3 and -1 < y < 3:
        if rows[y][x] == '-':
            return True
        else:
            print('space taken')
    else:
        print('input between 0 and 2')


def win_check():
    big_list = [rows[0], rows[1], rows[2]]
    for i in range(3):
        col = []
        for j in range(3):
            col.append(rows[j][i])
        big_list.append(col)

    diag_1 = [rows[2][2], rows[1][1], rows[0][0]]
    diag_2 = [rows[2][0], rows[1][1], rows[0][2]]
    big_list.append(diag_1)
    big_list.append(diag_2)

    for triplet in big_list:
        if triplet.count('X') == 3 or triplet.count('O') == 3:
            print(f'\n{current} has wonnered!!')
            return True
        elif count == 9:
            print('\nA flippin draw!')
            return True


while game_on:
    print_board()
    x_coord = int(input('Input x coordinate:\n'))
    y_coord = int(input('Input y coordinate:\n'))

    if valid_check(x_coord, y_coord):
        rows[y_coord][x_coord] = current
        count += 1
        if win_check():
            game_on = False
            print_board()
            break

        if current == 'X':
            current = 'O'
        else:
            current = 'X'
