class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        counts = {0:0, 1:0}    # [1,1,2,1,1] [2,2,2,1,2,2,1,2,2,2]
                               #  L           L     M      
                                         # R              R
        L = 0
        nice = 0
        R2 = None
        for R in range(len(nums)):
            counts[nums[R]%2]+= 1
            while counts[1] == k:
                R2 = R + 1
                while  R2 < len(nums) and nums[R2] % 2 != 1:
                    R2 += 1
                        
                nice += R2 - R
                counts[nums[L]%2] -= 1
                L += 1
                
        return nice