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
            
            maxLeft = dfs(root.left)
            maxRight = dfs(root.right)
            
            maxLeft = max(maxLeft, 0)
            maxRight = max(maxRight, 0)
            
            res = max(res, maxLeft+maxRight+root.val)
            
            #return max without a split
            return max(maxLeft, maxRight) + root.val
        
        dfs(root)
        return res
            
            
            
        