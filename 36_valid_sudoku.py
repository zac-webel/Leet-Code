# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.


# board[row][col]
# brute force 
    # check verticle repeated numbers
    # check horizontal repeated numbers
    # check three box
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_v(b):
            for col in range(9):
                seen = set()
                for row in range(9):
                    val = b[row][col]
                    if val!='.':
                        if val not in seen:
                            seen.add(val)
                        else:
                            return False
            return True
                    
        def check_h(b):
            for row in range(9):
                seen = set()
                for col in range(9):
                    val = b[row][col]
                    if val!='.':
                        if val not in seen:
                            seen.add(val)
                        else:
                            return False
            return True

        def check_3(b):
            for starting_row in [0,3,6]:
                for starting_col in [0,3,6]:
                    seen = set()
                    for row in range(starting_row,starting_row+3):
                        for col in range(starting_col,starting_col+3):
                            val = b[row][col]
                            if val!='.':
                                if val not in seen:
                                    seen.add(val)
                                else:
                                    return False
            return True

        valid_v = check_v(board)
        valid_h = check_h(board)
        valid_3 = check_3(board)
        if valid_v and valid_h and valid_3:
            return True
        return False