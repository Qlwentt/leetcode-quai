class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # g = array of child greeds
        # s = array of cookie sizes
        g.sort()
        s.sort() 
        
        
        child = 0
        cookie = 0
        
        while cookie < len(s) and child < len(g):
            if s[cookie] >= g[child]:
                child += 1
            cookie += 1
        
        return child
        
    # Time: O(NlogN + MlogM)
    # Space: O(N+M) (because sorting in python takes O(N) space)