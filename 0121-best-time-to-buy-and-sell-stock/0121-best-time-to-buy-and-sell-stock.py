class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prices = collections.deque([])
        cur_max = float('-inf')
        for price in reversed(prices):
            cur_max = max(cur_max, price)
            max_prices.appendleft(cur_max)
            
        # [7,6,6,6,4]
        max_profit = 0
        for i, buy_price in enumerate(prices):
            today_profit = max_prices[i] - buy_price
            max_profit = max(today_profit, max_profit)
        
        return max_profit