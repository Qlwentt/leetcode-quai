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
        distP = 0
        distQ = 0
        
        cur = p
        while cur:
            distP += 1
            cur = cur.parent
        
        cur = q
        while cur:
            distQ += 1
            cur = cur.parent
        
        while distP > distQ:
            p = p.parent
            distP -= 1
        
        while distQ > distP:
            distQ -= 1
            q = q.parent
            
        
        while p != q:
            p = p.parent
            q = q.parent
            
        return p