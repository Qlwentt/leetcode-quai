class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # [1,1,2,2,3,1]
        #          L
        #            R
        eles = 0 # 1 2 3 1 2 1
        L = 0
        R = 0
        k = 0 # 1 2
        prev = float("inf") # 1 1 1 2 2
        while R < len(nums):
            if prev == nums[R]:
                eles += 1
            else: 
                eles = 1
            prev = nums[R]
            if eles < 3:
                nums[L], nums[R] = nums[R], nums[L]
                k += 1
                L += 1
            R += 1
        return k
                