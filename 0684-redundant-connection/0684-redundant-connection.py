class UnionFind:
    def __init__(self, n):
        self.parents = {}
        self.rank = {}
        
        for i in range(1, n+1):
            self.parents[i] = i
            self.rank[i] = 1
    
    def find(self,node):
        parent = self.parents[node]
        while parent != self.parents[parent]:
            self.parents[parent] = self.parents[self.parents[parent]]
            parent = self.parents[parent]
        return parent
    
    def union(self, node1, node2):
        root1, root2 = self.find(node1), self.find(node2)
        
        if root1 == root2:
            return False
        
        # make larger rank the parent of the smaller rank
        if self.rank[root1] > self.rank[root2]: 
            self.parents[root2] = root1
        elif self.rank[root2] > self.rank[root1]:
            self.parents[root1] = root2
        else:
            self.parents[root2] = root1
            self.rank[root1] += 1
            
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # find the edge that makes graph have a cycle
        n = len(edges)
        u = UnionFind(n)
        
        for parent, node in edges:
            if not u.union(parent, node):
                return [parent, node]
        