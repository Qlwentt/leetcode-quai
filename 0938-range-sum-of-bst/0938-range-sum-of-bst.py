# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sum_ = 0
        
        def dfs(root):
            nonlocal sum_
            if not root:
                return
            
            if root.val in range(low, high+1):
                sum_ += root.val
                
            if low < root.val:
                dfs(root.left)
                
            if high >= root.val:
                dfs(root.right)
        dfs(root)
        return sum_