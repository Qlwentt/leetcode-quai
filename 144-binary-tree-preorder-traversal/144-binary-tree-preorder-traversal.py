# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = []
    # def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     # VLR
    #     if not root:
    #         return self.result
    #     self.result.append(root.val)
    #     self.preorderTraversal(root.left)
    #     self.preorderTraversal(root.right)
    #     return self.result
    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [(root, False)]
        result = []
        # VLR
        while stack:
            if stack[-1][1]:
                node, toBeVisited = stack.pop()
                if node:
                    result.append(node.val)
                continue
            node, toBeVisited = stack.pop()
            if not node:
                continue
            stack.extend([(node.right,False),(node.left,False),(node,True)])
        return result