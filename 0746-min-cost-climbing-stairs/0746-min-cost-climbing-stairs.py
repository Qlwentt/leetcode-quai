class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n+2)
        dp[n-1] = cost[-1]

        i = n-2
        while i >= 0:
            dp[i] = cost[i] + min(dp[i+1], dp[i+2])
            i -= 1
        
        return min(dp[0], dp[1])