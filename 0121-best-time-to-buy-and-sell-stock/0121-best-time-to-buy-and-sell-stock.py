class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxProfit = 0
        prevSellPrice = 0
        for i in range(len(prices)-1,0,-1):
            sellPrice = max(prevSellPrice, prices[i])
            profit = sellPrice - prices[i-1]
            maxProfit = max(profit, maxProfit)
            prevSellPrice = sellPrice
        return maxProfit
        