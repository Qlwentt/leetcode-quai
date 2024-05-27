class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = [[0,0] for _ in range(maxSize)]
        self.currentSize = 0

    def push(self, x: int) -> None:
        if self.currentSize < self.maxSize:
            self.currentSize += 1
            self.stack[self.currentSize - 1] = [x,0]

    def pop(self) -> int:
        if self.currentSize == 0:
            return -1
        
        val, inc = self.stack[self.currentSize-1]
        self.currentSize -= 1
        if self.currentSize > 0:
            self.stack[self.currentSize-1][1] += inc
        
        return val + inc
        
        

    def increment(self, k: int, val: int) -> None:
        lastItemToIncrement = min(self.currentSize -1, k-1)
        self.stack[lastItemToIncrement][1] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)