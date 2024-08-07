class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # [7,1,5,3,6,4]
        #  7 6 6 6 6 4
        
        maxes = [0] * len(prices)
        cur_max = float('-inf')
        
        for i, p in reversed(list(enumerate(prices))):
            cur_max = max(cur_max,p)
            maxes[i] = cur_max
        max_profit = 0
        for i, p in enumerate(prices):
            best_sell = maxes[i]
            buy = p
            max_profit = max(max_profit, best_sell-buy)
        return max_profit
            
        