class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        answer = 0
        L = 0
        prev = None
        for R in range(len(nums)):
            if prev is not None and prev == nums[R]:
                L = R
            answer += R - L + 1
            prev = nums[R]
        return answer