class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def helper(i):
            if i >= len(nums):
                return 0
            
            take = nums[i] + helper(i+2)
            skip = helper(i+1)
            return max(take, skip)
        return helper(0)
        