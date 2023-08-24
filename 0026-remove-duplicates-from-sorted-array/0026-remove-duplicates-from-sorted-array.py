class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # [0,0,1,1,1,2,2,3,3,4]
        # [0,1,2,3,4,_,_,_,_,_]
        # [0,1,2,3,4,0,2,1,3,1]
                   # L
                   #           R
        k = 0            
        L = 0
        R = 0
        prev = float("inf")
        while R < len(nums):
            if nums[R] != prev:
                k += 1
                prev = nums[R]
                nums[L], nums[R] = nums[R], nums[L]
                L += 1
            R += 1
        return k
            