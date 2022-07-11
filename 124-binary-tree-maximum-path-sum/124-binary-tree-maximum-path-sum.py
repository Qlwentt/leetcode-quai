# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val
        
        def dfs(root):
            nonlocal res
            
            if not root:
                return 0
            
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)
            
            # calc with split
            
            res = max(res, leftMax + rightMax + root.val)
            
            return max(leftMax,rightMax) + root.val
        dfs(root)
        return res
            
            
        