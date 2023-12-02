class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findFirst(nums, target):
            L = 0
            R = len(nums) - 1
            
            while L <= R:
                mid = (L + R) // 2
                
                if nums[mid] >= target:
                    R = mid - 1
                else:
                    L = mid + 1
            return L
        
        def findLast(nums, target):
            L = 0
            R = len(nums) - 1
            
            while L <= R:
                mid = (L + R) // 2
                
                if nums[mid] > target:
                    R = mid - 1
                else:
                    L = mid + 1
            return R
        
        start = findFirst(nums, target)
        end = findLast(nums,target)
        
        return [start,end] if (start in range(len(nums)) and nums[start] == target) else [-1,-1]