class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        rev_sorted_nums = sorted(nums,reverse=True)
        answer = 0
        for a, b in zip(sorted_nums, rev_sorted_nums):
            answer = max(answer, a+b)
        
        return answer