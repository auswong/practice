# August 19, 2020
# House Robber: determine the max amount of money you can rob without robbing adjacent houses

# Bottom up approach: 
# - Handle the edge cases: 0 houses & < 3 houses
# - Create fn to handle recurrence relation: house[i] = max(house[i-1], house[i-2] + house[i])
def rob(self, nums: List[int]) -> int:
    if not nums:
        return 0
    
    if len(nums) < 3:
        return max(nums)
    
    nums[2] += nums[0]
    for i in range(3, len(nums)):
        nums[i] += max(nums[i-2], nums[i-3])

    return max(nums[-2], nums[-1])