class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # [1,2,3,1] 3
        # [1,2,3,1,2,3] 2
     #.    L
     #.        R
        
       # [1,0,1,1] 1
       #.   L
       #        R
        
        L = 0
        numsSet = set()
        for R in range(len(nums)):
            while R-L+1 > k+1:
                numsSet.remove(nums[L])
                L += 1
            if nums[R] in numsSet:
                return True
            numsSet.add(nums[R])
        return False
            
                
        




                