class Solution:
    def findMin(self, nums: List[int]) -> int:
#    [5,1,2,3,4]
#    [4,5,1,2,3]
#    [3,4,5,1,2]
#    [2,3,4,5,1]
#    [1,2,3,4,5]


#    [3,1,2]    [4,5,1,2,3] [3,4,5,1,2] [2,3,4,5,1] [1,2,3,4,5]
#                                        L   M   R
#     L M R
        def getPivot():
        
            L = 0
            R = len(nums) - 1
            
            if nums[L]< nums[R] or L == R:
                return R

            while L <= R:
                mid = (L+R) // 2

                next_ = nums[mid+1] if mid < len(nums) -1 else float("inf")
                
                if next_ < nums[mid]:
                    return mid
                elif nums[mid] < nums[R] and nums[R] < nums[L]:
                    R = mid - 1
                else:
                    L = mid + 1
                    
        pivot = getPivot()
        return nums[pivot + 1] if pivot != len(nums) -1 else nums[0]
        
        