class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # [1,3,5,6]
        #        R
        #  L
                
        l = 0
        r = len(nums) - 1
        
#         while l <= r:
#             mid = (l+r) // 2
            
#             if nums[mid] >= target:
#                 r = mid - 1
#             else:
#                 l = mid + 1
#         return l

        while l <= r:
            mid = (l+r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
        return l