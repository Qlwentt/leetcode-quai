class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comps = {}
        for i, num in enumerate(nums):
            if target - num in comps:
                return comps[target-num], i
            comps[num] = i
        return -1