from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
    def __str__(self):
        return str(self.val)


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        copy = Node(node.val)
        q = deque([(node, copy)])
        nodesAndCopies = {}
        visited = set()
        
        while q:
            current, currentCopy = q.popleft()
            if current in visited:
                continue
            for neighbor in current.neighbors:
                if neighbor in nodesAndCopies:
                    neighborCopy = nodesAndCopies[neighbor]
                else:
                    neighborCopy = Node(neighbor.val)
                    nodesAndCopies[neighbor] = neighborCopy
                currentCopy.neighbors.append(neighborCopy)
                q.append((neighbor, neighborCopy))
               
            nodesAndCopies[current] = currentCopy
            visited.add(current)
    
        return copy