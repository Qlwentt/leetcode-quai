# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque([(root, 1)])
        i = 1
        result = []
        while q:
            node, j = q.popleft()

            if node.right:
                q.append((node.right, j+1))
            if node.left:
                q.append((node.left, j+1))
            if i == j:
                result.append(node.val)
                i += 1
        return result
        
        