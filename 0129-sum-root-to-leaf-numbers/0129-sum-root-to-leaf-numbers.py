# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        answer = 0
        def preorder(root, path):
            nonlocal answer
            if not root:
                return
            
            path = path * 10 + root.val
            if not root.left and not root.right:
                answer += path
            preorder(root.left, path)
            preorder(root.right, path)
        preorder(root, 0)
        return answer
            