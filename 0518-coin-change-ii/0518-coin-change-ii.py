class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # memoization
#         memo = {}
#         def dfs(i, curTotal):
#             if i >= len(coins) or curTotal > amount:
#                 return 0
            
#             if curTotal == amount:
#                 return 1
            
#             if (i, curTotal) in memo:
#                 return memo[(i,curTotal)]
#             # choose coin between 1 and unlimited times
#             take = dfs(i, curTotal + coins[i])
            
#             # skip coin
#             skip = dfs(i+1, curTotal)
            
#             memo[(i, curTotal)] = take+skip
#             return memo[(i, curTotal)]
#         return dfs(0, 0)
    
        # dp

        # row = index
        # col = amount
        n = len(coins)
        m = amount
        dp = [[0]* (amount+1) for _ in range(n+1)]

        for i in range(n+1):
            dp[i][m] = 1

        for i in range(n-1,-1,-1):
            for curTotal in range(m-1, -1, -1):
                if coins[i] + curTotal > amount:
                    take = 0
                else:
                    take = dp[i][curTotal+coins[i]]
                skip = dp[i+1][curTotal]
                dp[i][curTotal] = skip + take
        return dp[0][0]
    