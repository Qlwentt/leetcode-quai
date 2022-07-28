from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        adjList = defaultdict(list)
        wordList.append(beginWord)
        
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                adjList[pattern].append(word)
                
        visited = set()
        q = deque([(beginWord, 1)])
        
        while q:
            word, level = q.popleft()
            if word == endWord:
                return level
            if word in visited:
                continue
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                for neigh in adjList[pattern]:
                    if neigh == word:
                        continue
                    q.append((neigh, level+1))
            visited.add(word)
        return 0
        