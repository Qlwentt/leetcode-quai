class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # [3,3,2,3] 3
        #  L
        #      R
        # [2,3,3,3]

        # [1,3,0,4,2,2,2,2] 2 
        #          L
        #                R
        L = 0
        R = 0
        k = 0 # 1 2 3 4
        while R < len(nums):
            if nums[L] == val:
                while nums[R] == val:
                    R +=1
                    if R >= len(nums):
                        return k
                nums[L], nums[R] = nums[R], nums[L]
            else:
                R += 1
            k += 1
            L += 1
        return k
        