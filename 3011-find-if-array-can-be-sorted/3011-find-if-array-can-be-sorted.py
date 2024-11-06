class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        set_bits = {}
        
        def get_set_bits(x):
            count = 0
            while x:
                count += x & 1
                x = x >> 1
            return count
        
        for num in nums:
            set_bits[num] = get_set_bits(num)
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] <= nums[i]:
                    if set_bits[nums[i]] == set_bits[nums[j]]:
                        nums[i], nums[j] = nums[j], nums[i]
                    else:
                        return False
        return True
            
        
        