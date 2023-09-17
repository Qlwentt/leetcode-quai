# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def getDepth(node, depth):
            if not node:
                return depth
            leftDepth = getDepth(node.left, depth + 1)
            rightDepth = getDepth(node.right, depth + 1) 
            return max(leftDepth, rightDepth)
            
        return getDepth(root, 0)
            