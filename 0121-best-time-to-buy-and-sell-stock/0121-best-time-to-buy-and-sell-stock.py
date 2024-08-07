class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        best_sell_price = float('-inf')
        max_profit = 0
        for buy_day in range(len(prices)-1,-1,-1):
            best_sell_price = max(best_sell_price,prices[buy_day])
            max_profit = max(max_profit, best_sell_price-prices[buy_day])
        
        return max_profit
            
        