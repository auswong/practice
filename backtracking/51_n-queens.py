# August 24, 2020
# N-Queens:  The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two 
# queens attack each other. Given an integer n, return all distinct solutions to the n-queens puzzle.

# Backtracking:
# - Base case: stop once row == n
# - start with 1 queen in each square in the top row & initialize map from row to occupied column
# - Backtracking fundamentals
#   1. Make the change: check which square in the next row can have a queen
#   2. Recurse: call backtrack(...) w/updated chess board and map and row+1 
#   3. Undo the change: happens automatically
# Note: make sure to ALL squares directly and diagonally above are empty before placing a queen. The patter for diagonal
#       conflict is that in a row k squares away, the k squares to the right and left of the current column must be empty
def solveNQueens(self, n: int) -> List[List[str]]:
    if n < 1:
        return [[]]
    if n == 2 or n == 3:
        return []

    ans = []
    def backtrack(n, curr_row, cols, so_far): # cols: maps row index to occupied column
        if curr_row == n:
            ans.append(list(so_far))
            return
        
        for col in range(n):
            can_placeQ = True
            for check in range(1, curr_row+1):    # marks as false if ANY conflict exists directly or diagonally above
                if col - cols[curr_row-check] == 0 or abs(col - cols[curr_row-check]) == check:
                    can_placeQ = False
                    break
            
            if can_placeQ:
                so_far[curr_row] = ('.' * col + 'Q' + '.' * (n-1-col))
                cols[curr_row] = col

                backtrack(n, curr_row + 1, cols, so_far)

    so_far = ['.'*n] *n
    cols = [-1] * n
    for i in range(n):
        so_far[0] = '.' * i + 'Q' + '.' * (n-1-i)
        cols[0] = i
        
        backtrack(n, 1, cols, list(so_far))
        
    return ans
        