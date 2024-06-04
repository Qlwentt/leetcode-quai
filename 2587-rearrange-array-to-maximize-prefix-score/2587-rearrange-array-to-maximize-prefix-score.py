class Solution:
    def maxScore(self, nums: List[int]) -> int:
        
        nums.sort(reverse=True)
        
        curSum = 0
        score = 0
        for i, num in enumerate(nums):
            curSum += num
            if curSum > 0:
                score += 1
        return score
        