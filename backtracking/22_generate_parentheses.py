# August 20, 2020
# Generate Parentheses: given n pairs of parentheses, generate all combinations of well-formed parentheses

# Backtracking: 
# - Key idea: # of remaining left parentheses must always be <= # of remaining right parentheses
# - Main base case: when remaining left and right parentheses = 0, save permutation
# - Secondary base case: when remaining left parentheses = 0, append all the remaining right parentheses
# - Now there are 2 scenarios we have to decide to recurse on: when to add a left parenthesis (left == right)
#   and a right one (left < right)
def generateParenthesis(self, n: int) -> List[str]:
    if n == 0:
        return []
    
    def gen(left, right, so_far, ans):
        if left == 0 and right == 0:
            ans.append(so_far)
            return
        
        if left == 0:
            ans.append(so_far + ')'*right)
            return
        

        # More readable solution
        # if left == right:
        #     gen(left-1, right, so_far + '(', ans)

        # elif left < right:
        #     gen(left-1, right, so_far + '(', ans)
        #     gen(left, right-1, so_far + ')', ans)


        # More concise solution
        if left < right:
            gen(left, right-1, so_far + ')', ans)

        gen(left-1, right, so_far + '(', ans)

    ans = []
    gen(n-1, n, '(', ans)
    return ans