# August 19, 2020
# House Robber 2: determine the max amount of money you can rob without robbing adjacent or both the 1st and last 
# houses (indices)

# Bottom up approach: 
# - Handle the edge cases: 0 houses, < 4 houses, and 4 houses
# - Create fn to handle recurrence relation: house[i] = max(house[i-1], house[i-2] + house[i])
# - In order to apply this recurrence relation to the circular neighborhood, take the max of robbing the 
#   neighborhood excluding the 1st house and excluding the last house
def rob(self, nums: List[int]) -> int:
    if not nums:
        return 0
    
    if len(nums) < 4:
        return max(nums)
    
    elif len(nums) == 4:
        return max(nums[0]+nums[2], nums[1]+nums[3])

    def rob_helper(nums: List[int]) -> int:
        nums.insert(0,0)
        for i in range(2, len(nums)):
            nums[i] = max(nums[i-1], nums[i-2] + nums[i])
        
        return nums[-1]

    return max(rob_helper(nums[1:]), rob_helper(nums[:-1]))