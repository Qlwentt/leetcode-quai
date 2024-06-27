class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

# memoization
        # @cache
        # def backtrack(i):
        #     if i >= len(nums):
        #         return 0
        #     max_take = 1
        #     for j in range(i+1, len(nums)):
        #         if nums[i] < nums[j]:
        #             take = 1 + backtrack(j)
        #             max_take = max(max_take, take)
        #     return max_take
        # answer = 1
        # for i in range(len(nums)):
        #     answer = max(backtrack(i), answer)
        # return answer
        

# dp
        n = len(nums)
        dp = collections.defaultdict(int)
        
        for i in range(n-1,-1,-1):
            max_take = 1
            for j in range(i+1,n):
                if nums[i] < nums[j]:
                    take = 1 + dp[j]
                    max_take = max(max_take, take)
            dp[i] = max_take
        
        return max(dp.values())
        

        