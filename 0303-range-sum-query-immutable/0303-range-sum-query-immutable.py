class NumArray:

    def __init__(self, nums: List[int]):
        # [-2, 0, 3, -5, 2, -1]
        # [-2, -2, 1,-4,-2,-3]
        #   0   1  2  3  4  5
        self.prefix_sums = []
        cur_sum = 0
        for num in nums:
            cur_sum += num
            self.prefix_sums.append(cur_sum)       

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sums[right] - self.prefix_sums[left -1] if left > 0 else self.prefix_sums[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

# Time: init - O(N); sumRange - O(1)
# Space: init - O(N); sumRange - O(1)