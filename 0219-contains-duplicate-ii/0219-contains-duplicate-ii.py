class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # [1,2,3,1] 3
        # [1,2,3,1,2,3] 2

        numsSet = set()
        L = 0
        R = 0

        while R < len(nums):
            if abs(R-L) > k:
                numsSet.remove(nums[L])
                L += 1
            if nums[R] in numsSet:
                return True
            numsSet.add(nums[R])
            R += 1
        return False




                