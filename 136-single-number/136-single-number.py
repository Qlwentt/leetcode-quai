class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = nums[0]
        for num in nums[1:]:
            xor = num ^ xor
            
        return xor