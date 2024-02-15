# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = deque([(root, 0,0)])
        colGroups = defaultdict(list)
        minCol = 0
        maxCol = 0
        while q:
            node, r, c = q.popleft()
            colGroups[c].append((r, node.val))
            minCol = min(minCol, c)
            maxCol = max(maxCol, c)
            if node.left:
                q.append((node.left, r+1, c-1))
            
            if node.right:
                q.append((node.right, r+1, c+1))
        answer = []
        for i in range(minCol, maxCol+1):
            answer.append([val for row, val in sorted(colGroups[i])])
            
        return answer
        