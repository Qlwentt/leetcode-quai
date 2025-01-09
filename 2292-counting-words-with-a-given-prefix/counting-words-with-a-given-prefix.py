class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
            current.count += 1

    def prefix_count(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return 0
            current = current.children[char]
        return current.count
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        # trie = Trie()
        # for word in words:
        #     trie.insert(word)

        # return trie.prefix_count(pref)
        count = 0
        for word in words:
            if len(pref) <= len(word) and word[:len(pref)] == pref:
                count += 1
        return count
