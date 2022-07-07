# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def helper(root):
            if not root:
                return (True, 0)
            if not root.left and not root.right:
                return (True, 1)
            isBalL, heightL = helper(root.left)
            isBalR, heightR = helper(root.right)
            
            return (isBalL and isBalR and abs(heightL - heightR)<=1, max(heightL,heightR) + 1)
            
        return helper(root)[0]