class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split (" ")
        
        def reverse(word):
            word = list(word)
            l = 0
            r = len(word) - 1
            
            while l < r:
                word[l], word[r] = word[r], word[l]
                l += 1
                r -= 1
            return "".join(word)
        reversed_words = []
        for word in s:
            reversed_words.append(reverse(word))
        return " ".join(reversed_words)
        