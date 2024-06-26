class Solution:
    def longestPalindrome(self, s: str) -> str:
        def longest_pal(L,R):
            longest = 0
            maxL = 0
            maxR = 0
            
            while L >= 0 and R < len(s):
                if s[L] != s[R]:
                    break
                if R-L+1 > longest:
                    maxL = L
                    maxR = R
                    longest = R-L+1
                L -= 1
                R += 1
            return [longest, maxL, maxR]
        maxL = 0
        maxR = 0
        longest = 0
        for i in range(len(s)):
            even_length, evenL, evenR = longest_pal(i,i+1)
            odd_length,oddL, oddR = longest_pal(i,i)
            longest = max(even_length, odd_length, longest)
            if even_length == longest:
                maxL = evenL
                maxR = evenR
            elif odd_length == longest:
                maxL = oddL
                maxR = oddR
        return s[maxL:maxR+1]
            
            
        
        
        
        