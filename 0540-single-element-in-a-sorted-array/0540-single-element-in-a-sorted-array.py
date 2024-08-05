class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # [1,1,2,3,3,4,4,8,8]  [3,3,7,7,10,11,11] # 
        #                       l     m       r
       # l 
     #                     r
      #          m
        l = 0
        r = len(nums) -1   
        
        while l < r:
            mid = (l+r) // 2
            if  nums[mid+1] == nums[mid]:
                if (r - mid) % 2 == 1:
                    r = mid - 1
                else:
                    l = mid + 2
            elif nums[mid-1] == nums[mid]:
                if (r-mid) % 2 == 1 :
                    l = mid + 1
                else:
                    r = mid - 2
            else:
                return nums[mid]
            
        return nums[l]
            