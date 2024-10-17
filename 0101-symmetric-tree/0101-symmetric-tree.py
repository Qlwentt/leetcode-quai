# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return True
        
        def are_mirrors(root1,root2):
            if not root1 and not root2:
                return True
            if not root1 and root2:
                return False
            if not root2 and root1:
                return False
            
            if root1.val != root2.val:
                return False
            
            left = are_mirrors(root1.left, root2.right)
            right = are_mirrors(root1.right, root2.left)
            
            return left and right
        
        return are_mirrors(root.left, root.right)
        
        
        