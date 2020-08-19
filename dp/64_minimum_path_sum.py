# August 19, 2020
# Minimum Path Sum: find a path from top left to bottom right which minimizes the sum of all # along its path

# Bottom up approach: 
# - Initialize each index in the 1st row and col to have the sum of all previous elements in row and col respectively
# - Starting at cell (1,1), add the cells value to the min of the top and left cell
# - The answer will be in the bottom right cell since you're always taking the min at each step
def minPathSum(self, grid: List[List[int]]) -> int:
    # initialize 1st row
    for i in range(1, len(grid[0])):
        grid[0][i] += grid[0][i-1]
    
    #initialize 1st col
    for i in range(1, len(grid)):
        grid[i][0] += grid[i-1][0]
        
    # bottom up dp always taking the minimum of up and left cell
    for row in range(1, len(grid)):
        for col in range(1, len(grid[0])):
            grid[row][col] += min(grid[row-1][col], grid[row][col-1])     # min of above and left cell
            
    return grid[-1][-1]