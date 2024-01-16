class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comps = {}
        
        for i, num in enumerate(nums):
            comp = target - num
            if comp in comps:
                return [i, comps[comp]]
            comps[num] = i
            
        return -1