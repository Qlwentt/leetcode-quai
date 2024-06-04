class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums)-2):
            c = nums[i]
            a = nums[i+1]
            b = nums[i+2]
            if a + b > c:
                return a + b + c
        
        return 0
                    