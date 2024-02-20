# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, deque
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        colGroups = defaultdict(list)
        q = deque([(root, 0)])
        minCol = 0
        maxCol = 0
        while q:
            node, col = q.popleft()
            
            colGroups[col].append(node.val)
            minCol = min(minCol, col)
            maxCol = max(maxCol, col)
            
            if node.left:
                q.append((node.left, col - 1))
            
            if node.right:
                q.append((node.right, col + 1))
        answer = []
        for i in range(minCol, maxCol+1):
            answer.append(colGroups[i])
            
        return answer