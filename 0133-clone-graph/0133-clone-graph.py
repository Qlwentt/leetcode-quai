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
        visited = set([node])
        q = deque([node])
        origToCopy = {}
        while q:
            curNode = q.popleft()
            if curNode in origToCopy:
                copy = origToCopy[curNode]
            else:
                copy = Node(curNode.val)
                origToCopy[curNode] = copy
            
            for neigh in curNode.neighbors:
                copyNeigh = origToCopy[neigh] if neigh in origToCopy else Node(neigh.val)
                origToCopy[neigh] = copyNeigh
                copy.neighbors.append(copyNeigh)
                if neigh not in visited:
                    q.append(neigh)
                    visited.add(neigh)
            
        return origToCopy[node]