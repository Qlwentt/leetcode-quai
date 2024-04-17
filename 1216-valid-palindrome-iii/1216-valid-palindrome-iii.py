class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        memo = {}
        def isKPal(L,R, k):
            if (L,R,k) in memo:
                return memo[(L,R,k)]
            
            while L < R:
                if s[L] != s[R]:
                    if k > 0:
                        answer = isKPal(L+1,R, k-1) or isKPal(L,R-1,k-1)
                        memo[(L,R,k)] = answer
                        return answer
                    else:
                        memo[(L,R,k)] = False
                        return False
                L += 1
                R -= 1
            return True
        return isKPal(0, len(s)-1, k)
            
            
        