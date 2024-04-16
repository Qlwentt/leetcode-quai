from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        q = deque([root])
        answer = []
        while q:
            hasOutputted = False
            for _ in range(len(q)):
                node = q.popleft()
                if not hasOutputted:
                    answer.append(node.val)
                    hasOutputted = True
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
        return answer
            
        