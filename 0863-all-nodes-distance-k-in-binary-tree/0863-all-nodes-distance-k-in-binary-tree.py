# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict, deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        adjList = defaultdict(list)
        
        def dfs(root):
            if not root:
                return
            if root.left:
                adjList[root].append(root.left)
                adjList[root.left].append(root)
            if root.right:
                adjList[root].append(root.right)
                adjList[root.right].append(root)
                
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        q = deque([(target, 0)])
        visited = set([target])
        answer = []
        while q:
            node, distance = q.popleft()
            if distance == k:
                answer.append(node.val)
            elif distance > k:
                break
            
            for neigh in adjList[node]:
                if neigh not in visited:
                    q.append((neigh, distance+1))
                    visited.add(neigh)
                    
        return answer
        