class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        counts = [0 for _ in range(len(nums)+1)]
        for num in nums:
            counts[num] += 1
        
        twice = None
        missing = None
        for num in range(1,len(counts)):
            if counts[num] == 0:
                missing = num
            if counts[num] == 2:
                twice = num
        
        return [twice, missing]

