from collections import defaultdict
class UnionFind:
    def __init__(self, n):
        self.parents = {i: i for i in range(n)}
        self.ranks = {i:1 for i in range(n)}
    
    def find(self, node):
        parent = self.parents[node]
        
        while self.parents[parent] != parent:
            self.parents[parent] = self.parents[self.parents[parent]]
            parent = self.parents[parent]
        
        return parent
    
    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 == root2:
            return False
        
        if self.ranks[root1] < self.ranks[root2]:
            self.parents[root2] = root1
        elif self.ranks[root2] < self.ranks[root1]:
            self.parents[root1] = root2
        else:
            self.parents[root1] = root2
            self.ranks[root2] += 1
        
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailToId = {}
        u = UnionFind(len(accounts))
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in emailToId:
                    j = emailToId[email]
                    u.union(i,j)
                else:
                    emailToId[email] = i
        emailGroups = defaultdict(list)
        for email, id_ in emailToId.items():
            baseAccount = u.find(id_)
            emailGroups[baseAccount].append(email)
        answer = []
        for account, emails in emailGroups.items():
            answer.append([accounts[account][0]] + sorted(emails))
        
        return answer
        