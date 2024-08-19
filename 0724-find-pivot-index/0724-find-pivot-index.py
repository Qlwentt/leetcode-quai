class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
    # [0,  1, 8,11,17,22]
    # [27,20,17,11,6, 0]
    
        cur_sum = 0
        left = []
        for num in nums:
            left.append(cur_sum)
            cur_sum += num
        
        cur_sum = 0
        right = [0] * len(nums)
        
        for i in range(len(nums)-1,-1,-1):
            right[i] = cur_sum
            cur_sum += nums[i]
        
        for i in range(len(left)):
            if left[i] == right[i]:
                return i
            
        return -1
# Time: O(N)
# Space: O(N)
    
    