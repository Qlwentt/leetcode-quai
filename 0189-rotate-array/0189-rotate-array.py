class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        
        left = nums[:-k]
        right = nums[-k:]
        print(left)
        print(right)
        answer = right+left
        
        nums[:] = answer
        
      #   [4,5,6,7,2,3,1] 
      # #        L           
      # #              R 
      #   [7,1,2,3,4,5,6]
      #   [6,7,1,2,3,4,5]
      #   [5,6,7,1,2,3,4]
      #   [4,5,6,7,1,2,3]
      #   [3,4,5,6,7,1,2]
      #   [2,3,4,5,6,7,1]
        