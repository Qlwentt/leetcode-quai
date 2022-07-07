# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = []
    # def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     if not root:
    #         return None
    #     self.inorderTraversal(root.left)
    #     self.result.append(root.val)
    #     self.inorderTraversal(root.right)
    #     return self.result
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [(root, False)] # (node, toBeVisited)
        res = []
        #LVR
        while stack:
            if stack[-1][1]:
                node, toBeVisited = stack.pop()
                if node:
                    res.append(node.val)
                continue
            node, toBeVisited = stack.pop()
            if not node:
                continue
            stack.extend([(node.right,False),(node,True),(node.left,False)])
        return res