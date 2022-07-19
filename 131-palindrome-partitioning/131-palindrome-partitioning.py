class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        part = []
        
        def dfs(i):
            if i >= len(s):
                result.append(part[:])
                return
            for j in range(i, len(s)):
                word = s[i:j+1]
                if self.isPalindrome(word):
                    part.append(word)
                    dfs(j+1)
                    part.pop()
        dfs(0)
        return result
                
            
        
    
    def isPalindrome(self,word):
        p1 = 0
        p2 = len(word) - 1
        
        while p1 < p2:
            if word[p1] != word[p2]:
                return False
            p1 += 1
            p2 -= 1
        return True