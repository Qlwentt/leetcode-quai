class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        seq_sum = nums[0]
        nums_set = set(nums)
        prev = nums[0]
        for i, num in enumerate(nums[1:]):
            if prev + 1 == num:
                seq_sum += num
            else:
                break
            prev = num
            
        
        for i in range(seq_sum, max(max(nums)+1, seq_sum +1)):
            if i not in nums_set:
                return i
        
        return max(nums) + 1
            
            
                