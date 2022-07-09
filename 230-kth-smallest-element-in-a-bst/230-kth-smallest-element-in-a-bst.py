# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        treeArray = []
        
        def inorder(root):
            if not root:
                return treeArray
            if root.left:
                inorder(root.left)
            treeArray.append(root.val)
            if root.right:
                inorder(root.right)
            return treeArray
        treeArray = inorder(root)
        return treeArray[k-1]