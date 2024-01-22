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
        parents = set()
        
        def traverseUp(node):
            if not node:
                return node
            
            if node in parents:
                return node
            parents.add(node)
            return traverseUp(node.parent)
            
            
            
            
            
            
        
        traverseUp(p)
        return traverseUp(q)
        
        
        
        
       
        
        
            
            
            