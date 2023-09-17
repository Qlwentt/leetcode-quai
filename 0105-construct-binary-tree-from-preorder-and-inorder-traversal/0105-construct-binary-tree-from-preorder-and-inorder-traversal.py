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
        inorderLeft = inorder[:iRoot]
        inorderRight = inorder[iRoot+1:]

        preorderLeftLen = len(inorderLeft)
        preorderRightLen = len(inorderRight)

        left = self.buildTree(preorder[1:1+preorderLeftLen], inorderLeft)
        right = self.buildTree(preorder[1+preorderLeftLen:1+preorderLeftLen+preorderRightLen], inorderRight)
        root = TreeNode(rootVal, left, right)
        return root