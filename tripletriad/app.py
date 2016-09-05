import shelve

def write_board():
    board_name = 'board_01'
    board = {
        1: '', 2: '', 3: '',
        4: '', 5: '', 6: '',
        7: '', 8: '', 9: '',
        }


    with open('board', 'w') as b:
        b.write(str(board))
        b.closed

def u_board():
    with open('board', 'r') as b:
        print(b.readlines())
        b.closed

# write_board()
u_board()

def new_board():
    board_list = shelve.open('game.db')
    board_name = 'board_01'
    try:
        board_list[board_name] = {
            1: '', 2: '', 3: '',
            4: '', 5: '', 6: '',
            7: '', 8: '', 9: '',
            }
    finally:
        board_list.close()


def enter_board():
    board_list = shelve.open('game.db')
    board_name = 'board_01'
    try:
        aa = board_list[board_name]
        aa[5] = 'nadine'
    finally:
        board_list.close()


def update_board():
    board_list = shelve.open('game.db')
    board_name = 'board_01'
    try:
        aa = board_list[board_name]
    finally:
        board_list.close()
        return aa

# new_board()

def game_loop():
    """Default rule set = Open"""
    return True

def game_board(play=False):
    """"""
    board = []
    if play == False:
        board = [None for x in range(9)]
        return board
    else:
        board[play[0]] = play[1]
        return board
