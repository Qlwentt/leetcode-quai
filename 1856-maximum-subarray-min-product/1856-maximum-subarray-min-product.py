class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        nums.append(0)
        prefix_sums = [0] * (len(nums) + 1)
        
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum += nums[i] 
            prefix_sums[i+1] = cur_sum
       
        stack = []
        max_min_product = 0
        for i, num in enumerate(nums):
            start = i
            while stack and stack[-1][1] > num:
                j, val = stack.pop()
                max_min_product = max(val * (prefix_sums[i] - prefix_sums[j]), max_min_product)
                start = j
            stack.append((start,num))
        return max_min_product % (10 ** 9 + 7)