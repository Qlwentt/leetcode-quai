class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
       # [1,1,1,0,0,0,1,1,1,1,0]
       #  L
       #  R
    
        L = 0
        maxLen = 0
        for R in range(len(nums)): 
            k -= 1 if nums[R] == 0 else 0
            while k < 0:
                k += 1 if nums[L] == 0 else 0
                L += 1
            maxLen = max(maxLen, R-L+1)
        
        return maxLen