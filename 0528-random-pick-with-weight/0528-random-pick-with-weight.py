from random import randint
from bisect import bisect_left
class Solution:

    def __init__(self, w: List[int]):    
        self.choices = [0]*len(w)
        self.sumWeights = sum(w)
        runSum = 0
        for i, weight in enumerate(w):
            runSum += weight
            self.choices[i] = runSum
        
            

    def pickIndex(self) -> int:
        
        key = randint(1, self.sumWeights)
        return bisect_left(self.choices, key)
    


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()