class RandomizedSet:

    def __init__(self):
        self.store = {}
        self.randomList = []
        
        

    def insert(self, val: int) -> bool:
        if val not in self.store:
            self.store[val] = len(self.randomList)
            self.randomList.append(val)
            return True
        return False
            

    def remove(self, val: int) -> bool:
        if val in self.store:
            i = self.store[val]
            end = len(self.randomList) -1
            self.store[self.randomList[end]] = i
            del self.store[val]
            self.randomList[i] = self.randomList[end]
            self.randomList.pop()
            return True
        return False

    def getRandom(self) -> int:
        randI = randrange(0, len(self.randomList))
        return self.randomList[randI]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()