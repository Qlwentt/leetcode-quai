class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            if not char in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.word = True

    def search(self, word: str) -> bool:
        def rec_search(word, cur):
            for i, char in enumerate(word):
                if char == ".":
                    options = [rec_search(word[i+1:], cur.children[child]) for child in cur.children.keys()]
                    return any(options)
                else:
                    if not char in cur.children:
                        return False
                    cur = cur.children[char]
            return cur.word
        return rec_search(word, self.root)
    


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)