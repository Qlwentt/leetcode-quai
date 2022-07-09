# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         treeArray = []
        
#         def inorder(root):
#             if not root:
#                 return treeArray
#             if root.left:
#                 inorder(root.left)
#             treeArray.append(root.val)
#             if root.right:
#                 inorder(root.right)
#             return treeArray
#         treeArray = inorder(root)
#         return treeArray[k-1]
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = [(root,False)]
        i = 1
        # LVR
        while stack:
            node, visit = stack.pop()
            if not node:
                continue
            if visit:
                if k == i:
                    return node.val
                i += 1
                continue
            stack.extend([(node.right,False),(node,True),(node.left,False)])