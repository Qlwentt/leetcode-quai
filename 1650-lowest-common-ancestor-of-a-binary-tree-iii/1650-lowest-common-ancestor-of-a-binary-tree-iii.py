"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""
from collections import defaultdict
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        
        def distance(node):
            if not node:
                return 0
            
            return 1 + distance(node.parent)
            
        pDistance = distance(p)
        qDistance = distance(q)
        
        # further away needs to swim up until it's equal
        # only one of these will run or non if they are already equal
        while pDistance > qDistance:
            p = p.parent
            pDistance -= 1
        
        while qDistance > pDistance:
            q = q.parent
            qDistance -= 1
        
        # swim up until both meet
        while p != q:
            p = p.parent
            q = q.parent
        
        return p
            
# time: O(N)
# space: O(1)
            
            
        
        
        
        
       
        
        
            
            
            