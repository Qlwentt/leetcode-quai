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
            
            if curNode.word:
                answer.append(curWord)
                t.removeWord(curWord)
            
            if (row < 0 or col < 0 or
                row >= ROWS or col >= COLS or
                (row,col) in path or
                board[row][col] not in curNode.children or
                curNode.children[board[row][col]].refs < 1
            ):
                return False
            
            
            path.add((row,col))
            
            letter = board[row][col]
            curWord = curWord + letter
            curNode = curNode.children[letter]

            up = backtrack(row-1,col, curWord, curNode)
            down = backtrack(row+1, col, curWord, curNode)
            left = backtrack(row, col-1, curWord, curNode)
            right = backtrack(row, col+1, curWord, curNode)
            
            path.remove((row,col))
            
            return up or down or left or right
        
        for row in range(ROWS):
            for col in range(COLS):
                backtrack(row,col, "", t.root)
                    
        return answer
            