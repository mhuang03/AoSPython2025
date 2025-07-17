"""
A program that helps chess players determine whether a knight or rook can move to a given position on the board.
This version is a little buggy. Can you find the bugs and fix them?
"""


def extract_file_rank(pos):
    """
    Accepts a chess position and returns the file and rank as integers
    :param pos: a position string in chess notation (e.g. 'a1' or 'g7')
    :return: a tuple of integers from 1 to 8 inclusive.
    """
    # check for valid chess positions
    if (pos[0] not in 'abcdefghABCDEFGH') or (pos[1] not in '12345678'):
        raise ValueError(f'{pos} is not a valid chess position.')

    # calculate file and rank
    file = ord(pos[0].lower()) - ord('a') + 1     # ord() maps chars A-Z to 65-90 and chars a-z to ints 97-122
    rank = int(pos[1])

    # ensure file and rank are integers from 1 to 8 inclusive
    if file not in range(1, 9):
        raise ValueError(f'File number {file} is outside the valid range.')
    if rank not in range(1, 9):
        raise ValueError(f'Rank number {rank} is outside the valid range.')

    return file, rank


def knight_can_move(knight_pos, other_pos):
    """
    Determines whether a knight can move to another position
    :param knight_pos: a position string in chess notation
    :param other_pos: a position string in chess notation
    :return: boolean
    """
    knight_file, knight_rank = extract_file_rank(knight_pos)
    other_file, other_rank = extract_file_rank(other_pos)

    # knights move 2 spaces along one direction and 1 in the other
    file_dist = abs(knight_file - other_file)
    rank_dist = abs(knight_rank - other_rank)
    if file_dist == 2 and rank_dist == 1 or file_dist == 1 and rank_dist == 2:
        return True
    return False


def rook_can_move(rook_pos, other_pos):
    """
    Determines whether a rook can move to another position
    :param rook_pos: a position string in chess notation
    :param other_pos: a position string in chess notation
    :return: boolean
    """
    rook_file, rook_rank = extract_file_rank(rook_pos)
    other_file, other_rank = extract_file_rank(other_pos)

    # rooks can move any distance along its file or rank
    if rook_file == other_file or rook_rank == other_rank:
        return True
    return False


if __name__ == '__main__':
    # These position lists should not be changed.
    knight_positions = ['A4', 'c5', 'f8', 'd1', 'C3']
    rook_positions = ['b7', 'c2', 'H1', 'g6', 'e3']
    other_positions = ['B5', 'E6', 'd3', 'f2', 'a1']

    # For each knight position, we check if it can move to each other position
    for knight in knight_positions:
        for other in other_positions:
            if knight_can_move(knight, other):
                print(f'A knight on {knight.lower()} can move to {other.lower()}.')

    # Repeat with rook positions
    for rook in rook_positions:
        for other in other_positions:
            if rook_can_move(rook, other):
                print(f'A rook on {rook.lower()} can move to {other.lower()}.')


# The following is the expected output from this program:
"""
A knight on c5 can move to e6.
A knight on c5 can move to d3.
A knight on f8 can move to e6.
A knight on d1 can move to f2.
A knight on c3 can move to b5.
A rook on b7 can move to b5.
A rook on c2 can move to f2.
A rook on h1 can move to a1.
A rook on g6 can move to e6.
A rook on e3 can move to e6.
A rook on e3 can move to d3.
"""


