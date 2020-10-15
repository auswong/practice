# Oct 10, 2020
# Valid Sudoku:

# Find out if a board is valid (may not necessarily be solvable)
# list of 9 set()'s for row, column, and boxes
def isValidSudoku(self, board: List[List[str]]) -> bool:
    rows = [set() for i in range(9)]
    cols = [set() for i in range(9)]
    boxes = [set() for i in range(9)]
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] != ".":
                # if a duplicate exists in the corresponding row, col, or box
                if board[r][c] in rows[r] or board[r][c] in cols[c] or  board[r][c] in boxes[3* (r//3) + (c//3)]:
                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                boxes[3* (r // 3) + (c // 3)].add(board[r][c])
    return True
                