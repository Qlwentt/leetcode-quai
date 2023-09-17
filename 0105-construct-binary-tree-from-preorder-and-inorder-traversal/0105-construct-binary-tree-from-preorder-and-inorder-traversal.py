# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        rootVal = preorder[0]
        iRoot = inorder.index(rootVal)
        left = self.buildTree(preorder[1:iRoot+1], inorder[:iRoot])
        right = self.buildTree(preorder[iRoot+1:], inorder[iRoot+1:])
        root = TreeNode(rootVal, left, right)
        return root