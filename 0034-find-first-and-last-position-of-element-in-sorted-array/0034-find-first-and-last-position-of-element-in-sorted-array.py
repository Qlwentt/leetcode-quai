class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        L = 0
        R = len(nums) - 1

        while L <= R:
            mid = (L+R) // 2

            if nums[mid] >= target:
                R = mid - 1
            else:
                L = mid + 1

        ansL = L if L in range(len(nums)) and nums[L] == target else -1
        if ansL == -1:
            return [-1,-1]
        L = 0
        R = len(nums) - 1

        while L <= R:
            mid = (L+R) // 2

            if nums[mid] <= target:
                L = mid + 1
            else:
                R = mid - 1
        ansR = R
        return [ansL, ansR]