class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        nums_dict = collections.defaultdict(int)
        cur_sum = 0
        L = 0
        max_sum = 0
        for R in range(len(nums)):
            if R-L+1 > k:
                nums_dict[nums[L]] -= 1
                if nums_dict[nums[L]] == 0:
                    del nums_dict[nums[L]]
                cur_sum -= nums[L]
                L += 1
            cur_sum += nums[R]
            nums_dict[nums[R]] += 1
            if R-L+1 == k and len(nums_dict) == k:
                max_sum = max(cur_sum, max_sum)
        return max_sum