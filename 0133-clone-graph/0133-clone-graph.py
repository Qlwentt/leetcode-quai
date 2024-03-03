"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        q = deque([node])
        originalToCopy = {}
        visited = set([node])
        while q:
            original = q.popleft()
            copy = originalToCopy[original] if original in originalToCopy else Node(original.val)
            originalToCopy[original] = copy
            
            for neigh in original.neighbors:
                copyNeigh = originalToCopy[neigh] if neigh in originalToCopy else Node(neigh.val)
                originalToCopy[neigh] = copyNeigh
                if neigh not in visited:
                    q.append(neigh)
                    visited.add(neigh)
                copy.neighbors.append(copyNeigh)
                
        return originalToCopy[node]
                
            
        
        