# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        q = collections.deque([root])
        count = 0
        while q:
            level = []
            i = 0
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)     
                
                if node.left:
                    q.append(node.left)
                    
                if node.right:
                    q.append(node.right)
            ideal = sorted(level)
            indexes_level = {num: i for i, num in enumerate(level)}
            for i, num in enumerate(level):
                if level[i] != ideal[i]:
                    correct_index = indexes_level[ideal[i]]
                    level[i],level[correct_index] = level[correct_index], level[i]
                    
                    indexes_level[level[correct_index]] = correct_index
                    indexes_level[level[i]] = i
                    
                    count += 1
                    
        return count
            
            
            