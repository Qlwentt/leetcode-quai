class Node:
    def __init__(self, key = None, value=None, next_=None):
        self.key = key
        self.value = value
        self.next = next_

class MyHashMap:

    def __init__(self):
        self.capacity = 10 ** 4
        self.storage = [None] * self.capacity
        self.size = 0
        
    

    def put(self, key: int, value: int) -> None:
        i = self._hash(key)
        if self.storage[i] == None:
            self.storage[i] = Node(None,None, Node(key,value))
            return
        dummy = self.storage[i]
        cur = dummy
        
        while cur and cur.next:
            if cur.next.key == key:
                cur.next.value = value
                return 
            cur = cur.next
        cur.next = Node(key,value)
        self.size += 1        
        

    def get(self, key: int) -> int:
        i = self._hash(key)
        if self.storage[i] == None:
            return -1
        dummy = self.storage[i]
        cur = dummy.next
        while cur:
            if cur.key == key:
                return cur.value
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        i = self._hash(key)
        if self.storage[i] == None:
            return
        dummy = self.storage[i]
        cur = dummy
        while cur and cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                self.size -= 1
                return
            cur = cur.next
        
        
    def _hash(self, key: int) -> int:
        return key % self.capacity
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)