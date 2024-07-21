class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        
        L = 0
        R = len(s) - 1
        vowels = 'aeiou'
        while L < R:
            if s[L].lower() in vowels  and s[R].lower() in vowels:
                s[L], s[R] = s[R], s[L]
                L += 1
                R -= 1
            else:
                if s[L].lower() not in vowels:
                    L += 1
                if s[R].lower() not in vowels:
                    R -= 1
        return "".join(s)
            