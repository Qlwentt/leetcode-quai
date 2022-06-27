class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.store = {} #key: Node
        self.capacity = capacity
        self.header = Node(0,0) # most recently used
        self.footer = Node(0,0) # least recently used
        
        self.header.next = self.footer
        self.footer.prev = self.header
        
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insertFront(self, node):
        node.prev = self.header
        node.next = self.header.next
        self.header.next.prev = node
        self.header.next = node
            
    
    def get(self, key: int) -> int:
        res = -1
        if key in self.store:
            node = self.store[key]
            res = node.value
            # move to most recently used
            self._remove(node)
            self._insertFront(node)
        return res

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            node = self.store[key]
            node.value = value
            self._remove(node)
        else:
            node = Node(key,value)
            self.store[key] = node
        # move to most recently used
        self._insertFront(node)
        if  len(self.store) > self.capacity:
            del self.store[self.footer.prev.key]
            self._remove(self.footer.prev)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# O(1) time - put, get
# O(n) space