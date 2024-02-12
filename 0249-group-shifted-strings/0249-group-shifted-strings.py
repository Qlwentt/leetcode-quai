from collections import defaultdict
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        
        for s in strings:
            charToNum = {char: i for i, char in enumerate("abcdefghijklmnopqrstuvwxyz")}
            encode = []
            for i in range(len(s)-1):
                diff = (charToNum[s[i]] - charToNum[s[i+1]]) % 26
                encode.append(diff)
            groups[tuple(encode)].append(s)
            
        return groups.values()