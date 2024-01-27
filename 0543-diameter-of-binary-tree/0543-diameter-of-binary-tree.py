# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0
        
        def dfs(root):
            nonlocal maxDiameter
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            left = 1 + left if root.left else left
            right = 1 + right if root.right else right
            
            diameter = left + right
            maxDiameter = max(diameter, maxDiameter)
            
            return max(left, right)
        dfs(root)
        return maxDiameter