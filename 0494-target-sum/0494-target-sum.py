class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # memoization
        memo = {}
        def dfs(i, curSum):
            if curSum == target and i >= len(nums):
                return 1
            if i >= len(nums):
                return 0
            if (i, curSum) in memo:
                return memo[(i, curSum)]
           
            # add
            add = dfs(i+1, curSum + nums[i])
            
            # subtract
            
            subtract = dfs(i+1, curSum - nums[i])
            
            memo[(i,curSum)] = add + subtract
            return memo[(i, curSum)]
        
        return dfs(0,0)            
            