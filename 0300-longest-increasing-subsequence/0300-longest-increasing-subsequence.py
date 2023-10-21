class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # not optimal memoization - TLE
#         memo = {i: {} for i in range(len(nums))}
#         def backtrack(i, prev):
#             if i >= len(nums):
#                 return 0
            
#             if prev in memo[i]:
#                 return memo[i][prev]

#             take = 0
#             num = nums[i]
#             if num > prev:
#                 # take number
#                 take = 1 + backtrack(i+1, num)
#             # skip number
#             skip = backtrack(i+1, prev)

#             memo[i][prev] = max(take,skip)
#             return memo[i][prev]
        
#         return backtrack(0, float('-inf'))

# memoization
#         memo = {}
#         def backtrack(i):
#             if i >= len(nums):
#                 return 0
            
#             if i in memo:
#                 return memo[i]
            
#             maxTake = 1
#             for j in range(i+1, len(nums)):
#                 take = 1
#                 if nums[i] < nums[j]:
#                     take += backtrack(j)
#                     maxTake = max(take,maxTake)
                                
#             memo[i] = maxTake
#             return memo[i]
        
#         answer = 1
#         for i in range(len(nums)):
#             answer = max(answer, backtrack(i))
#         return answer

# dp
        n = len(nums)
        dp = [1] * (n)
        
        for i in range(n-1, -1,-1):
            for j in range(n-1, i-1, -1):
                a = nums[i]
                b = nums[j]
                if a < b:
                    dp[i] = max(dp[i], 1 + dp[j])
        
        return max(dp)                
        
        

        