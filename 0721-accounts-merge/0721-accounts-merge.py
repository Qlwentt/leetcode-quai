class UnionFind:
    def __init__(self,n):
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
    def union(self, node1,node2):
        root1, root2 = self.find(node1), self.find(node2)
        if root1 == root2:
            return False
        
        if self.ranks[root1] < self.ranks[root2]:
            self.parents[root2] = root1
        elif self.ranks[root2] < self.ranks[root1]:
            self.parents[root1] = root2
        else: # both equal
            self.parents[root1] = root2
            self.ranks[root2] += 1
        return True
        
from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        emailToAccountId = {}
        u = UnionFind(len(accounts))
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in emailToAccountId:
                    i2 = emailToAccountId[email]
                    u.union(i,i2)
                else:
                    emailToAccountId[email] = i
        emailGroups = defaultdict(list)
        for email, id_ in emailToAccountId.items():
            root = u.find(id_)
            emailGroups[root].append(email)
        
        answer = []
        for id_, emails in emailGroups.items():
            answer.append([accounts[id_][0]]+sorted(emails))
        
        return answer
                    