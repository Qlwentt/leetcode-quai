class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        nums.sort(reverse=True)
        
        for num in nums:
            if count[num] == 1:
                return num
        return -1