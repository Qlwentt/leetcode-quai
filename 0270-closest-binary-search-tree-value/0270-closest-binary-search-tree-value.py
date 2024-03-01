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
            
            answer = min(root.val, answer, key=lambda x: (abs(target-x), x))
            
            if root.val > target:
                dfs(root.left)
            elif root.val < target:
                dfs(root.right)
                
        dfs(root)
        return answer