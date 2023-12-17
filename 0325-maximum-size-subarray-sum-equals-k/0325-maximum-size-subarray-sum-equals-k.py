class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        curSum = 0
        answer = 0
        prefixSums = {0:0}
        for R, num in enumerate(nums):
            curSum += num
            if curSum - k in prefixSums:
                L = prefixSums[curSum-k]
                answer = max(answer, R-L+1)
            prefixSums[curSum] = min(R + 1, prefixSums.get(curSum, float('inf')))
        
        return answer