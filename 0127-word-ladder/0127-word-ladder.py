class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    
        wordList.append(beginWord)
        adjList = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                adjList[pattern].append(word)
        
        q = collections.deque([(beginWord,1)])
        visited = set([beginWord])
        
        while q:
            word, distance = q.popleft()
            if word == endWord:
                return distance
            
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                for neigh in adjList[pattern]:
                    if neigh not in visited:
                        q.append((neigh, distance+1))
                        visited.add(neigh)
            
        return 0
            