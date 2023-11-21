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
        parents = defaultdict(set)
        
        def getParents(node, start, target):
            if not node:
                return node
            
            if target and node.val in parents[target]:
                return node
            
            parents[start].add(node.val)
            return getParents(node.parent, start, target)
            
            
        
        getParents(p,p, None)
        return getParents(q,q,p)
        
        
        
        
       
        
        
            
            
            