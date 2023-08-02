class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        setNums = set(nums)
        return len(setNums) != len(nums)
        