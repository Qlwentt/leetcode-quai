# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root
        q = deque([(root, 1)])
        result = []
        j = 1
        while q:
            level = deque([])
            while q and q[0][1] == j:
                node, i = q.popleft()
                if i % 2:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)
    
                if node.left:
                    q.append((node.left, i+1))
                if node.right:
                    q.append((node.right, i+1))
            j += 1
            result.append(level)
            
        return result   
            
        