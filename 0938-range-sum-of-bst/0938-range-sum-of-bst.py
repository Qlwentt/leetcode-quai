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
                dfs(root.left)
                dfs(root.right)
            else:
                if root.val < low:
                    return dfs(root.right)
                elif root.val > high:
                    return dfs(root.left)
        dfs(root)
        return sum_
        