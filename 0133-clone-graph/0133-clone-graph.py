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
        
        originalToCopy = {}
        visited = set([node])
        q = deque([node])
        
        while q:
            cur = q.popleft()
            curCopy = originalToCopy[cur] if cur in originalToCopy else Node(cur.val)
            originalToCopy[cur] = curCopy
            
            for neigh in cur.neighbors:
                neighCopy = originalToCopy[neigh] if neigh in originalToCopy else Node(neigh.val)
                originalToCopy[neigh] = neighCopy
                curCopy.neighbors.append(neighCopy)
                if neigh not in visited:
                    q.append(neigh)
                    visited.add(neigh)
                
            
        
        return originalToCopy[node]
        
        
        