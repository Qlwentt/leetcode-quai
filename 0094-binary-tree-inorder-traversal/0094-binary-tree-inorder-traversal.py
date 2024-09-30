# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        def inorder(node):
            if not node:
                return 
            
            inorder(node.left)
            answer.append(node.val)
            inorder(node.right)
        inorder(root)
        return answer
# Time: O(N)
# Space: O(H) where h is the height of the tree. O(N) for a skewed tree, O(log(N)) for a balanced tree
        
        