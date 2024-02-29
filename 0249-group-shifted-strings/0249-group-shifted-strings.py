from collections import defaultdict
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strings:
            encoded = []
            letterToNum = {char:i for i, char in enumerate("abcdefghijklmnopqrstuvwxyz")}
            for i in range(len(s)-1):
                encoded.append((letterToNum[s[i]] - letterToNum[s[i+1]]) % 26)
            groups[tuple(encoded)].append(s)
            
        return groups.values()