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
    
    def union(self, n1, n2):
        p1,p2 = self.find(n1), self.find(n2)
        
        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.parents[p2] = p1
        elif self.rank[p2] > self.rank[p1]:
            self.parents[p1] = p2
        else:
            self.parents[p2] = p1
            self.rank[p1] += 1
        self.components -= 1
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        u = UnionFind(n)
        for n1, n2 in edges:
            if not u.union(n1,n2):
                return False
            
        return u.components == 1
        