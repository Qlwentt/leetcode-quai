# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         answer = []
#         def postorder(node):
#             if not node:
#                 return
            
#             postorder(node.left)
#             postorder(node.right)
#             answer.append(node.val)
#         postorder(root)
#         return answer
# # Time: O(N)
# # Space: O(H) where H is height of the tree

# iterative solution

        stack = [(root,False)]
        answer = []
        
        while stack:
            node, to_visit = stack.pop()
            
            if not node:
                continue
            
            if to_visit:
                answer.append(node.val)
            else:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
        return answer
        