import os

dir_path = os.path.realpath(__file__)
path, filename = os.path.split(dir_path)                
input = open(path + '\\input.txt')

numbers = [int(x) for x in next(input).split(',')]
next(input)

boards = []

first_win = len(numbers)
last_win = -2

for i in range(100):
    board = []
    try:
        for j in range(5):
            line = next(input).replace('\n', '').split()
            line = [int(x) for x in line]
            board.append(line)
        boards.append(board)
        next(input)
    except StopIteration:
        break

for board in boards:
    transposed_board = [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]
    transposed_board += board

    board_winning_drawings = []

    for line in transposed_board:
        if all([x in numbers for x in line]): #is winning line or column
            line_winning_drawing = max([numbers.index(int(x)) for x in line])
        else:
            line_winning_drawing = -1
        board_winning_drawings.append(line_winning_drawing)

    board_win_step = min(board_winning_drawings)

    #Part 1
    if board_win_step < first_win:
        first_win_board = board
        first_win = board_win_step
    
    #Part 2
    if board_win_step > last_win:
        last_win_board = board
        last_win = board_win_step

unmarked_sum = 0
for line in first_win_board:
    for n in line:
        #unmarked numbers - not in the drawn numberlist or is in the list after the winning number
        if n not in numbers or numbers.index(n) > first_win:
            unmarked_sum += n

result_p1 = unmarked_sum * numbers[first_win]
print(result_p1)

unmarked_sum = 0
for line in last_win_board:
    for n in line:
        if n not in numbers or numbers.index(n) > last_win:
            unmarked_sum += n

result_p2 = unmarked_sum * numbers[last_win]
print(result_p2)