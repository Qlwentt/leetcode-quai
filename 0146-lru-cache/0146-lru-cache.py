class Node:
    def __init__(self, key, val):
        self.next = None
        self.prev = None
        self.key = key
        self.val = val
class LRUCache:

    def __init__(self, capacity: int):
        self.header = Node(None, 0) # most recent ----- least recent
        self.footer = Node(None, 0)
        self.capacity = capacity
        self.store = {} #key: key, val: Node
        self.header.next = self.footer
        self.footer.prev = self.header
        
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _insertFront(self, node):
        node.next = self.header.next
        node.prev = self.header
        self.header.next.prev = node
        self.header.next = node
    
    def get(self, key: int) -> int:
        res = -1
        if key in self.store:
            node = self.store[key]
            res = node.val
            # move to front
            self._remove(node)
            self._insertFront(node)
        return res
            

    def put(self, key: int, value: int) -> None:
        # if already in store, update val
        if key in self.store:
            node = self.store[key]
            node.val = value
            # take from current pos
            self._remove(node)
        else:
            node = Node(key, value)
            self.store[key] = node
        # move to front
        self._insertFront(node)
        
        # evict least recently used
        if len(self.store) > self.capacity:
            lru = self.footer.prev
            del self.store[lru.key]
            self._remove(lru)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)