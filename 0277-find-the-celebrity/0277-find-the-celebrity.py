# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        candidate = 0
        for i in range(1,n):
            if knows(candidate, i):
                candidate = i
                
        return candidate if self.isCeleb(candidate,n) else -1
        
    def isCeleb(self, candidate, n):
        for i in range(n):
            if i == candidate:
                continue
            if knows(candidate,i) or not knows(i, candidate):
                return False
            
        return True