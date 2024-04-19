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
            copy = originalToCopy.get(curNode, Node(curNode.val))
            originalToCopy[curNode] = copy
            
            for neigh in curNode.neighbors:
                copyNeigh = originalToCopy.get(neigh, Node(neigh.val))
                originalToCopy[neigh] = copyNeigh
                copy.neighbors.append(copyNeigh)
                if neigh not in visited:
                    q.append(neigh)
                    visited.add(neigh)
        
        return originalToCopy[node]