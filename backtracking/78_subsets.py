# August 21, 2020
# Subsets: given a set of distinct integers, return all possible subsets (the power set)

# Backtracking:
# - Base case: stop once tthe remaining left to insert == 0
# - Backtracking fundamentals
#   1. Make the change: insert a num into so_far list
#   2. Recurse: call gen(...) w/start index == index of inserted+1 which prevents adding duplicates to a subset-in-progress 
#      and incorrect subsets)
#   3. Undo the change: pop list
# Note: make sure to copy so_far when saving a permutation or don't actually modify it, otherwise all the lists in ans
#       will be same value (referencing the same object)
def subsets(self, nums: List[int]) -> List[List[int]]:
    ans = []
    
    def gen(nums, start, remaining, so_far):
        if remaining == 0:
            # Solution 1
            ans.append(list(so_far))

            # Solution 2
            # ans.append(so_far)
            return
        
        for i in range(start, len(nums)):
            # Solution 1
            so_far.append(nums[i])
            gen(nums, i+1, remaining-1, so_far)
            so_far.pop()

            # Solution 2
            # gen(nums, i+1, remaining-1, so_far + [nums[i]])
        
    for i in range(len(nums)+1):
        gen(nums, 0, i, [])
    
    return ans  