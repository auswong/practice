# August 17, 2020
# Coin Change: return fewest number of coins needed to make amount

# Bottom up approach: 
# - Create dp array with indexes from 0 to amount (value = inf). Ignore index 0 and the index equals money amount.
# - Iterate from 1 to amount, and at each index select the min num of coins used to reach the values one
#   coin less than current index.
# - If amount index is untouched, can't reach. Else, return that amount. 
def coinChange(self, coins: List[int], amount: int) -> int:
    # if amount == 0:   handled by "dp[0] = 0"
    #     return 0

    dp = [float("inf")] * (amount+1)
    dp[0] = 0

    # each of provided denominations can be reached with 1 coin of itself
    for c in coins:
        if c <= amount:
            dp[c] = 1

    for idx in range(1, amount+1):
        if dp[idx] == float("inf"): # untouched so far (could also write "not in coins")
            for c in coins:         
                if idx - c >= 0:    # find min amt from all denominations that can be reached by adding 1 coin
                    dp[idx] = min(dp[idx], dp[idx - c] + 1)
    
    return -1 if dp[amount] == float("inf") else dp[amount]     # if amount is untouched -> can't reach; else return 
                