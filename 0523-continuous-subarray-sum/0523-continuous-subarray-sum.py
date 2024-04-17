class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefixDict = {}
        prefixDict[0] = -1
        
        curSum = 0
        for R, num in enumerate(nums):
            curSum += num
            if curSum%k in prefixDict:
                L = prefixDict[curSum % k]
                if R - L >= 2:
                    return True
            else:  
                prefixDict[curSum %k] = R
        
        return False
        