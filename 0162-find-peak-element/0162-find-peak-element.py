class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        L = 0
        R = len(nums) -1
        
        while L <= R:
            M = (L + R) // 2
            [3,2,1]
            # if left neighbor is greater search on the left
            if M > 0 and nums[M-1] > nums[M]:
                R = M - 1
            # if right neighbor is greater search on the right
            elif M < len(nums) -1 and nums[M+1] > nums[M]:
                L = M + 1
            else: # it is greater than left and right - found peak element
                return M
                