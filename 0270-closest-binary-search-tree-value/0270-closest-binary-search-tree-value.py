# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        answer = root.val
        
        def dfs(root):
            nonlocal answer
            if not root:
                return
            answer = min(answer, root.val, key=lambda x: (abs(x-target), x))
            
            if root.val < target:
                dfs(root.right)
            elif root.val > target:
                dfs(root.left)
                
        dfs(root)
        return answer