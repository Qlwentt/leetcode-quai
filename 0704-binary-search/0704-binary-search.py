class Solution:
    def search(self, nums: List[int], target: int) -> int:
       #.  0 1 2 3 4 5  5+0 // 2
      #  [-1,0,3,5,9,12]
      #   L 
      #     R
      #       M
        L = 0
        R = len(nums) - 1
      
        while L <= R:
            mid = (L+R) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                L = mid + 1
            else:
                R = mid - 1
        return -1
        