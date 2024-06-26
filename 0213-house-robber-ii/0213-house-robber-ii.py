class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def helper(i, nums, memo):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            take = nums[i] + helper(i+2, nums, memo)
            skip = helper(i+1, nums, memo)
            ans = max(take,skip)
            memo[i] = ans
            return ans
        if len(nums) >= 2:
            return max(helper(0, nums[:-1], {}), helper(1, nums, {}))
        return nums[0] 
        