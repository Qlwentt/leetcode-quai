class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_nums = [None] * (len(nums) * 2)
        for i, num in enumerate(nums):
            new_nums[i] = num
            new_nums[i+len(nums)] = num
        return new_nums
        