class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = []
        
        minLen = len(min(strs, key=len))
        
        for i in range(minLen):
            target = strs[0][i]
            common = True
            for s in strs[1:]:
                if s[i] != target:
                    common = False
            if common:
                lcp.append(target)
            else:
                break
                    
        
        return "".join(lcp)