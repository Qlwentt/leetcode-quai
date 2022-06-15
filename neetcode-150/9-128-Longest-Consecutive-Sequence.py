from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        
        longest = 0
        
        for num in nums:
            if num - 1 not in numsSet:
                length = 1
                while num + length in numsSet:
                    length += 1
                longest = max(longest, length)
        return longest

# O(n) time
# O(n) space