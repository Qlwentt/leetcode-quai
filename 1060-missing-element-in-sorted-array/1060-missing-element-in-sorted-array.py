class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        
        def missingNums(start, end):
            return nums[end] - nums[start] - end
        
        L, R = 0, len(nums) - 1
        
        while L <= R:
            mid = (L + R) // 2
            
            if missingNums(0,mid) >= k:
                R = mid - 1
            else:
                L = mid + 1
        return nums[0] + k - 1 + L