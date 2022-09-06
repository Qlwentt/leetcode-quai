from collections import defaultdict, Counter
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        sortedString = []
        counts = Counter(s)
        
        for char in order:
            if char in counts and counts[char] > 0:
                sortedString.append(char*counts[char])
                counts[char] = 0
        for char, count in counts.items():
            if count > 0:
                sortedString.append(char*counts[char])
                counts[char] = 0
        return "".join(sortedString)
        