# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # def inorder(node, answer):
        #     if not node:
        #         return answer
        #     inorder(node.left, answer)
        #     answer.append(node.val)
        #     inorder(node.right, answer)
        #     return answer
        # return inorder(root, [])[k-1]
        stack = [(root, False)]
        
        while stack:
            node, toVisit = stack.pop()
            
            if not node:
                continue
            
            if toVisit:
                k -= 1
                if not k:
                    return node.val
            else:
                stack.extend([(node.right, False),(node, True),(node.left, False)])
            
        
    
        
            
        