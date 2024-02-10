from random import randint
class Solution:

    def __init__(self, w: List[int]):
        self.total = 0
        self.choices = [0]* len(w)

        for i, weight in enumerate(w):
            self.total+= weight
            self.choices[i] = self.total
            
        

    def pickIndex(self) -> int:
        target = randint(1,self.total)
        
        lo = 0
        hi = len(self.choices) - 1
        
        while lo <= hi:
            mid = (lo+hi) // 2
            
            if self.choices[mid] >= target:
                hi = mid - 1
            else:
                lo = mid + 1
                
        return lo


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()