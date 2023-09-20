# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         parents = defaultdict(dict)
#         def getParents(root, parent):
#             if not root:
#                 return 
#             nonlocal parents
                        
#             parents[root.val][root] = None
            
#             currParent = parents[root.val]
#             if parent:
#                 currParent.update(parents[parent.val])
            
#             getParents(root.left, root)
#             getParents(root.right, root)
        
#         getParents(root, None)
        
#         pParents = parents[p.val]
#         qParents = parents[q.val]
        
#         for parent in pParents.keys():
#             if parent in qParents:
#                 return parent
#         return None
        while root:
            if p.val > root.val and q.val > root.val:
                root = root.right
            elif p.val < root.val and q.val < root.val:
                root = root.left
            else:
                return root
                
            
        
        
        
        