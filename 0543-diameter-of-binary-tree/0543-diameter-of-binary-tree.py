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
            
            leftL += 1
            leftR += 1
            
            rightL += 1
            rightR += 1
            
            left = max(leftL, leftR)
            right = max(rightL, rightR)
            
            longestPath = max(longestPath, left+right)
            
            return [left, right]
        
        dfs(root)
        return longestPath
            
            
            
            