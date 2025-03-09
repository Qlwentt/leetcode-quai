class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        # def is_palindrome(word):
        #     l = 0
        #     r = len(word) - 1
            
        #     while l < r:
        #         if word[l] != word[r]:
        #             return False
        #         l += 1
        #         r -= 1
        #     return True
        
        # for word in words:
        #     if is_palindrome(word):
        #         return word
        # return ""
    # Time: O(N*M)
    # Space: O(1)
        for word in words:
            if list(word) == list(reversed(word)):
                return word
        return ""