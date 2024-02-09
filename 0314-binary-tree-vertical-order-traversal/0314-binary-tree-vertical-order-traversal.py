# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        q = deque([(root, 0)])
        colToValues = defaultdict(list)
        minCol = float('inf')
        maxCol = float('-inf')
        
        while q:
            node, col = q.popleft()
            
            colToValues[col].append(node.val)
            minCol = min(col, minCol)
            maxCol = max(col, maxCol)
            
            if node.left:
                q.append((node.left, col - 1))

            if node.right:
                q.append((node.right, col + 1))
        
        answer = []
        for i in range(minCol,maxCol+1):
            answer.append(colToValues[i])
            
        return answer
        
        