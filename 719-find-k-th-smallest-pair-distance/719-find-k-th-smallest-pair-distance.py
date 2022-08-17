class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        
        def isPossibleKth(guess,):
            left = 0
            count = 0
            for right in range(1, len(nums)):
                while nums[right] - nums[left] > guess:
                    left += 1
                count += (right - left)
            return count >= k
        
        low = 0
        high = nums[-1] - nums[0]
        
        while low < high:
            mid = (high + low) // 2
            if isPossibleKth(mid):
                high = mid
            else:
                low = mid + 1
        return low
            