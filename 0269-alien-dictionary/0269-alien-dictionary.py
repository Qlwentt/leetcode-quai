class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adjList = {char: set() for word in words for char in word}
        
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2:
                return ""
            
            for fromChar, toChar in zip(w1[:minLen], w2[:minLen]):
                if fromChar != toChar:
                    adjList[fromChar].add(toChar)
                    break
        print(adjList)       
        visited = set()
        visiting = set()
        answer = []
        def topSort(node):
            if node in visiting:
                return False
            if node in visited:
                return True
            
            visited.add(node)
            visiting.add(node)
            for neigh in adjList[node]:
                if not topSort(neigh):
                    return False
            answer.append(node)
            visiting.remove(node)
            return True
        
        for letter in adjList.keys():
            if not topSort(letter):
                return ""
        answer.reverse()
        return "".join(answer)
        