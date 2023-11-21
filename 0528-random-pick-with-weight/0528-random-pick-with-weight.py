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
        
        target = randint(1, self.sumWeights)
        
        lo = 0
        hi = len(self.choices) - 1
        
        while lo <= hi:
            mid = (lo+hi) // 2
            
            if target > self.choices[mid]:
                lo = mid + 1
            else:
                hi = mid -1
        return lo
    


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()