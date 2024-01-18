class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        
       # [100,4,200,1,3,2]
        longest = 0
        for num in nums:
            if num - 1 not in numsSet:
                length = 1
                while num + 1 in numsSet:
                    length += 1
                    num += 1
                longest = max(length, longest)
        return longest
        