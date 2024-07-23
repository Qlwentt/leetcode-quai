class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                # without python magic
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp

                # python magic way to swap variables
                # nums[left], nums[right] = nums[right], nums[left]
                left += 1
        
# Time: O(N)
# Space: O(1)
