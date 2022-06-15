class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        
        while right > left:
            leftLetter = s[left]
            rightLetter = s[right]
            
            if not leftLetter.isalnum():
                left += 1
                continue
            if not rightLetter.isalnum():
                right -= 1
                continue
            
            if leftLetter.lower() != rightLetter.lower():
                return False
            left += 1
            right -= 1
        return True
# O(n) time
# O(1) space