# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return
            if not node.left and not node.right and node.val == target:
                return None
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            node.left = left
            node.right = right
            
            if not left and not right and node.val == target:
                return None
            return node
        return dfs(root)
        