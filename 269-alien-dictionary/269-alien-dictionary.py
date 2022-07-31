from collections import defaultdict
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        adjList = {char: set() for word in words for char in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):

                if w1[j] != w2[j]:
                    adjList[w1[j]].add(w2[j])
                    break
                
        
        visiting = set()
        visited = set()
        order = []
        def visitInOrder(node):
            if node in visiting:
                return False
            if node in visited:
                return True
            visiting.add(node)
            
            for neigh in list(adjList[node]):
                if not visitInOrder(neigh):
                    return False
            visiting.remove(node)
            visited.add(node)
            order.append(node)
            return True
        nodes = list(adjList.keys())
        for i in adjList:
            if not visitInOrder(i):
                return ""
        order.reverse()
        return "".join(order)
    
    
                