from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}
        for i, num in enumerate(nums):
            complement = target - num
            foundIndex = numsDict.get(complement, None)
            if foundIndex is not None:
                return [foundIndex, i]
            else:
                numsDict[num] = i

# O(n) time
# O(n) space