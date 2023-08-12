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
        L = 0
        R = 1
        numsSet = set([nums[L]])    

        while R < len(nums):            
            if abs(L-R) > k:
                numsSet.remove(nums[L])
                L += 1       
            if nums[R] in numsSet and abs(L-R) <= k:
                return True
            numsSet.add(nums[R])
            R += 1
        return False

                