class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixSums = [0] * len(nums)
        summ = 0
        for i, num in enumerate(nums):
            summ += num
            self.prefixSums[i] = summ
       # [-2, 0,  3, -5,  2, -1]  2, 4 => 0
       #   0  1   2   3   4   5   pS[R] - ps[L-1]
       # [-2, -2, 1, -4, -2, -3]

    def sumRange(self, left: int, right: int) -> int:
        prefixSumR = self.prefixSums[right]
        prefixSumL = self.prefixSums[left -1] if left > 0 else 0
        return prefixSumR - prefixSumL


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)