class StockSpanner:

    def __init__(self):
        self.stack = [(float('inf'), 0)]
        self.day = 1

    def next(self, price: int) -> int:
        while self.stack and price >= self.stack[-1][0]:
            self.stack.pop()
        span = self.day - self.stack[-1][1]
        self.stack.append((price, self.day))
        self.day += 1
        return span
        
# Time: O(N) where N is the length of the stream
# Space: O(N)


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)