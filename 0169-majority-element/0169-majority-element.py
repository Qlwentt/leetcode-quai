from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = len(nums) // 2 + 1
        counter = Counter(nums)
        
        for num, count in counter.items():
            if count >= majority:
                return num
        return -1
        
        