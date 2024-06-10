# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(root):
            if not root:
                return False
            
            left_has_one = dfs(root.left)
            right_has_one = dfs(root.right)
            
            if not left_has_one:
                root.left = None
            
            if not right_has_one:
                root.right = None
            
            return left_has_one or right_has_one or root.val
        
        root_has_one = dfs(root)
        return root if root_has_one else None
        