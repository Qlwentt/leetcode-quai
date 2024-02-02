class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
       # [1,1,1,0,0,0,1,1,1,1,0]
       #  L
       #  R
    
        L = 0
        maxLen = float("-inf")
        for R in range(len(nums)):
            decrK = 1 if nums[R] == 0 else 0
            k -= decrK
            while k < 0:
                incrK = 1 if nums[L] == 0 else 0
                k += incrK
                L += 1
            maxLen = max(maxLen, R-L+1)
        
        return maxLen