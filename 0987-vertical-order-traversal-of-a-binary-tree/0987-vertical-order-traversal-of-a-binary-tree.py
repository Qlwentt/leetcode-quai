# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # left and down = (row+1, col-1)
        # right and down = (row+1, col+1)
        if not root:
            return root
        minCol = float('inf')
        maxCol = float('-inf')
        colMap = defaultdict(list)
        q = deque([(0,0, root)])
        
        while q:
            row, col, node = q.popleft()
            
            minCol = min(col, minCol)
            maxCol = max(col, maxCol)
            
            colMap[col].append((row, node.val))
            
            if node.left:
                q.append((row+1, col-1, node.left))
            if node.right:
                q.append((row+1,col+1, node.right))
        answer = [] 
        for i in range(minCol, maxCol+1):
            answer.append([val for row, val in sorted(colMap[i])])
            
        return answer
        
    # Time: N log N
    # Space: N
            
        
        
        
            