# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        array = []
        def dfs(root):
            if not root:
                return
            
            array.append(str(root.val))
            if root.left:
                array.append("(")
                dfs(root.left)
                array.append(")")
            else:
                if root.right:
                    array.append("()")
            
            if root.right:
                array.append(("("))
                dfs(root.right)
                array.append(")")
        dfs(root)
        return "".join(array)