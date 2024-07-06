class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float('inf')
        cur_sum = 0
        L = 0
        for R in range(len(nums)):
            cur_sum += nums[R]
            while cur_sum >= target:
                min_length = min(R-L+1, min_length)
                cur_sum -= nums[L]
                L += 1
        return min_length if min_length != float('inf') else 0
                