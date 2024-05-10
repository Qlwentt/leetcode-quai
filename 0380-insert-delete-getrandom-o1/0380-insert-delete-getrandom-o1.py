class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.list = []
        self.i = 0
        

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        i, lastEle = self.dict[val], self.list[-1]
        self.dict[lastEle], self.list[i] = i, lastEle
        del self.dict[val]
        self.list.pop()
    
    
        return True
        
        

    def getRandom(self) -> int:
        return random.choice(self.list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()