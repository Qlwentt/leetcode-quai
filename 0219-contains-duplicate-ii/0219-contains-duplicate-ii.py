class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # [1,2,3,1] 3
        # [1,1,3,1,2,3] 2
     #.    L
     #.      R
        
       # [1,0,1,1] 1
       #.   L
       #        R
        
        L = 0
        R = 0
        numsSet = set()
        
        while R < len(nums):
            while abs(L-R) > k:
                numsSet.remove(nums[L])
                L += 1
            if nums[R] in numsSet:
                return True
            numsSet.add(nums[R])
            R += 1
            
        return False
                
        




                