class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [4,5,6,7,0,1,2] 
      #    L     M     R
            
        L = 0
        R = len(nums) - 1
        
        while L <= R:
            mid = (L + R) // 2
            if nums[mid] == target:
                return mid
           
            # is the array sorted between L and M ?
            if nums[L] <= nums[mid]:
                # search right
                if target > nums[mid] or target < nums[L]:
                    L = mid + 1
                # search left
                else:
                    R = mid - 1
            # array is sorted between M and R
            else:
                # search left
                if target < nums[mid] or target > nums[R]:
                    R = mid - 1
                # search right
                else:
                    L = mid + 1
            
        return -1