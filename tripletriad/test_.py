from app import game_loop, game_board


# Triple Triad is played on a three-by-three (3x3) square grid of blank spaces
def test_game_board_new():
    dummy_data = [None for x in range(9)]
    call_func = game_board()
    assert call_func == dummy_data

def test_game_board_existing():
    dummy_data = (3, 'card')
    board = [None for x in range(9)]
    board[dummy_data[0]] = dummy_data[1]

    call_func = game_board((3, 'card'))
    assert call_func == board

# Game rules - Default open
def test_game_loop():
    dummy_data = True
    call_func = game_loop()
    print(call_func)
    assert call_func == dummy_data
# Each card has four numbers (known as ranks) placed in top left corner;
# each number corresponds to one of the four sides of the card
# The top right of the card sometimes has an elemental symbol representing the
# card's element: Earth, Fire, Water, Poison, Holy, Lightning, Wind, or Ice.
# Red cards belong to the opponent and blue cards belong to the player.
card = ('rank', 'rank', 'rank', 'rank', 'elemental=elemental', 'player=bool')
# The ranks range from one to nine, the letter A representing ten.
rank = (range(1-10)) # 10 == 'A'
# In a basic game each player has five cards.
def hand():
    """each player is dealt 5 cards"""
    pass
# A coin-flip decides who begins
def coinflip():
    """Winner gets to go first"""
    pass
# The player who wins the coin toss may choose a card to play anywhere on the
# grid. After the first card is played, the opponent may play a card on any
# unoccupied space on the board. The game continues with players' turns alternating.
# the player must capture cards by placing a card adjacent to an opponent's
# card whereupon the ranks of the sides where the two cards touch will be compared.
# If the player's rank is higher, the opponent's card will be captured and
# changed into the player's color instead.
def play():
    """Play card in empty grid space.
    if next to card: compare 'touching' ranks.
    if players rank is higher, card turns player colour"""
    pass
# To win, a majority of the total ten cards played (including the one card that
# is not placed on the board) must be of the player's card color.
# A draw occurs if the player and the opponent possess equal numbers of cards in their color on the board.
# Depending on alternate card rules, this can be defined by a sudden death
# scenario where the first person to capture a card in a new game wins,
# or by playing until a winner is defined.
# The winner takes one or more of the loser's cards, depending upon the trade
# rules in effect
def winner():
    """check who has most cards on the board.
    most cards == winner.
    if draw: sudden death
    winner takes loser cards based on TRADE RULES"""
    pass

#Open
#Enables the player to see which cards the opponent is using.
see_cards = bool
# Same
# When a card is placed touching two or more other cards (one or both of them
# have to be the opposite color), and the touching sides of each card is the
# same (8 touching 8 for example), then the other two cards are flipped.
# Combo rule applies.

# Same Wall
# An extension of the Same rule. The edges of the board are counted as A ranks
# for the purposes of the Same rule. Combo rule applies. If the Same rule is
# not present in a region that has Same Wall, Same Wall will not appear in
# the list of rules when starting a game because it can have no effect without
# Same but it will be carried with the player to other regions, and can
# therefore still be spread.

# Sudden Death
# If the game ends in a draw, a sudden death occurs in which a new game is
# started but the cards are distributed on the side of the color they were on
# at the end of the game.

# Random
# Five cards are randomly chosen from the player's deck instead of the player
# being able to choose five cards themselves.

# Plus
# Similar to the Same rule. When one card is placed touching two others
# and the ranks touching the cards plus the opposing rank equal the same sum,
# then both cards are captured. Combo rule applies.

# Combo
# Of the cards captured by the Same, Same Wall or Plus rule, if they are
# adjacent to another card whose rank is lower, it is captured as well.
# This is not a separate rule; any time Same or Plus is in effect, Combo is
# in effect as well.

# Elemental
# In the elemental rule, one or more of the spaces are randomly marked with an
# element. Some cards have elements in the upper-right corner. Ruby Dragon,
# for example, is fire-elemental, and Quezacotl is thunder-elemental. When an
# elemental card is placed on a corresponding element, each rank goes up a
# point. When any card is placed on a non-matching element, each rank goes down
# a point. This does not affect the Same, Plus and Same Wall rules where the
# cards' original ranks apply.

# CARD TRADE RULES

# One - Rank 1
# 	Winner chooses one card from loser.

# Difference (diff) - Rank 2
# Winner chooses one card per score difference (2, 4, or 5).

# Direct - Rank 3
# 	Players take cards that are their color at the end of the game.

# All - Rank 4
# Winner takes all.


"""
from unnecessary_math import multiply

def test_numbers_3_4():
    assert multiply(3,4) == 12

def test_strings_a_3():
    assert multiply('a',3) == 'aaa'
"""
