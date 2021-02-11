from typing import Tuple, List, Optional, cast
from random import randint

Playground = List[str]

win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
             (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))


# Representation of the game board

# Creates and returns a new blank game board

def new_playground() -> Playground:
    # Here I create a list with empty elements. I could have
    # created a list with three lists (one list per row),
    # but I thought it would be easier to use math and access
    # the item by index.
    playground: Playground = ['  ', '  ', '  ',
                              '  ', '  ', '  ',
                              '  ', '  ', '  ']
    return playground


# returns a representation of the checkbox on the specified row and column

def get(playground: Playground,
        row: int, col: int) -> str:
    # Here is an index search.
    # For example 1 row and 2 col is the 5 index
    # 1 * 3 + 2 = 5
    index = row * 3 + col
    return playground[index]


# adds to the game board the specified symbol to the specified coordinates

def put(playground: Playground, row: int,
        col: int, symbol: str) -> bool:
    index = row * 3 + col
    if playground[index] == '  ':
        # Increasing the age of the remaining elements

        # I hope I understood what you meant
        n_symbol = (symbol + '3', symbol + '2', symbol + '1')
        for_change = ('  ', symbol + '3', symbol + '2')

        for elem in n_symbol:
            if elem in playground:
                playground[playground.index(elem)] \
                    = for_change[n_symbol.index(elem)]

        # And I put a new symbol on the field
        playground[index] = symbol + '1'
        return True
    else:
        return False


def draw(playground: Playground) -> None:
    print("     0  1  2\n   +--+--+--+")
    for i in range(0, len(playground) - 1, 3):
        # Here I use translating a number to a letter to put all(nearly)
        # actions in one loop. Since the cycle step is 3,
        # I add the remainder of dividing i by 3
        # to the Unicode of the letter 'A'
        print(' ' + chr(65 + (i // 3)) + ' ' + '|' + str(playground[i]) + '|' +
              str(playground[i + 1]) + '|' +
              str(playground[i + 2]) + '|\n   +--+--+--+')


def who_won(playground: Playground) -> Optional[str]:
    o = x = False
    for each in win_coord:
        # I don't know if this is better or worse than a simple
        # if ' X 'in ... and' X ' in...:
        # Can you explain?
        if all('X' in i for i in (playground[each[0]],
                                  playground[each[1]],
                                  playground[each[2]])):
            x = True

        if all('O' in i for i in (playground[each[0]],
                                  playground[each[1]],
                                  playground[each[2]])):
            o = True

    if x == o is True:
        return 'invalid'
    if x is True:
        return 'X'
    if o is True:
        return 'O'
    return None


def hint(playground: Playground, symbol: str) \
        -> Optional[Tuple[int, int]]:
    # If there is only one item of the symbol in the list,
    # then there is no point in running a loop
    if symbol + '2' not in playground:
        return None

    for each in win_coord:
        # Creating "switches" for checking empty space
        # and characters of the desired age
        check_space = check_age_1 = check_age_2 = False
        place_of_space = 42
        for i in range(0, 3, 1):
            if playground[each[i]] == '  ':
                place_of_space = each[i]
                check_space = True
            if symbol + '1' in playground[each[i]]:
                check_age_1 = True
            if symbol + '2' in playground[each[i]]:
                check_age_2 = True
            if all([check_space, check_age_1, check_age_2]):
                return place_of_space // 3, \
                       place_of_space - 3 * (place_of_space // 3)

    return None


def game(x_score: int, o_score: int) -> None:
    # need to randomly determine whose move
    counter = randint(0, 1)
    # "switcher" to stop the game
    endgame = False
    playground = new_playground()
    col = row = 34

    if x_score == 0 and o_score == 0:
        print("First, choose who you will play for\nIt can be the symbol "
              "'X' and 'O'\n(don't worry, the first move will be chosen "
              "randomly)\nAre you choose the symbol and ready "
              "to start the game?")

        start_game = False
        while start_game is False:
            check_start = input('\ny/n: ')
            if check_start == 'y':
                print('Good luck!')
                start_game = True
            elif check_start == 'n':
                print("Ok, i'll wait...")
            else:
                print('Input correct letter!')

    while endgame is False:
        draw(playground)
        if counter % 2 == 0:
            print("X-player, your move!")
            symbol_inp = 'X'
        else:
            print("O-player, your move!")
            symbol_inp = 'O'

        if hint(playground=playground, symbol=symbol_inp) is not None:
            hint_tuple = cast(Tuple[int, int],
                              hint(playground=playground,
                                   symbol=symbol_inp))
            # Here I also use the translation of
            # a number into a letter
            print(symbol_inp + "-player, your move to win:",
                  chr(65 + hint_tuple[0]), hint_tuple[1])

        # Creating a loops so that you can
        # correct an incorrectly entered value
        check_get = False
        while check_get is False:
            # "switches" for checking the correctness of
            # rows and columns for checking them for correct input
            check_row = check_col = False
            while check_row is False:
                # Entering letters will not depend on case sensitivity
                row_inp = input('Input row (A, B, C): ')
                if any(row_inp == i for i in ['A', 'B', 'C']):
                    # translate a letter into a number
                    row = ord(row_inp) - 65
                    check_row = True
                elif any(row_inp == i for i in ['a', 'b', 'c']):
                    row = ord(row_inp) - 97
                    check_row = True
                else:
                    print('Row is not correct')
                    check_row = False

            while check_col is False:
                col_inp = input('Input column (0, 1, 2): ')
                if col_inp.isdigit():
                    col = int(col_inp)
                    if any(col == i for i in [0, 1, 2]):
                        check_col = True
                    else:
                        print('Column is not correct')
                else:
                    print('Column is not correct, input number!')

            # Check the entered coordinates for emptiness
            if get(playground, row=row, col=col) == '  ':
                check_get = True
            else:
                print('Try another place!')

        put(playground, row=row, col=col, symbol=symbol_inp)

        # Changes the parity of the counter
        # for the second player's move
        counter += 1
        if who_won(playground) == 'X' or who_won(playground) == 'O':
            draw(playground)
            # Scoring points
            if who_won(playground) == 'X':
                x_score += 1
            else:
                o_score += 1

            print(symbol_inp + "-player, now you are win!\n"
                               '___________________________\n'
                               '       Actual score\n[X-player]',
                  x_score, ':', o_score,
                  '[O-player]\n'
                  '___________________________')

            # You need to give the opportunity for a rematch,
            # don't you?:)
            check = False
            while check is False:
                print('One more game?')
                next_game = input('y/n: ')
                if next_game == 'y' or next_game == 'Y':
                    return game(x_score, o_score)
                elif next_game == 'n' or next_game == 'N':
                    print("See you later!")
                    endgame = True
                    check = True
                else:
                    print('Print correct letter!')


if __name__ == '__main__':
    # I added the game score, so there are zeros here
    # To be honest, I would also add a time limit on the move,
    # but we can't import the time module ¯\_(ツ)_/¯
    game(0, 0)
