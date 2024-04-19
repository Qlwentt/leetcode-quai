class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # [1,1,1,0,0,0,1,1,1,1,0]
        #            R
        #          L
        L = 0
        longest = 0
        for R in range(len(nums)):
            num = nums[R]
            k -= 1 if num == 0 else 0
            while k < 0:
                outgoing = nums[L]
                k += 1 if outgoing == 0 else 0
                L += 1
            longest = max(R-L+1, longest)
        
        return longest
        