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
        pDistance = 0
        
        curr = p
        while curr:
            curr = curr.parent
            pDistance += 1
        
        curr = q
        qDistance = 0
        while curr:
            curr = curr.parent
            qDistance += 1
            
        while pDistance > qDistance:
            p = p.parent
            pDistance -= 1
        
        while qDistance > pDistance:
            q = q.parent
            qDistance -= 1
            
        while p != q:
            p = p.parent
            q = q.parent
        
        return p