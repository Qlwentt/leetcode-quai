class OrderedStream:

    def __init__(self, n: int):
        self.store = [None]* (n+1)
        self.i = 1
    def insert(self, idKey: int, value: str) -> List[str]:
        self.store[idKey] = value
        answer = []
        for x in range(self.i, len(self.store)):
            if self.store[x] != None:
                answer.append(self.store[x])
                new_i = x
            else:
                break
        if answer:
            self.i = x
        return answer


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)