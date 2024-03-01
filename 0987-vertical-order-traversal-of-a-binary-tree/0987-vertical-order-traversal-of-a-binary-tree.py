# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([(root, 0, 0)])
        
        minCol = 0
        maxCol = 0
        answer = []
        groups = defaultdict(list)
        
        while q:
            node, row, col = q.popleft()
            
            groups[col].append((row, node.val))
            minCol = min(col, minCol)
            maxCol = max(col, maxCol)
            
            if node.left:
                q.append((node.left, row+1, col-1))
            
            if node.right:
                q.append((node.right, row+1, col+1))
                
        for i in range(minCol, maxCol+1):
            answer.append([val for row, val in sorted(groups[i])])
            
        return answer
            
        
        