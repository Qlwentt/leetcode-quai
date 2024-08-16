class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comps = {}
        
        for i, num in enumerate(nums):
            if target - num in comps:
                return [i, comps[target-num]]
            comps[num] = i
        