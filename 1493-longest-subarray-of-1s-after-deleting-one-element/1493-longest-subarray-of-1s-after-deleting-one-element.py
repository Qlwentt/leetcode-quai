class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        L = 0
        counts = {0:0, 1:0}
        longest = 0
        for R in range(len(nums)):
            counts[nums[R]] += 1
            while counts[0] > 1:
                counts[nums[L]] -= 1
                L += 1
            if counts[0]:
                longest = max(longest, counts[1])
            else:
                longest = max(longest, counts[1]-1)
        return longest
            