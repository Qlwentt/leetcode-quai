class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = len(nums)
        
        for i, num in enumerate(nums):
            result ^= i ^ num
            
        return result