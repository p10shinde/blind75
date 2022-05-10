# Best time to buy and sell stock
input = [7, 1, 5, 3, 6, 4]
input = [7, 6, 4, 3, 1]
input = [2, 4, 1]
# Time: O(n)
# Space: O(1) 
def maxProfit(prices):
    maxP = 0
    l,r=0, 1 # left = buy, right = sell
    while r < len(prices):
        # profitable?
        if prices[l] <  prices[r]:
            profit = prices[r] - prices[l]
            maxP = max(profit, maxP)
        else:
            l = r
        r+=1
    return maxP

print(maxProfit(input))