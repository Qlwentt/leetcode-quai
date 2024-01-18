class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # [7,1,2,5,6,4]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i]> prices[i-1]:
                profit += prices[i] - prices[i-1]
                
        return profit
        