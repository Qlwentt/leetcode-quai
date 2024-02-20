import random
class Solution:

    def __init__(self, w: List[int]):
        self.totalSum = 0
        self.choices = [0]*len(w)
        for i, weight in enumerate(w):
            self.totalSum += weight
            self.choices[i] = self.totalSum
        

    def pickIndex(self) -> int:
        target = randint(1, self.totalSum)
        lo = 0
        hi = len(self.choices) - 1
        
        while lo <= hi:
            mid = (lo + hi) // 2
            
            if self.choices[mid] >= target:
                hi = mid - 1
            else:
                lo = mid + 1
                
        return lo


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()