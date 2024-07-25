class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last_unique = None
        l = 0
        for r in range(len(nums)):
            if nums[r] != last_unique:
                last_unique = nums[r]
                nums[r], nums[l] = nums[l], nums[r]
                l += 1
        return l
                