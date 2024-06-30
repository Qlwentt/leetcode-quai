class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = collections.defaultdict(lambda: collections.defaultdict(int))
        result = 0
        for i in range(1, len(nums)):
            for prev in range(i - 1, -1, -1):
                remain = (nums[i] + nums[prev]) % k
                dp[i][remain] = max(dp[i][remain], dp[prev][remain] + 1)
                result = max(result, dp[i][remain] + 1)
        return result
        