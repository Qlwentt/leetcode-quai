class Node:
    def __init__(self, val, nxt, prev):
        self.val = val
        self.next = nxt
        self.prev = prev

class MyCircularDeque:

    def __init__(self, k: int):
        self.size = 0
        self.max_size = k
        self.front = Node(0, None, None)
        self.end = Node(0, None, self.front)
        self.front.next = self.end

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        node = Node(value, self.front.next, self.front)
        self.front.next.prev = node
        self.front.next = node
        self.size += 1
        return True
        
        

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        node = Node(value,self.end,self.end.prev)
        self.end.prev.next = node
        self.end.prev = node
        self.size += 1
        return True
        

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front.next.next.prev = self.front
        self.front.next = self.front.next.next
        self.size -= 1
        return True
        

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.end.prev.prev.next = self.end
        self.end.prev = self.end.prev.prev
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.front.next.val
        

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.end.prev.val
        

    def isEmpty(self) -> bool:
        return self.front.next == self.end
        

    def isFull(self) -> bool:
        return self.size == self.max_size
        
# Time: O(1) for all operations
# Space: O(1) for all operations or O(N) for total space the deque takes up in general on N calls to insert methods

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()