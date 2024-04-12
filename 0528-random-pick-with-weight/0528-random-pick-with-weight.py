import random
class Solution:

    def __init__(self, w: List[int]):
        self.picks = []
        curSum = 0
        for weight in w:
            curSum += weight
            self.picks.append(curSum)
        

    def pickIndex(self) -> int:
        target = randint(1, self.picks[-1])
        L = 0
        R = len(self.picks) - 1
        
        while L <= R:
            mid = (L + R) // 2
            if self.picks[mid] >= target: # too hi
                R = mid - 1
            else:
                L = mid + 1
        return L
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()