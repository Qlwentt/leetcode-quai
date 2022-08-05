class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        maxProduct = nums[0]
        minProduct = nums[0]
        for i in range(1, len(nums)):
            temp = maxProduct
            maxProduct = max(maxProduct * nums[i], minProduct * nums[i], nums[i])
            minProduct = min(temp * nums[i], minProduct * nums[i], nums[i])
            res = max(res, maxProduct)
        return res
            