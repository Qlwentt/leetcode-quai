class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if (k*2) + 1 > len(nums):
            return [-1] * len(nums)
        curSum = 0
        L = 0
        windowLen = (k * 2) + 1
        answer = [-1] * k
        for R in range(len(nums)):
            curSum += nums[R]
            if R - L + 1 == windowLen:
                answer.append(int(curSum/windowLen))
                curSum -= nums[L]
                L += 1
            
        return answer + [-1] * k
                