class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # memoization
        memo = {}
        def dfs(i,curBuy):
            if i >= len(prices):
                return 0
            
            if (i, curBuy) in memo:
                return memo[(i,curBuy)]
            
            # buy
            buy = dfs(i+1, prices[i])
            
            # sell
            sell = 0
            if curBuy != -1:
                profit = prices[i] - curBuy
                sell = profit + dfs(i+2,-1)
                
            cooldown = dfs(i+1, curBuy)
           
            memo[(i,curBuy)] = max(buy,sell, cooldown)
            return memo[(i,curBuy)]
        return dfs(0, -1)
        
    
    