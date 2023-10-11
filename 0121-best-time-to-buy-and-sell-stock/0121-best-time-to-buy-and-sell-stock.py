class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxProfit = 0
        buyPrice = float("inf")
        for buyDay in range(len(prices)-1):
            buyPrice = min(prices[buyDay], buyPrice) 
            sellPrice = prices[buyDay+1]
            maxProfit = max(maxProfit, sellPrice-buyPrice)            
        
        return maxProfit
            
            
        