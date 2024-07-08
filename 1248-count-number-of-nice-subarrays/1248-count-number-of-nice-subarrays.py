class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
                               # [1,1,2,1,1] [2,2,2,1,2,2,1,2,2,2]
                               #  L           L     M      
                                         # R              R
        odd = 0
        L = 0
        nice = 0
        R2 = None
        for R in range(len(nums)):
            odd += nums[R] % 2 
            while odd == k:
                R2 = R + 1
                while  R2 < len(nums) and nums[R2] % 2 != 1:
                    R2 += 1
                        
                nice += R2 - R
                odd -= nums[L] % 2
                L += 1
                
        return nice