class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # memoization
        memo = {}
        def dfs(i, curTotal):
            if i >= len(coins) or curTotal > amount:
                return 0
            
            if curTotal == amount:
                return 1
            
            if (i, curTotal) in memo:
                return memo[(i,curTotal)]
            # choose coin between 1 and unlimited times
            take = dfs(i, curTotal + coins[i])
            
            # skip coin
            skip = dfs(i+1, curTotal)
            
            memo[(i, curTotal)] = take+skip
            return memo[(i, curTotal)]
        return dfs(0, 0)