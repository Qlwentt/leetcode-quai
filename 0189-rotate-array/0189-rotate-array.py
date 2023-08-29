class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
#        k = k % len(nums)
        
#         left = nums[:-k]
#         right = nums[-k:]
#         answer = right+left
        
#         nums[:] = answer
        k = k % len(nums)
        def reverse(start, stop):
            L = start
            R = stop
            
            while L < R:
                nums[L], nums[R] = nums[R], nums[L]
                L += 1
                R -= 1
        reverse(0,len(nums)-1)
        reverse(0, k-1)
        reverse(k, len(nums)-1)
        
      # [1,2,3,4,5,6,7]
      # [7,6,5,4,3,2,1]
      #        k
      # [5,6,7,1,2,3,4]
