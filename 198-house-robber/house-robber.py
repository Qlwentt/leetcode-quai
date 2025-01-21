class Solution:
    def rob(self, nums: List[int]) -> int:

        # Top Down Memoization
        cache = {}
        def dp(i):
            if i >= len(nums):
                return 0
            if i in cache:
                return cache[i]

            take = nums[i] + dp(i+2)
            skip = dp(i+1)
            result =  max(take,skip)
            cache[i] = result
            return result

        return dp(0)

        # Bottom Up - Tabulation

        # dp = defaultdict(int)
        # for i in range(len(nums)-1,-1,-1):
        #     take = nums[i] + dp[i+2]
        #     skip = dp[i+1]
        #     dp[i] = max(take, skip)

        # return dp[0]
    
    
        