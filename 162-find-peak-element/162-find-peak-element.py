class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = (start + end) // 2
            num = nums[mid]
            leftNeigh = nums[mid - 1] if mid - 1 >= 0 else float('-inf')
            rightNeigh = nums[mid + 1] if mid + 1 < len(nums) else float('-inf')
            
            if num > leftNeigh and num > rightNeigh:
                return mid
            elif num > leftNeigh and num < rightNeigh:
                start = mid + 1
            else:
                end = mid - 1
        