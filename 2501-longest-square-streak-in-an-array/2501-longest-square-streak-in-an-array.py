class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums_set = set(nums)
        
        longest = 1
        for num in nums:
            subsequence = set()
            length = 0
            cur = num
            if math.sqrt(cur) not in nums_set:
                while cur in nums_set:
                    cur = cur * cur
                    length += 1
            longest = max(length, longest)
        return longest if longest != 1 else -1
                