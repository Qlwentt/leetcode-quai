class NumArray:

    def __init__(self, nums: List[int]):
        # [-2, 0, 3, -5, 2, -1]
        # [-2, -2, 1,-4,-2,-3]
        #   0   1  2  3  4  5
        self.prefixSums = [0]*len(nums)
        runSum = 0
        for i in range(len(nums)):
            runSum += nums[i]
            self.prefixSums[i] = runSum        

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixSums[right] - self.prefixSums[left -1] if left > 0 else self.prefixSums[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)