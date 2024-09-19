class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt

class MyCircularQueue:

    def __init__(self, k: int):
        self.front = Node(0)
        self.end = self.front
        self.max_size = k
        self.size = 0
        
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.end.next = Node(value)
        self.end = self.end.next
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front.next = self.front.next.next
        self.size -= 1
        if self.isEmpty():
            self.end = self.front
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.front.next.val
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.end.val
        

    def isEmpty(self) -> bool:
        return self.front.next == None
        

    def isFull(self) -> bool:
        return self.size == self.max_size
        
# Time: O(1) for all operations
# Space: O(1) for all operations, O(N) for total space taken up by the queue considering N calls to enqueue


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()