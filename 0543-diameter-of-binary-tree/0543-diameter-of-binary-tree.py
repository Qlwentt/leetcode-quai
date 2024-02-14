# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        longestPath = float('-inf')
        
        def dfs(root):
            nonlocal longestPath
            if not root:
                return [-1,-1]
            
            leftL, leftR = dfs(root.left)
            rightL, rightR = dfs(root.right)
            
            
            left = max(leftL, leftR) + 1
            right = max(rightL, rightR) + 1
            
            longestPath = max(longestPath, left+right)
            
            return [left, right]
        
        dfs(root)
        return longestPath
            
            
            