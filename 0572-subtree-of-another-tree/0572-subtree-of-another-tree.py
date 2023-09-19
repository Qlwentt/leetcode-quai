# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            
            if p.val != q.val:
                return False
            
            left = isSameTree(p.left, q.left)
            right = isSameTree(p.right, q.right)
            
            return left and right
        
        if not root:
            return False
        
        if root.val == subRoot.val:
            if isSameTree(root, subRoot):
                return True
        
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
        
        return left or right
        
        