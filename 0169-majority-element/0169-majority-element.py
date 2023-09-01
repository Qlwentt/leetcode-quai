from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0 # 1 2 1 0 1 0 1
        candidate = nums[0] # 2, 1, 2
        
       # [2,2,1,1,1,2,2]
        
        for num in nums:
            if candidate == num:
                count += 1
            elif count == 0:
                candidate = num
                count += 1
            else:
                count -= 1
        return candidate
        