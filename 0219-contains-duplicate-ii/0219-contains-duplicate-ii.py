class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numsDict = {}
        
        for i,num in enumerate(nums):
            j = numsDict.get(num, None)
            if j != None and (abs(i-j) <= k):
                return True
            else:
                numsDict[num] = i
        
        return False