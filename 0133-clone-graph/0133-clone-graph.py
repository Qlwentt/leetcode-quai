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
        q = deque([node])
        visited = set([node])
        while q:
            curNode = q.popleft()
            copyNode = originalToCopy[curNode] if curNode in originalToCopy else Node(curNode.val)
            originalToCopy[curNode] = copyNode
            
            for neigh in curNode.neighbors:
                copyNeigh = originalToCopy[neigh] if neigh in originalToCopy else Node(neigh.val)
                originalToCopy[neigh] = copyNeigh
                copyNode.neighbors.append(copyNeigh)
                if neigh not in visited:
                    q.append(neigh)
                    visited.add(neigh)
                    
        return originalToCopy[node]
                
        
        