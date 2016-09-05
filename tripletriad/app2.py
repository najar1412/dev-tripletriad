import sqlite3
import ast
import random

db_name = 'database.db'


def card_gen():
    rank = [
        random.choice(tuple([x for x in range(11)[1:]])),
        random.choice(tuple([x for x in range(11)[1:]])),
        random.choice(tuple([x for x in range(11)[1:]])),
        random.choice(tuple([x for x in range(11)[1:]]))
        ]

    elemental = random.choice(('Earth', 'Fire', 'Water', 'Poison', 'Holy', 'Lightning', 'Wind', 'Ice'))
    card = [rank[0], rank[1], rank[2], rank[3], elemental, True]

    return card


def mk_table():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    # Create table
    c.execute('''CREATE TABLE boards
                 (id integer primary key, name text, layout text)''')
    conn.commit()
    conn.close()


def mk_board(name):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    board_name = ('{}'.format(name),)
    c.execute('SELECT name FROM boards WHERE name=?', board_name)
    result_board_name = c.fetchall()

    # Insert a row of data
    layout = {
        1: None, 2: None, 3: None,
        4: None, 5: None, 6: None,
        7: None, 8: None, 9: None,
        }

    if len(result_board_name) < 1:
        c.execute("INSERT INTO boards VALUES (NULL, '{}', '{}')".format(name, layout))
    # Save (commit) the changes
    conn.commit()
    conn.close()


def get_board(name):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    board_name = ('{}'.format(name),)
    c.execute('SELECT * FROM boards WHERE name=?', board_name)
    board = tuple(c.fetchone())[2]
    board = ast.literal_eval("{}".format(board))
    conn.close()

    return board


def update_board(name, position, card):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    query_name = ('{}'.format(name),)
    c.execute('SELECT * FROM boards WHERE name=?', query_name)

    board = tuple(c.fetchone())[2]
    board = ast.literal_eval("{}".format(board))

    board[position] = card

    query_layout = '{}'.format(board)
    c.execute("UPDATE boards SET layout=? WHERE name=?", (query_layout, name))
    conn.commit()
    conn.close()


def hand_player(count=5):
    hand = []
    for card in range(count):
        hand.append(card_gen())

    return hand


def hand_opponent(count=5):
    hand = []
    for card in range(count):
        hand.append(card_gen())

    for card in hand:
        card[5] = False

    return hand


def coinflip(call='heads'):
    coin = ['heads', 'tails']
    flip = random.choice(coin)
    if call == flip:
        return (True, flip)
    else:
        return (False, flip)


def play_card(card, player):
    hand = player
    played_card = list(hand).pop(card)
    return played_card


def card_check(name, card, position):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    query_name = ('{}'.format(name),)
    c.execute('SELECT * FROM boards WHERE name=?', query_name)

    board = tuple(c.fetchone())[2]
    board = ast.literal_eval("{}".format(board))

    checker = {
        1: ((2, 1, 3), (4, 2, 0)),
        2: ((1, 3, 1), (5, 2, 0), (3, 1, 3)),
        3: ((2, 3, 1), (6, 2, 0)),
        4: ((1, 0, 2), (5, 1, 3), (7, 2, 0)),
        5: ((2, 0, 2), (4, 3, 1), (6, 1, 3), (8, 2, 0)),
        6: ((3, 0, 2), (5, 3, 1), (9, 2, 2)),
        7: ((4, 0, 2), (8, 1, 3)),
        8: ((5, 0, 2), (7, 3, 1), (9, 1, 3)),
        9: ((6, 0, 2), (8, 3, 1))
    }

    # flip colour of card if play cards rank is higher
    for x in checker[position]:
        if board[x[0]] != None:
            if card[1] > board[x[0]][x[2]]:
                board[x[0]][5] = card[5]

    # Update db row with new board
    query_layout = '{}'.format(board)
    c.execute("UPDATE boards SET layout=? WHERE name=?", (query_layout, name))
    conn.commit()
    conn.close()
    return board


def gameloop():
    # start game
    new_game = True
    # new board
    board_name = 'board_02' # generate unqiue board name
    mk_board(board_name)
    print(get_board(board_name))
    # deal hands
    hand_player()
    hand_opponent()

    # flip coin
    flip = coinflip('tails')
    # user plays
    if flip[0]:
        # Player turn
        card_to_play = 1
        position_to_play = 6
        played_card = play_card(card_to_play, hand_player())
        update_board(board_name, position_to_play, played_card)
        card_check(board_name, played_card, position_to_play)
    else:
        # opponent plays
        card_to_play = 1
        position_to_play = 5
        played_card = play_card(card_to_play, hand_opponent())
        update_board(board_name, position_to_play, played_card)
        card_check(board_name, played_card, position_to_play)


gameloop()
