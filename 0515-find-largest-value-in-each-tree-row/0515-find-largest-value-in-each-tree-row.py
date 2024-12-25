# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        if not root:
            return answer
        q = collections.deque([root])
        
        while q:
            max_ = float('-inf')
            for _ in range(len(q)):
                node = q.popleft()
                max_ = max(node.val, max_)
                if node.left:
                    q.append(node.left)
                    
                if node.right:
                    q.append(node.right)
                    
            answer.append(max_)
        
        return answer
        