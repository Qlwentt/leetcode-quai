class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        for i, num in enumerate(nums):
            if target - num in numDict:
                return [numDict[target-num], i]
            numDict[num] = i
        