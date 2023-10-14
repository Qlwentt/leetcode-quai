class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n+2)
        dp[n-1] = cost[n-1]
        
        i = n - 2
        while i >= 0:
            dp[i] = min(cost[i] + dp[i+1], cost[i] + dp[i+2])
            i -= 1
        print(dp)
        return min(dp[0], dp[1])