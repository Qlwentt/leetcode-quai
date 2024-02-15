class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainderDict = {0: -1}
        
        runSum = 0
        for R, num in enumerate(nums):
            runSum += num
            if runSum % k in remainderDict:
                L = remainderDict[runSum % k]
                if R - L >= 2:
                    return True
            else:
                remainderDict[runSum % k] = R
        
        return False
                