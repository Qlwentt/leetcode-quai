class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        nums = list(counts.keys())
        nums.sort()
        n = len(nums)
        next_i = [n] * n
        
        p = 0
        for q in range(n):
            while nums[q] > nums[p] + 1:
                next_i[p] = q
                p += 1
#         @cache      
#         def dp(i):
#             if i == len(nums):
#                 return 0
            
#             take = counts[nums[i]] * nums[i] + dp(next_i[i])
#             skip = dp(i+1)
            
#             return max(take, skip)
        
#         return dp(0)

        dp = collections.defaultdict(int)
        n = len(nums)
        for i in range(n-1,-1,-1):
            take = counts[nums[i]] * nums[i] + dp[next_i[i]]
            skip = dp[i+1]
            dp[i] = max(take, skip)
        return dp[0]
        
        
        
        