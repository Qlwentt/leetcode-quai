class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = float("inf")
                count += 1
        
        nums.sort()
        return len(nums) - count
                                
        