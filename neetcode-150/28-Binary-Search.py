from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        
        
        while end >= start:
            mid = start + (end - start) // 2
            
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else: # nums[mid] == target
                return mid
        return -1

# O(log(n)) time
# O(1) space