from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        
        while True:
            currentSum = numbers[left] + numbers[right]
            if currentSum > target:
                right -= 1
            elif currentSum < target:
                left += 1
            else: # if it is equal
                return [left + 1, right + 1]
            
# O(n) time
# O(1) space