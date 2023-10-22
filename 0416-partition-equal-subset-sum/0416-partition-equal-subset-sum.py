
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # memoization
#         memo = {}
#         numsSum = sum(nums)
#         def backtrack(i, curTotal):
#             otherHalf = numsSum - curTotal
#             if curTotal > otherHalf:
#                 return False
#             if curTotal == otherHalf:
#                 return True
#             if i >= len(nums):
#                 return False
#             if (i, curTotal) in memo:
#                 return memo[(i, curTotal)]
            
#             # take num
#             take = backtrack(i+1, nums[i]+curTotal)
#             # skip num
#             skip = backtrack(i+1, curTotal)
            
#             memo[(i, curTotal)] = take or skip
#             return memo[(i, curTotal)]
        
#         return backtrack(0,0)

# dp
        if sum(nums) % 2:
            return False
        n = len(nums)
        half = sum(nums) // 2
        dp = [[False] * (half+1) for _ in range(n+1)]
        
        # when curTotal == half, set to True
        for i in range(n+1):
            dp[i][half] = True
        
        for i in range(n-1, -1, -1):
            for curTotal in range(half, -1, -1):
                if nums[i] + curTotal > half:
                    take = False
                else:
                    take = dp[i+1][nums[i]+curTotal]
                skip = dp[i+1][curTotal]
                dp[i][curTotal] = skip or take
                
        return dp[0][0]
        
        
            
            
            
                