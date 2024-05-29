class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        L = 0
        R = len(nums) - 1
        answer = 0
        while L < R:
            a = nums[L]
            b = nums[R]
            answer = max(a+b, answer)
            L += 1
            R -= 1
        return answer
            