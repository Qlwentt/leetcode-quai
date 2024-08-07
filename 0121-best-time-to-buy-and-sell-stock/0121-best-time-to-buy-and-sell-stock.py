class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        best_sell_price = float('-inf')
        max_profit = 0
        for i, buy_price in reversed(list(enumerate(prices))):
            best_sell_price = max(best_sell_price,buy_price)
            max_profit = max(max_profit, best_sell_price-buy_price)
        
        return max_profit
            
        