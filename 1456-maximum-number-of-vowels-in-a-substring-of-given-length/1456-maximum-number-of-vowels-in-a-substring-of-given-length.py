class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_vowels = 0
        cur_vowels = 0
        vowels = "aeiou"
        L = 0
        for R in range(len(s)):
            while R-L+1 > k:
                cur_vowels -= 1 if s[L] in vowels else 0
                L += 1
            cur_vowels += 1 if s[R] in vowels else 0
            if R-L+1 == k:
                max_vowels = max(cur_vowels, max_vowels)
        
        return max_vowels
    
    # Time: O(N)
    # Space: O(1)
                