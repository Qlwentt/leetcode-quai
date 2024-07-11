class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        counts = 0
        sum_ = 0
        for num in nums:
            sum_ += num
            if sum_ == 0:
                counts += 1
        
        return counts