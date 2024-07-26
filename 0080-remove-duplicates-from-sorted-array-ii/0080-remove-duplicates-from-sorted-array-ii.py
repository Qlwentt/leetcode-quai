class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        current = None
        count = 0
        l = 0
        for r in range(len(nums)):
            if current != nums[r] or current == nums[r] and count < 2:
                nums[l] = nums[r]
                l += 1
            if current != nums[r]:
                current = nums[r]
                count = 1
            else:
                count += 1
    
        return l
    
# Time: O(N)
# Space: O(1)
            