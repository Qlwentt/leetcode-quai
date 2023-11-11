class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = len(nums)
        for i,num in enumerate(nums):
            result = result ^ i ^ num
        
        return result
            
            