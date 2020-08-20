# August 20, 2020
# Permutations: given a collection of distinct integers, return all possible permutations

# Backtracking:
# - Base case: stop once the current perm length == length of nums array
# - Backtracking fundamentals
#   1. Make the change: perm + [i]
#   2. Recurse: call gen(...)
#   3. Undo the change: implicit here. Perm isn't changed before the gen(...) call, so when you return from the gen(...)
#      call, perm is as if the change never happened
#   Alternate solution:
#       perm.append(i)
#       gen(nums, perm, ans)
#       perm.pop()
def permute(self, nums: List[int]) -> List[List[int]]:
    if not nums:
        return nums
    
    def gen(nums, perm, ans):
        if len(nums) == len(perm):
            ans.append(perm)
        
        for i in nums:
            if i not in perm:
                perm.append
                gen(nums, perm + [i], ans)
        
    ans = []
    gen(nums, [], ans)
    return ans