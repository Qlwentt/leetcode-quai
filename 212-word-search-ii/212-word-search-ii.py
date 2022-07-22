class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    
    def addWord(self, word):
        current = self
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.endOfWord = True
    
    def pruneWord(self, word) -> None:
        cur: TrieNode = self
        nodeAndChildKey: list[tuple[TrieNode, str]] = []
        for char in word:
            nodeAndChildKey.append((cur, char))
            cur = cur.children[char]

        for parentNode, childKey in reversed(nodeAndChildKey):
            targetNode = parentNode.children[childKey]
            if len(targetNode.children) == 0:
                del parentNode.children[childKey]
            else:
                return
    
    
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)
        
        foundWords = set()
        
        numRows = len(board)
        numCols = len(board[0])
        
        path = set()
        
        def dfs(r,c, node, word):
            

            if (r < 0 or c < 0 
                or r >= numRows
                or c >= numCols
                or (r,c) in path
                or board[r][c] not in node.children
            ):
                return
            
            
            
            
            char = board[r][c]
            word.append(char)
            path.add((r,c))
            node = node.children[char]
            
            if node.endOfWord:
                foundWords.add("".join(word))
                node.endOfWord = False
                root.pruneWord(word)
            
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word) 
            dfs(r, c + 1, node, word) 
            dfs(r, c - 1, node, word)
            
            word.pop()
            path.remove((r,c))
        for row in range(numRows):
            for col in range(numCols):
                dfs(row, col, root, [])
    
        return foundWords
               
            
            
            
        