class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 1 if nums else 0
    
        for num in nums:
            nothingBefore = (num - 1) not in numsSet
            somethingAfter = (num + 1) in numsSet
            if nothingBefore and somethingAfter:
                node = num
                length = 0
                while (node + 1) in numsSet:
                    length += 1
                    node = node + 1
                longest = max(length + 1, longest)
        return longest
