class FirstUnique:

    def __init__(self, nums: List[int]):
        self.counts = collections.Counter(nums)

    def showFirstUnique(self) -> int:
        for num, count in self.counts.items():
            if count == 1:
                return num
        return -1
        

    def add(self, value: int) -> None:
        self.counts[value] +=1 
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)