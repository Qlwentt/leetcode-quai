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
        root = TreeNode(preorder[0])
        mid = inorder.index(root.val)
        
        leftLen = len(inorder[:mid])
    
        root.left = self.buildTree(preorder[1:leftLen+1], inorder[:mid])
        root.right = self.buildTree(preorder[leftLen+1:], inorder[leftLen+1:])
        return root
        
