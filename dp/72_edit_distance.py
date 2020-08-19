# August 18, 2020
# Edit Distance: find the minimum # of ops required to convert word1 to word2 (insert, substitute, delete)

# Bottom up approach: 
# Levenshtein Distance Algorithm
# - Create 2d dp array len(word1)+1 x len(word2)+1
# - Fill the elements in the 1st row and column with their own respective index
# - Iterate through remaining rows and cols, and if chars don't match in the two words take the min of the up, left, and 
#   up-left cell + 1
# - if the chars match, take the copy the up-left cell into the current cell
# - return the bottom right cell value

# If converting from row word (vertical) to col word (horzontal)
#   diagonal = substitute
#   vertical = delete from row word
#   horizontal = insert into row word
# Else if converting from col word (horizontal) to row word (vertical)
#   diagonal = substitute
#   vertical = insert into col word
#   horizontal = delete into col word
def minDistance(self, word1: str, word2: str) -> int:
    # initialize 2d dp array
    dp2d = [] 
    for row in range(len(word2) + 1):
        dp2d.append([0] * (len(word1) + 1))
        
    for col in range(1, len(word1) + 1):
        dp2d[0][col] = col
        
    for row in range(1, len(word2) + 1):
        dp2d[row][0] = row
    
    for row in range(1, len(word2) + 1):
        for col in range(1, len(word1) + 1):
            if word1[col-1] != word2[row-1]:
                dp2d[row][col] = min(dp2d[row-1][col], dp2d[row-1][col-1], dp2d[row][col-1]) + 1
            else:
                dp2d[row][col] = dp2d[row-1][col-1]
    
    return dp2d[-1][-1]