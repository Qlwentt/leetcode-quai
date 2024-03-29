class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
        self.refs = 0
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word):
        cur = self.root
        cur.refs +=1
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
            cur.refs +=1
            
        cur.word = True
    
    def removeWord(self, word):
        cur = self.root
        cur.refs -= 1
        for char in word:
            if char in cur.children:
                cur = cur.children[char]
                cur.refs -= 1
        cur.word = False
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        t = Trie()
        for word in words:
            t.addWord(word)
        
        ROWS = len(board)
        COLS = len(board[0])
        path = set()
        answer = []
        

        def backtrack(row,col, curWord, curNode):
            if (row < 0 or col < 0 or
                row >= ROWS or col >= COLS or
                (row,col) in path or
                board[row][col] not in curNode.children or
                curNode.children[board[row][col]].refs < 1
            ):
                return
            
            
            path.add((row,col))
            
            letter = board[row][col]
            curWord = curWord + letter
            curNode = curNode.children[letter]
            
            if curNode.word:
                answer.append(curWord)
                t.removeWord(curWord)

            backtrack(row-1,col, curWord, curNode)
            backtrack(row+1, col, curWord, curNode)
            backtrack(row, col-1, curWord, curNode)
            backtrack(row, col+1, curWord, curNode)
    
            path.remove((row,col))
            
        
        for row in range(ROWS):
            for col in range(COLS):
                backtrack(row,col, "", t.root)
                    
        return answer
            