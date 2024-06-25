class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operations = 0
        for num in nums:
            real_num = num ^(operations % 2)
            if real_num == 0:
                operations += 1
        return operations