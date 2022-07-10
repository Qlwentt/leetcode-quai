# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None

        root = TreeNode(postorder[-1])
        mid = inorder.index(root.val)
        
        leftLen = len(inorder[:mid])

        root.left = self.buildTree(inorder[:mid],postorder[:leftLen])
        root.right = self.buildTree(inorder[mid+1:],postorder[leftLen:-1])
        return root