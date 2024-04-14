# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        answer = 0
        def dfs(root):
            nonlocal answer
            if not root:
                return
            if root.val in range(low, high+1):
                answer += root.val
                dfs(root.left)
                dfs(root.right)
            else:
                if root.val < low:
                    dfs(root.right)
                elif root.val > high:
                    dfs(root.left)
        dfs(root)
        return answer
        