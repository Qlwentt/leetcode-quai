class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        L = 0
        answer = 0
        for R in range(len(nums)):
            k -= 1 if nums[R] == 0 else 0
            while k < 0:
                k += 1 if nums[L] == 0 else 0
                L += 1
            answer = max(answer, R - L + 1)
        
        return answer