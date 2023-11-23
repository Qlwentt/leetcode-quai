from collections import defaultdict
from random import choice
class Solution:

    def __init__(self, nums: List[int]):
        self.numMap = defaultdict(list)
        for i, num in enumerate(nums):
            self.numMap[num].append(i)

    def pick(self, target: int) -> int:
        return choice(self.numMap[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)