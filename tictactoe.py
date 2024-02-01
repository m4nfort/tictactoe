
board = [' ' for _ in range(9)]


def display_board():
    for i in range(3):
        row = '|'.join(board[i*3:(i+1)*3])
        print(row)
        if i < 2:
            print('-'*5)


def place_symbol(position, symbol):
    board[position] = symbol


def check_win(symbol):

    return (any(all(board[i] == symbol for i in line) for line in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]))


def tic_tac_toe():
    current_symbol = 'X'
    while ' ' in board:
        display_board()
        position = int(input(f'Игрок {current_symbol}, введите позицию (0-8): '))
        if board[position] == ' ':
            place_symbol(position, current_symbol)
            if check_win(current_symbol):
                display_board()
                print(f'Игрок {current_symbol} победил!')
                return
            current_symbol = 'O' if current_symbol == 'X' else 'X'
        else:
            print('Эта позиция уже занята. Попробуйте другую.')
    display_board()
    print('Ничья.')


tic_tac_toe()