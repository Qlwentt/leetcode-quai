from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        setNums = set(nums)
        return len(setNums) != len(nums)

# O(n) time
# O(n) space