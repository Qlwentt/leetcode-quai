class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in numsSet:
                cur = num
                length = 0
                while cur in numsSet:
                    length += 1
                    longest = max(longest, length)
                    cur = cur + 1
        return longest
