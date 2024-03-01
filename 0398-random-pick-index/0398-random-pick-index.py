from collections import defaultdict
class Solution:

    def __init__(self, nums: List[int]):
        self.choices = defaultdict(list)
        for i, num in enumerate(nums):
            self.choices[num].append(i)
        

    def pick(self, target: int) -> int:
        return random.choice(self.choices[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)