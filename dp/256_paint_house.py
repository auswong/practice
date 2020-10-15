# Input: [[14,2,11],[11,14,5],[14,3,10]]
# Output: 10
# Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue. Minimum cost: 2 + 5 + 3 = 10.
# Example 2:

# Input: [[1,2,3],[1,4,6]]
# Output: 3

# Input: [[17,2,17],[16,16,5],[14,3,19]]
# Output: 10

def paint_house(cost_matrix):
    for i in range(1, len(cost_matrix)):
        # curr color is "0" so the previous house must be color "1" or "2"
        cost_matrix[i][0] = min(cost_matrix[i-1][1], cost_matrix[i-1][2]) + cost_matrix[i][0]
        
        # curr color is "1" so the previous house must be color "0" or "2"
        cost_matrix[i][1] = min(cost_matrix[i-1][0], cost_matrix[i-1][2]) + cost_matrix[i][1]

        # curr color is "2" so the previous house must be color "0" or "1"
        cost_matrix[i][2] = min(cost_matrix[i-1][0], cost_matrix[i-1][1]) + cost_matrix[i][2]

    return min(cost_matrix[-1])


cost_matrix = [[14,2,11], [11,14,5], [14,3,10]]
cost_matrix1 = [[17,2,17],[16,16,5],[14,3,19]]
print(paint_house(cost_matrix1))