class TrieNode:
    def __init__(self):
        self.children = {} # key - letter, value - Node
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(root, j):  
            current = root
            for i in range(j,len(word)):
                char = word[i]
                if char == ".":
                    for child in current.children.values():
                        if dfs(child, i+1):
                            return True
                    return False
                else:
                    if char not in current.children:
                        return False
                    current = current.children[char]
            return current.endOfWord
        return dfs(self.root, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)