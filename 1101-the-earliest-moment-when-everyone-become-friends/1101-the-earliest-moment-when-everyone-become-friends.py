class UnionFind:
    def __init__(self,n):
        self.parents = {i:i for i in range(n)}
        self.rank = {i:1 for i in range(n)}
        self.components = n
    
    def find(self, node):
        parent = self.parents[node]
        while self.parents[parent] != parent:
            self.parents[parent] = self.parents[self.parents[parent]]
            parent = self.parents[parent]
        return parent
    
    def union(self, node1, node2):
        parent1 = self.find(node1)
        parent2 = self.find(node2)
        if parent1 == parent2:
            return False
        
        if self.rank[parent1] < self.rank[parent2]:
            self.parents[parent2] = parent1
        elif self.rank[parent2] < self.rank[parent1]:
            self.parents[parent1] = parent2
        else: # same
            self.parents[parent1] = parent2
            self.rank[parent2] += 1
        self.components -= 1
        return True



class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort()
        u = UnionFind(n)
        for time, a, b in logs:
            u.union(a,b)
            if u.components == 1:
                return time
        return -1
        
        
        
            
        
        