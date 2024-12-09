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
    # DFS solution
        if not node:
            return None
        
        original_to_copy = {}
        def dfs(node):
            if not node:
                return None
            if node in original_to_copy:
                return original_to_copy[node]
            
            copy = Node(node.val)
            original_to_copy[node] = copy
            for neigh in node.neighbors:
                copy.neighbors.append(dfs(neigh))
            
            return copy
        return dfs(node)
                
            
# BFS solution 
        if not node:
            return None
        
        original_to_copy = {}
        visited = set([node])
        
        q = deque([node])
        
        while q:
            cur = q.popleft()
            cur_copy = original_to_copy[cur] if cur in original_to_copy else Node(cur.val)
            original_to_copy[cur] = cur_copy
            
            for neigh in cur.neighbors:
                neigh_copy = original_to_copy[neigh] if neigh in original_to_copy else Node(neigh.val)
                original_to_copy[neigh] = neigh_copy
                cur_copy.neighbors.append(neigh_copy)
                if neigh not in visited:
                    q.append(neigh)
                    visited.add(neigh)
        
        return original_to_copy[node]
        
# Time: O(V+E)
# Space: O(V)
        