class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = { i: {} for i in range(len(coins))}
        
        def backtrack(i, curAmount):
            if i >= len(coins) or curAmount > amount :
                return float('inf')
            
            if curAmount == amount:
                return 0
            
            if curAmount in memo[i]:
                return memo[i][curAmount]
            
            # choose coin between 1 and unlimited times
            coins1 = 1 + backtrack(i, curAmount+coins[i])
            # skip coin
            coins2 = backtrack(i+1, curAmount)
            
            memo[i][curAmount] =  min(coins1, coins2)
            return memo[i][curAmount]
        answer = backtrack(0,0)
        return  answer if answer != float('inf') else -1 

            