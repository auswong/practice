# August 18, 2020
# Coin Change 2: find the number of combinations that make up given amount

# Bottom up approach: 
# - Create 1d dp array 0 to amount, initialize index 0 to 1

def change(self, amount: int, coins: List[int]) -> int:
    dp = [0] * (amount + 1)
    dp[0] = 1

    for coin in coins:
        for idx in range(coin, amount+1):
            if idx - coin >= 0:
                dp[idx] += dp[idx-coin]
    
    return dp[amount]