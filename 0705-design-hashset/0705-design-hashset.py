class Node:
    def __init__(self, value = None, next_ = None):
        self.value = value
        self.next = next_
        

class MyHashSet:

    def __init__(self):
        self.capacity = 10 ** 4
        self.size = 0
        self.storage = [None] * self.capacity
        

    def add(self, key: int) -> None:
        if self.contains(key):
            return
        targetI = self._hash(key)
        if self.storage[targetI] == None:
            self.storage[targetI] = Node(None, Node(key))
        else:
            dummy = self.storage[targetI]
            newNode = Node(key, dummy.next)
            dummy.next = newNode
        self.size += 1
            

    def remove(self, key: int) -> None:
        targetI = self._hash(key)
        if self.storage[targetI] == None:
            return
        dummy = self.storage[targetI]
        cur = dummy
        while cur and cur.next:
            if cur.next.value == key:
                cur.next = cur.next.next
                self.size -= 1
            cur = cur.next
        

    def contains(self, key: int) -> bool:
        targetI = self._hash(key)
        if self.storage[targetI] == None:
            return False
        dummy = self.storage[targetI]
        cur = dummy.next
        while cur:
            if cur.value == key:
                return True
            cur = cur.next
        return False
        
    def _hash(self, key):
        return key % self.capacity
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)