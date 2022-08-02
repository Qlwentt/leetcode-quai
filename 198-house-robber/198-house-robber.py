class Solution:
    def __init__(self):
        self.memo = {}
    def rob(self, nums: List[int]) -> int:
        def robHelper(i):
            if i >= len(nums):
                return 0
            if i not in self.memo:            
                self.memo[i] = max(robHelper(i+2) + nums[i], robHelper(i+1))
            return self.memo[i]
        return robHelper(0)
        