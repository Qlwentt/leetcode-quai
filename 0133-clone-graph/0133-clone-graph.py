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
            return None
        
        original_to_copy = {}
        visited = set()
        def dfs(node):
            if not node:
                return None
            if node in visited:
                return original_to_copy[node]
            
            visited.add(node)
            
            copy = Node(node.val)
            original_to_copy[node] = copy
            for neigh in node.neighbors:
                copy.neighbors.append(dfs(neigh))
            
            return copy
        dfs(node)
        return original_to_copy[node]
                
            
        
#         if not node:
#             return node
        
#         originalToCopy = {}
#         visited = set([node])
#         q = deque([node])
        
#         while q:
#             cur = q.popleft()
#             curCopy = originalToCopy[cur] if cur in originalToCopy else Node(cur.val)
#             originalToCopy[cur] = curCopy
            
#             for neigh in cur.neighbors:
#                 neighCopy = originalToCopy[neigh] if neigh in originalToCopy else Node(neigh.val)
#                 originalToCopy[neigh] = neighCopy
#                 curCopy.neighbors.append(neighCopy)
#                 if neigh not in visited:
#                     q.append(neigh)
#                     visited.add(neigh)
                
            
        
        # return originalToCopy[node]
        
        
        