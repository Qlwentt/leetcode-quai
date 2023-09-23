# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def getPathSums(root):
            if not root:
                return (0, float('-inf'))
            left, mpLeft = getPathSums(root.left)
            right, mpRight = getPathSums(root.right)
            
            pathSum = left + right + root.val
            
            maxPath = max(pathSum, mpLeft, mpRight)
            
            return (max(left+root.val, right + root.val, root.val, 0), maxPath)
        return getPathSums(root)[1]