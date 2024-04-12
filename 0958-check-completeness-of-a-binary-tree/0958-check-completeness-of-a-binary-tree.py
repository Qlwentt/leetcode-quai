# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        seenGap = False
        while q:
            node = q.popleft()
            if seenGap and node:
                return False
            if not node:
                seenGap = True
            else:   
                q.append(node.left)
                q.append(node.right)
        return True
    