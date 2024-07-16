class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(L,R):
            if L < R:
                s[L], s[R] = s[R], s[L]
                reverse(L+1,R-1)
        reverse(0, len(s)-1)
    
    # Time: O(N)
    # Space: O(N)
        
        
        