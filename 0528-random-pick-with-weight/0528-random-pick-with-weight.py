from random import randint
from bisect import bisect_left
class Solution:

    def __init__(self, w: List[int]):
        self.choices = [0]* len(w)
        self.sum = 0
        
        for i, weight in enumerate(w):
            self.sum += weight
            self.choices[i] = self.sum
        

    def pickIndex(self) -> int:
        target = randint(1,self.sum)
        return bisect_left(self.choices, target)

# Time __init__: O(N), pickIndex: O(log(N))
# Space __init__: O(N), pickIndex: O(1)

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()