# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxPath = float('-inf')
        
        def getPathSums(root):
            if not root:
                return 0
            nonlocal maxPath
            left = getPathSums(root.left)
            right = getPathSums(root.right)
            
            pathSum = left + right + root.val
            
            maxPath = max(pathSum, maxPath)
            
            return max(left+root.val, right + root.val, root.val, 0)
        getPathSums(root)
        return maxPath