# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        #RVL
        #inorder traversal
        prev = 0
        def dfs(root):
            nonlocal prev
            if not root:
                return 0
            
            dfs(root.right)
            root.val = root.val + prev
            prev = root.val
            dfs(root.left)
            return root.val
        dfs(root)
        return root
        
        