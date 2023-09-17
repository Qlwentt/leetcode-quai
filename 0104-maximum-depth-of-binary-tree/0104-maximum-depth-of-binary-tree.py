# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def getDepth(node):
            if not node:
                return 0
            leftDepth = getDepth(node.left) + 1
            rightDepth = getDepth(node.right) + 1 
            return max(leftDepth, rightDepth)
            
        return getDepth(root)
            