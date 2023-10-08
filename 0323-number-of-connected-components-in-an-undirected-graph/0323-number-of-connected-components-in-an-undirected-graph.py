class UnionFind:
    def __init__(self,n):
        self.parents = {}
        self.rank = {}
        self.components = n
        
        for i in range(n):
            self.parents[i] = i
            self.rank[i] = 1
    
    def find(self,node):
        parent = self.parents[node]
        
        while parent != self.parents[parent]:
            self.parents[parent] = self.parents[self.parents[parent]]
            parent = self.parents[parent]
        return parent
    
    def union(self,node1,node2):
        root1,root2 = self.find(node1),self.find(node2)
        if root1 == root2:
            return False
        
        if self.rank[root1] > self.rank[root2]:
            self.parents[root2] = root1
        elif self.rank[root2] > self.rank[root1]:
            self.parents[root1] = root2
        else:
            self.parents[root2] = root1
            self.rank[root1] += 1
        self.components -= 1
        return True
        
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        u = UnionFind(n)
        for n1, n2 in edges:
            u.union(n1,n2)
        return u.components
        