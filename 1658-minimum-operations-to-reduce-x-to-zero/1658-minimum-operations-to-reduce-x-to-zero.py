class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        [1,1]
        3
        total = sum(nums)
        if total == x:
            return len(nums)
        if total < x:
            return -1
        target = total - x

        L = 0
        cur_sum = 0
        longest = float('-inf')
        for R in range(len(nums)):
            cur_sum += nums[R]
            while cur_sum > target:
                cur_sum -= nums[L]
                L += 1
            if cur_sum == target:
                longest = max(R-L+1, longest)
        return len(nums) - longest if longest != float('-inf') else -1
        
            