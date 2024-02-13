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
        
        q = deque([root])
        answer = []
        while q:
            seen = False
            for _ in range(len(q)):
                node = q.popleft()
                if not seen:
                    answer.append(node.val)
                    seen = True
                
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
        return answer