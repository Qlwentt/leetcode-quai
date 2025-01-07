class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        word = collections.deque(list(word))
        while word: 
            cur = self.root
            for char in word:
                if char not in cur.children:
                    cur.children[char] = TrieNode()
                cur = cur.children[char]
                cur.count += 1
            word.popleft()
    
    def is_substring(self,word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return cur.count > 1

    

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        answer = []
        for word in words:
            if trie.is_substring(word):
                answer.append(word)

        return answer
        

     