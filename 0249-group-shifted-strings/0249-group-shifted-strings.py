from collections import defaultdict
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        sDict = defaultdict(list)
        charToNum = {char: i for i, char in enumerate("abcdefghijklmnopqrstuvwxyz")}
        def encode(s):
            code = []
            
            for i in range(len(s)-1):
                code.append((charToNum[s[i]]-charToNum[s[i+1]])%26)
            return tuple(code)
        for s in strings:
            sDict[encode(s)].append(s)
            
        return list(sDict.values())
