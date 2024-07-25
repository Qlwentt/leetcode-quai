class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        last_unique = float('inf')
        k = 0
        for r in range(len(nums)):
            if nums[r] != last_unique:
                last_unique = nums[r]
                nums[r], nums[l] = nums[l], nums[r]
                k += 1
                l += 1
        return k
                