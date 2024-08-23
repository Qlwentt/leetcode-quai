class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prefix_maxes = [0] * len(prices)
        cur_max = float('-inf')
        for i in range(len(prices)-1,-1,-1):
            cur_max = max(cur_max, prices[i])
            prefix_maxes[i] = cur_max
            
        # [7,6,6,6,4]
        max_profit = 0
        for i, buy_price in enumerate(prices):
            today_profit = prefix_maxes[i] - buy_price
            max_profit = max(today_profit, max_profit)
        
        return max_profit
# Time: O(N)
# Space: O(N)


# constant space solution
        cur_max = float('-inf')
        max_profit = 0
        for price in reversed(prices):
            cur_max = max(price, cur_max)
            today_profit = cur_max - price
            max_profit = max(today_profit, max_profit)
        return max_profit
    
# Time: O(N)
# Space: O(1)