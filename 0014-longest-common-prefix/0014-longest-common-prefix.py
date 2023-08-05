class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        maxLen = len(max(strs, key=len))
        prefixMap = [[] for _ in range(maxLen)]
        
        for s in strs:
            for i,char in enumerate(s):
                prefixMap[i].append(char)
        prefix = []
        for chars in prefixMap:
            charsSet = set(chars)
            if len(chars) == len(strs) and len(charsSet) == 1:
                prefix.append("".join(charsSet))
            else:
                break
        return "".join(prefix)
        
        
        
        