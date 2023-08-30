class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minLen = min([len(s) for s in strs])
        commonPrefix = []
        for i in range(minLen):
            charSet = set()
            for s in strs:
                charSet.add(s[i])
            if len(charSet) == 1:
                commonPrefix.append(strs[0][i])
            else:
                break
        return "".join(commonPrefix)
            
        
        
        