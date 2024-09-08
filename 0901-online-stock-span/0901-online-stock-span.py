class StockSpanner:

    def __init__(self):
        self.stack = []   
       
    def next(self, price: int) -> int:
        answer = 1
        while self.stack and self.stack[-1][0] <= price:
            answer += self.stack.pop()[1]
        self.stack.append((price, answer))
        
        return answer


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)