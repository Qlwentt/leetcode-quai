from collections import defaultdict
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        sDict = defaultdict(list)
        charToNum = {char: i for i, char in enumerate("abcdefghijklmnopqrstuvwxyz")}
        
        def encode(s):
            answer = []
            for i in range(len(s)-1):
                distance = (charToNum[s[i+1]] - charToNum[s[i]]) % 26
                answer.append(distance)
            return tuple(answer)
        
        for s in strings:
            sDict[encode(s)].append(s)
        
        return sDict.values()