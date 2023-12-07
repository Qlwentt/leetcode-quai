from collections import defaultdict
class UnionFind:
    def __init__(self, n):
        self.parents = {}
        self.ranks = {}
        
        for i in range(n):
            self.parents[i] = i
            self.ranks[i] = 1
    def find(self, node):
        parent = self.parents[node]
        
        while parent != self.parents[parent]:
            self.parents[parent] = self.parents[self.parents[parent]]
            parent = self.parents[parent]
        return parent
    
    def union(self, x,y):
        rootX, rootY = self.find(x), self.find(y)
        
        if rootX == rootY:
            return False
        
        if self.ranks[rootX] < self.ranks[rootY]:
            self.parents[rootY] = rootX
        elif self.ranks[rootY] < self.ranks[rootX]:
            self.parents[rootX] = rootY
        else:
            self.parents[rootX] = rootY
            self.ranks[rootY] += 1


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailsToAccount = {}
        u = UnionFind(len(accounts))
        
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in emailsToAccount:
                    u.union(i, emailsToAccount[email])
                else:
                    emailsToAccount[email] = i
        emailGroups = defaultdict(list)
        for email, node in emailsToAccount.items():
            parent = u.find(node)
            emailGroups[parent].append(email)
        
        answer = []
        for i , emails in emailGroups.items():
            answer.append([accounts[i][0]]+sorted(emails))
            
        return answer