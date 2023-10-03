class Solution:
    def partition(self, s: str) -> List[List[str]]:

        parts = []
        
        def isPalindrome(word):
            L = 0
            R = len(word) - 1
            
            while L < R:
                if word[L] != word[R]:
                    return False
                L += 1
                R -= 1
            return True

        def backtrack(i, curPart):
            if i >= len(s):
                parts.append(curPart.copy())
                return

            
            for j in range(i,len(s)):
                part = s[i:j+1]
                if not isPalindrome(part):
                    continue
                curPart.append(part)
                backtrack(j+1,curPart)
                curPart.pop()

        backtrack(0,[])
        return parts
            
        
                
            
        