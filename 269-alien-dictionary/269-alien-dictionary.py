from collections import defaultdict
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        adjList = {char: set() for word in words for char in word}
    

        def getEdge(word1,word2):
            p1 = 0
            p2 = 0
            while p1 < len(word1):
                char1 = word1[p1]
                char2 = word2[p2] if p2 < len(word2) else None
                if not char2:
                    return -1
                if char1 != char2:
                    return [char1, char2]
                p1 += 1
                p2 += 1
            return None
        
        for i in range(len(words)):
            word1 = words[i]
            for j in range(i+1, len(words)):
                word2 = words[j]
                edge = getEdge(word1,word2)
                if not edge:
                    continue
                if edge == -1:
                    return ""
                node, neigh = edge
                adjList[node].add(neigh)
                
        
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
        for i in nodes:
            if not visitInOrder(i):
                return ""
        order.reverse()
        return "".join(order)
    
    
                