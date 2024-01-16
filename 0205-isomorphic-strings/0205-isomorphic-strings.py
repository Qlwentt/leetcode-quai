class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_to_t = {}
        t_to_s = {}
        
        for i, char in enumerate(s):
            if char in s_to_t:
                if s_to_t[char] != t[i]:
                    return False
            s_to_t[char] = t[i]
        
        for i, char in enumerate(t):
            if char in t_to_s:
                if t_to_s[char] != s[i]:
                    return False
            t_to_s[char] = s[i]
        return True
        