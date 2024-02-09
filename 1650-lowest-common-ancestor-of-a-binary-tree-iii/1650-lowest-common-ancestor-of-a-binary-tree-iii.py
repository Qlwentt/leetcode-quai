"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        pDistToRoot = 0
        qDistToRoot = 0
        
        node = p
        while node:
            node = node.parent
            pDistToRoot += 1
        
        node = q
        while node:
            node = node.parent
            qDistToRoot += 1
            
        while pDistToRoot > qDistToRoot:
            p = p.parent
            pDistToRoot -= 1
            
        while qDistToRoot > pDistToRoot:
            q = q.parent
            qDistToRoot -= 1
            
        while p != q:
            p = p.parent
            q = q.parent
        
        return p