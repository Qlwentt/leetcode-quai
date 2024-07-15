class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        L = 0
        longest = 0
        counts = collections.defaultdict(int)
        
        for R in range(len(nums)):
            counts[nums[R]] += 1
            while counts[nums[R]] > k:
                counts[nums[L]] -= 1
                L += 1
            longest = max(R-L+1, longest)
        
        return longest