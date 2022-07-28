from collections import deque
# Definition for a Node.
# class Node:
#     def __init__(self, val = 0, neighbors = None):
#         self.val = val
#         self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        copy = Node(node.val)
        q = deque([(node, copy)])
        visited = set()
        nodeAndCopy = {} #key : node, value: copy
        
        while q:
            currentNode, currentCopy = q.popleft()
            if currentNode in visited:
                continue
            for neigh in currentNode.neighbors:
                if neigh not in nodeAndCopy:
                    copiedNeigh = Node(neigh.val)
                    nodeAndCopy[neigh] = copiedNeigh
                copiedNeigh = nodeAndCopy[neigh]
                currentCopy.neighbors.append(copiedNeigh)
                q.append((neigh, copiedNeigh))
            nodeAndCopy[currentNode] = currentCopy
            visited.add(currentNode)
        
        return copy
            