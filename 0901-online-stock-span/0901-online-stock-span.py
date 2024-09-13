class StockSpanner:

    def __init__(self):
        self.stack = [] #price, span
    
    def next(self, price: int) -> int:
        answer = 1
        while self.stack and self.stack[-1][0] <= price:
            lesser_price, span = self.stack.pop()
            answer += span
        self.stack.append((price,answer))
        return answer
        
# Time: O(N) where N is the length of the stream
# Space: O(N)


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)