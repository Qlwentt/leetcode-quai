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
        self.trie = SuffixTrie()
        self.stream = collections.deque([])
        self.len_stream = 0
        for word in words:
            self.trie.add_word(word)
            self.len_stream = max(len(word), self.len_stream)

    def query(self, letter: str) -> bool:
        self.stream.append(letter)
        if len(self.stream) > self.len_stream:
            self.stream.popleft()
        return self.trie.is_suffix(self.stream)

# Constructor: 
# N = # of words
# M = length of longest word       
# Time: O(N*M)
# Space: O(N*M)

# Query Function:
# M = length of longest word
# Time: O(M)
# Space: O(M) (stream datastructure is limited to length of longest word)

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)