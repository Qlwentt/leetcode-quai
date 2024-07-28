class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        content = 0
        
        p_child = 0
        p_cookie = 0
        
        while p_cookie < len(s) and p_child < len(g):
            if s[p_cookie] >= g[p_child]:
                p_cookie += 1
                p_child += 1
                content += 1
            else:
                p_cookie += 1
        
        return content
        
        