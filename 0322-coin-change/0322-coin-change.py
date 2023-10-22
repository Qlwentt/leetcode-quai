class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # memoization
#         memo = [[-1]*(amount) for _ in range(len(coins))]
        
#         def backtrack(i, curAmount):
#             if i >= len(coins) or curAmount > amount :
#                 return float('inf')
            
#             if curAmount == amount:
#                 return 0
            
#             if memo[i][curAmount] != -1:
#                 return memo[i][curAmount]
            
#             # choose coin between 1 and unlimited times
#             coins1 = 1 + backtrack(i, curAmount+coins[i])
#             # skip coin
#             coins2 = backtrack(i+1, curAmount)
            
#             memo[i][curAmount] =  min(coins1, coins2)
#             return memo[i][curAmount]
#         answer = backtrack(0,0)
#         print(memo)
#         return  answer if answer != float('inf') else -1 
        
#        # dp
        N = len(coins) # rows
        M = amount # cols
        
        dp = [[float('inf')]*(M+1) for _ in range(N+1)]
        
        for i in range(N+1):
            dp[i][M] = 0
            
        for i in range(N-1, -1,-1):
            for curAmount in range(M-1,-1,-1):
                if curAmount + coins[i] > amount:
                    take = float('inf')
                else:
                    take = 1 + dp[i][curAmount+coins[i]]
                skip = dp[i+1][curAmount]
                dp[i][curAmount] = min(take, skip)
        return dp[0][0] if dp[0][0] != float('inf') else -1