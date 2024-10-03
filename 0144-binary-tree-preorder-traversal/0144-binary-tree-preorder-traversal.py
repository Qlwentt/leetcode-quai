# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # answer = []
        # def preorder(node):
        #     if not node:
        #         return
        #     answer.append(node.val)
        #     preorder(node.left)
        #     preorder(node.right)
        # preorder(root)
        # return answer
# Time: O(N)
# Space: O(H) where H is the height of the tree

        stack = [(root, False)]
        answer = []
        
        while stack:
            node, to_visit = stack.pop()
            if not node:
                continue
            
            if to_visit:
                answer.append(node.val)
            else:
                stack.append((node.right, False))
                stack.append((node.left,False))
                stack.append((node, True))
        return answer
                