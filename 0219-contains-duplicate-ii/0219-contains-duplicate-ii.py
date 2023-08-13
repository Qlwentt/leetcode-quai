class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
#         numsDict = {}
        
#         for i,num in enumerate(nums):
#             j = numsDict.get(num, None)
#             if j != None and (abs(i-j) <= k):
#                 return True
#             else:
#                 numsDict[num] = i
        
#         return False

        numsSet = set()
        L = 0
        R = 0
        
        while R < len(nums):
            if abs(L-R) > k:
                numsSet.remove(nums[L])
                L += 1
            if nums[R] in numsSet:
                return True
            numsSet.add(nums[R])
            R += 1
        return False



                