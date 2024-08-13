class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
                
        l = 0
        r = len(nums) - 1

#         more intuitive solution for this problem
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
        return l
    
# shorter solution and works for other problems like LC 34       
#         while l <= r:
#             mid = (l+r) // 2
            
#             if nums[mid] >= target:
#                 r = mid - 1
#             else:
#                 l = mid + 1
#         return l