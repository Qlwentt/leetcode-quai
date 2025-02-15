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
            root_valid = root.val > prev
            prev = root.val
            right = inorder(root.right)
            
            return left and right and root_valid
        
        return inorder(root)
# Time: O(N)
# Space: O(H)
        