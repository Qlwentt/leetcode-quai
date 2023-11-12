from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0]*3
        for num in nums:
            count[num] += 1   
        
        i = 0
        for key in range((len(count))):
            for _ in range(count[key]):
                nums[i] = key
                i += 1
        return nums