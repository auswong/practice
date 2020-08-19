# August 17, 2020
# Minimum Cost For Tickets: return smallest price for travelling on all days in days list given prices for 1/7/30 day travel pass

# Bottom up approach: 
# - Create dp array with indexes from 0 to last day (value = 0). Ignore index 0 and the index equals the day.
# - Iterate from 1 to last day, and at each day (if we travel on it) check the min dollars that can be used to reach 
#   the days 1/7/30 days less than current day.
#   NOTE: once the price of repeated 1-day tickets overtake the price of a 7-day ticket, the 7-day price will be the 
#   min and therefore the value that fills the dp array at this index
# - If we don't travel on given day, day's cost is the previous day's cost.
# - Return end of array 
def mincostTickets(self, days: List[int], costs: List[int]) -> int:
    days_set = set(days)
    dp = [0] * (days[-1] + 1)
    
    for day in range(1, days[-1]+1):
        if day in days_set:
            if day > 30:
                dp[day] = min(dp[day-1] + costs[0], dp[day-7] + costs[1], dp[day-30] + costs[2])
            elif day > 7: 
                dp[day] = min(dp[day-1] + costs[0], dp[day-7] + costs[1], costs[2]) # can't go 30 days in the past but could've chosen a 30 day pass initially
            else:
                dp[day] = min(dp[day-1] + costs[0], costs[1], costs[2]) # can't go 30 or 7 days in the past but could've chosen a 30 day or 7 day pass initially
        else:
            dp[day] = dp[day-1]
    
    return dp[days[-1]]