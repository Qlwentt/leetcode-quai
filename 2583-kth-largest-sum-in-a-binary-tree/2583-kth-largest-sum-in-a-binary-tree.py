# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        q = collections.deque([root])
        sums_ = []
        levels = 0
        while q:
            level_sum = 0
            levels += 1
            for _ in range(len(q)):
                node = q.popleft()
                
                level_sum += node.val
                
                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            
            sums_.append((level_sum))
        
        if k > levels:
            return -1
        return heapq.nlargest(k, sums_)[-1]
        