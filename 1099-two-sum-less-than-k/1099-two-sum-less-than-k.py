class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        low = 0
        high = len(nums) -1
        best = -1
        while low < high:
            total = nums[low] + nums[high]
            if total >= k:
                high -= 1
            else:
                best = max(best, total)
                low += 1
        return best