class SmallestInfiniteSet:

    def __init__(self):
        self.banned = set()
        self.smallest = 1

    def popSmallest(self) -> int:
        self.banned.add(self.smallest)
        
        answer = self.smallest
        
        while self.smallest in self.banned:
            self.smallest += 1
            
        return answer
        
        

    def addBack(self, num: int) -> None:
        if num in self.banned:
            self.banned.remove(num)
            self.smallest = min(num, self.smallest)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)