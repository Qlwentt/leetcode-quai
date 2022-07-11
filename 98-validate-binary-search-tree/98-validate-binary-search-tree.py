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
            if not inorder(root.left):
                return False
            if not prev < root.val:
                return False
            prev = root.val
            if not inorder(root.right):
                return False
            return True
        return inorder(root)
        