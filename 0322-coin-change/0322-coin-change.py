class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dp(i, cur_amount):
            if cur_amount == 0:
                return 0
            if cur_amount < 0:
                return float('inf')
            if i == len(coins):
                return float('inf')
            
            # take
            take = 1 + dp(i, cur_amount - coins[i])
            
            # stop taking
            skip = dp(i+1, cur_amount)
            
            return min(take, skip)
        
        answer = dp(0, amount)
        return answer if answer != float('inf') else -1
    