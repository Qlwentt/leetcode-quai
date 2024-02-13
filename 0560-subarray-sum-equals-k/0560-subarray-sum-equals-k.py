from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixDict = defaultdict(int)
        prefixDict[0] = 1
        
        curSum = 0
        answer = 0
        for num in nums:
            curSum += num
            if curSum - k in prefixDict:
                answer += prefixDict[curSum-k]
            prefixDict[curSum] += 1
            
        return answer