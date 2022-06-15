from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyDay = 0
        sellDay = 1
        
        maxProfit = 0
        
        while sellDay < len(prices):
            #profitable?
            if prices[buyDay] < prices[sellDay]:
                profit = prices[sellDay] - prices[buyDay]
                maxProfit = max(profit, maxProfit)
            else: # buyDay greater than sellDay (or equal to)
                buyDay = sellDay
            sellDay += 1
        return maxProfit