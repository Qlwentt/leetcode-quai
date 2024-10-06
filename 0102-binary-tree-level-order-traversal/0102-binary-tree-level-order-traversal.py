# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        q = deque([(root, 1)])
        i = 1
        while q:
            level = []
            while q and q[0][1] == i:
                node, j = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append((node.left, j+1))
                if node.right:
                    q.append((node.right, j+1))
            i += 1
            result.append(level)
        return result
    
# Time: O(N)
# Space: O(N) it is O(max number of nodes in a level) for tree with 2 children per node the number of nodes in the last level is (N+1)/2. If you ignore constants that's O(N) 