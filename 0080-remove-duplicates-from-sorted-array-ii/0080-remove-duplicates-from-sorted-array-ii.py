class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # [1,1,1,2,2,3]
        # [1,1,2,2,3,_]
        # [1,1,2,2,3,1]
                   # L
                   #   R
        eles = 0
        L = 0
        R = 0
        k = 0
        prev = float("inf")
        while R < len(nums):
            if prev == nums[R]:
                eles += 1
            else: 
                eles = 1
            prev = nums[R]
            if prev != nums[R] or eles < 3:
                nums[L], nums[R] = nums[R], nums[L]
                k += 1
                L += 1
            R += 1
        return k
                