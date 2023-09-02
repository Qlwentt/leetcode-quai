from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSumDict = defaultdict(int)
        prefixSumDict[0] = 1
        
        prefixSum = 0
        answer = 0
        for num in nums:
            prefixSum += num
            answer += prefixSumDict[prefixSum-k]
            prefixSumDict[prefixSum] += 1
        
        return answer
            
            