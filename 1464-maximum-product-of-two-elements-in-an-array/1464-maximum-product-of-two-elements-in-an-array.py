class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first = max(nums)
        nums.pop(nums.index(first))
        second = max(nums)
        
        return (first-1) * (second-1)