from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0]*len(nums)
        
        pre = 1
        for i in range(len(nums)):
            multiplier = nums[i-1] if i > 0 else 1
            pre = pre * multiplier
            output[i] = pre
        post = 1
        for i in range(len(nums) -1, -1, -1):
            multiplier = nums[i+1] if i < len(nums) - 1 else 1
            post = post * multiplier
            output[i] = output[i] * post
        return output
# O(n) time
# O(1) space