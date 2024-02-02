from collections import defaultdict
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
    
    def union(self, node1, node2):
        parent1, parent2 = self.find(node1), self.find(node2)
        if parent1 == parent2:
            return False
        
        if self.ranks[parent1] < self.ranks[parent2]:
            self.parents[parent2] = parent1
        elif self.ranks[parent2] < self.ranks[parent1]:
            self.parents[parent1] = parent2
        else: # ranks are the same
            self.parents[parent1] = parent2
            self.ranks[parent2] += 1
        return True
    
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailToAccountId = {}
        u = UnionFind(len(accounts))
        for i, accountList in enumerate(accounts):
            for email in accountList[1:]:
                if email in emailToAccountId:
                    u.union(i, emailToAccountId[email])
                else:
                    emailToAccountId[email] = i
        
        emailGroups = defaultdict(list)
        for email, accountId in emailToAccountId.items():
            parentAccount = u.find(accountId)
            emailGroups[parentAccount].append(email)
        
        answer = []
        for accountId, emails in emailGroups.items():
            answer.append([accounts[accountId][0]] + sorted(emails))
        return answer
    
# Time: O (NKlog(NK))
# Space O (NK)