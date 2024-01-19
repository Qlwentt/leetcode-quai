from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSums = defaultdict(int)
        prefixSums[0] = 1

        curSum = 0
        answer = 0
        for num in nums:
            curSum += num
            if curSum - k in prefixSums:
                answer += prefixSums[curSum - k]
            prefixSums[curSum] += 1
        
        return answer
    
    
    # Time: O(n)
    # Space: O(n)
    
    # had to look up the solution on neetcode