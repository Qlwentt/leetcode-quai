# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = []
#     def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         #LRV
#         if not root:
#             return self.result
        
#         self.postorderTraversal(root.left)
#         self.postorderTraversal(root.right)
#         self.result.append(root.val)
#         return self.result
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [(root, False)]
        result = []
        #LRV
        while stack:
            node, toBeVisited = stack.pop()
            if not node:
                continue
            if toBeVisited:
                result.append(node.val)
            else:
                stack.extend([(node,True),(node.right,False),(node.left,False)])
                
        return result
                
                    