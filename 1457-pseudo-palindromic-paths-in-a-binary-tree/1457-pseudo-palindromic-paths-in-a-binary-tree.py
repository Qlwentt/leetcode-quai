# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def dfs(root,nodes):
            if root.val in nodes:
                nodes.remove(root.val)
            else:
                nodes.add(root.val)
            if not root.left and not root.right:
                return 1 if len(nodes) <= 1 else 0
            left = 0
            right = 0
            if root.left:
                left = dfs(root.left, nodes.copy())
            if root.right:
                right = dfs(root.right, nodes.copy())
            
            return left + right
        return dfs(root, set())