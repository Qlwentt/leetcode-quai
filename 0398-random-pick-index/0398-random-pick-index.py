from collections import defaultdict
import random
class Solution:

    def __init__(self, nums: List[int]):
        self.numDict = defaultdict(list)
        for i, num in enumerate(nums):
            self.numDict[num].append(i)
        

    def pick(self, target: int) -> int:
        return choice(self.numDict[target])
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)