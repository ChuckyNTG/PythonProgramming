board = []
for _ in range(4):
    board.append([int(num) for num in raw_input()])
move = int(raw_input())
if move == 0:
    for row in board:
        if set(row) == 4:
            pass
        else:
           
        

