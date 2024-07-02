# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def dfs(root,nodes, length):
            if root.val in nodes:
                nodes.remove(root.val)
            else:
                nodes.add(root.val)
            if not root.left and not root.right:
                if length % 2 == 0:
                    return 1 if len(nodes) == 0 else 0
                else:
                    return 1 if len(nodes) == 1 else 0
            left = 0
            right = 0
            if root.left:
                left = dfs(root.left, nodes.copy(), length+1)
            if root.right:
                right = dfs(root.right, nodes.copy(), length+1)
            
            return left + right
        return dfs(root, set(), 1)