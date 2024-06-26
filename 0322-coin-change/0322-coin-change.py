class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
#         @cache
#         def dp(i, cur_amount):
#             if cur_amount == 0:
#                 return 0
#             if cur_amount < 0:
#                 return float('inf')
#             if i == len(coins):
#                 return float('inf')
            
#             # take
#             take = 1 + dp(i, cur_amount - coins[i])
            
#             # stop taking
#             skip = dp(i+1, cur_amount)
            
#             return min(take, skip)
        
#         answer = dp(0, amount)
#         return answer if answer != float('inf') else -1

        dp = collections.defaultdict(lambda: collections.defaultdict(lambda : float('inf')))
        for i in range(len(coins)):
            dp[i][0] = 0
        
        for i in range(len(coins)-1,-1,-1):
            for cur_amount in range(1, amount+1):
                take = 1 + dp[i][cur_amount-coins[i]]
                skip = dp[i+1][cur_amount]
                dp[i][cur_amount] = min(take, skip)
        ans = dp[0][amount]
        return ans if ans != float('inf') else -1