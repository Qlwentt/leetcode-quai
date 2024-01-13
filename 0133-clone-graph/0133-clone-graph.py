"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        origToCopy = {}
        q = deque([node])
        visited = set()
        visited.add(node)
        
        while q:
            n = q.popleft()
            copyN = origToCopy[n] if n in origToCopy else Node(n.val)
            origToCopy[n] = copyN
            
            for neigh in n.neighbors:
                copyNeigh = origToCopy[neigh] if neigh in origToCopy else Node(neigh.val)
                origToCopy[neigh] = copyNeigh
                copyN.neighbors.append(copyNeigh)
                if neigh not in visited:
                    q.append(neigh)
                
                visited.add(neigh)
        
        return origToCopy[node]
            
        
        
        
        