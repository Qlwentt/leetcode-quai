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
        seenEmpty = False
        while q:
            node = q.popleft()
            
            if node:
                if seenEmpty:
                    return False
                q.append(node.left)
                q.append(node.right)
            else:
                seenEmpty = True
        
        return True
                