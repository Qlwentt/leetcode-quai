# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(node, answer):
            if not node:
                return answer
            inorder(node.left, answer)
            answer.append(node.val)
            inorder(node.right, answer)
            return answer
        return inorder(root, [])
        
        
        