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
            return root
        q = deque([(root, 0)])
        answer = []
        i = 0
        
        while q:
            node, level = q.popleft()
            
            if node.right:
                q.append((node.right, level + 1))
                
            if node.left:
                q.append((node.left, level + 1))
                
            if i == level:
                answer.append(node.val)
                i += 1
        return answer
    
# Time: O(N) touch every node
# Space: O(N) put every node on q