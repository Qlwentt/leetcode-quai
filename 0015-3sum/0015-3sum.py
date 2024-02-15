class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answers = set()
        target = 0
        
        for i in range(len(nums)):
            lo = i + 1
            hi = len(nums) - 1
            while lo < hi:
                if nums[lo] + nums[hi] + nums[i] > target:
                    # too hi decrease sum
                    hi -= 1
                elif nums[lo] + nums[hi] + nums[i] < target:
                    # too low, increase sum
                    lo += 1
                else: # found match
                    answers.add(tuple(sorted([nums[lo], nums[hi], nums[i]])))
                    lo += 1
                    hi -= 1
        return list(answers)
        