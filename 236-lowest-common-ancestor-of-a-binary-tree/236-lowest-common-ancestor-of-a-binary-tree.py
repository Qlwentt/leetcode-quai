# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [root]
        parents = {root:None}
        
        while p not in parents or q not in parents:
            node = stack.pop()
            
            if node.left:
                stack.append(node.left)
                parents[node.left] = node
            
            if node.right:
                stack.append(node.right)
                parents[node.right] = node
        
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parents[p]
        
        while q:
            if q in ancestors:
                break
            q = parents[q]
        return q