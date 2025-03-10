class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class SuffixTrie:
    def __init__(self):
        self.root = TrieNode()
    
    def add_word(self, word):
        cur = self.root
        for char in reversed(word):
            if not char in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.end_of_word = True
    
    def is_suffix(self, word):
        cur = self.root
        for char in reversed(word):
            if not char in cur.children:
                return False
            cur = cur.children[char]
            if cur.end_of_word:
                return True
            
        return False
            
class StreamChecker:
    

    def __init__(self, words: List[str]):
        self.cur_word = ""
        self.trie = SuffixTrie()
        for word in words:
            self.trie.add_word(word)

    def query(self, letter: str) -> bool:
        self.cur_word += letter
        return self.trie.is_suffix(self.cur_word)
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)