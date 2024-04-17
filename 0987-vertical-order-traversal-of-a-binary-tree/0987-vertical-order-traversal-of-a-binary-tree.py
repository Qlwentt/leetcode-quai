# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([(root, 0,0)])
        colGroups = defaultdict(list)
        minCol = 0
        maxCol = 0
        while q:
            node, row, col = q.popleft()
            minCol = min(col, minCol)
            maxCol = max(col, maxCol)
            colGroups[col].append((row,node.val))
            if node.left:
                q.append((node.left, row+1,col-1))
            
            if node.right:
                q.append((node.right, row+1, col+1))
        answer = []
        for i in range(minCol, maxCol+1):
            answer.append([val for row, val in sorted(colGroups[i])])
            
        return answer
        
        