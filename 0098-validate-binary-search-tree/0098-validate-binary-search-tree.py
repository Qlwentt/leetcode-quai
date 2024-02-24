# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = float('-inf')
        def inorder(root):
            nonlocal prev
            if not root:
                return True
            
        
            left = inorder(root.left)
            
            if prev >= root.val:
                return False
            prev = root.val
            right = inorder(root.right)
            
            return left and right
        return inorder(root)