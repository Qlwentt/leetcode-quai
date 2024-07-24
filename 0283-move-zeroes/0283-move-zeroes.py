class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
     #   [0,1,0,3,12]
      #  P
      #  Q
        
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left] = nums[right]
                if right != left:
                    nums[right] = 0
                left += 1
        
# Time: O(N)
# Space: O(1)
