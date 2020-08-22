# August 21, 2020
# Permutations 2: given a collection of integers (maybe duplicates), return all possible permutations

# Backtracking: swap method
# - Base case: stop once the current index you're dealing with == length of nums array
# - Backtracking fundamentals
#   1. Make the change: swap nums value at stationary index (start) with that at runner index
#   2. Recurse: call perm(...) w/stationary index incremented
#   3. Undo the change: same swap as before (swap back)
# - Handling Duplicates: create a new set at each start index (each perm recursive call). This set saves values that
#   have been used at this index. If we reach a value in the array that is already in the set, we don't proceed because it 
#   would generate a whole tree of outcomes that completely match another tree.
# Note: make sure to copy nums when saving a permutation otherwise all the lists in ans will be same value (referencing
#       the same object)
def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    if not nums:
        return []
    
    ans = []
    def perm(nums, start):
        if start == len(nums):
            ans.append(list(nums))
            return
            
        used_curr_idx = set()
        for run in range(start, len(nums)):
            if nums[run] not in used_curr_idx:
                used_curr_idx.add(nums[run])
                nums[start], nums[run] = nums[run], nums[start]
                perm(nums, start+1)
                nums[start], nums[run] = nums[run], nums[start]
            
    perm(nums, 0)
    return ans