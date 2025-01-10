from collections import Counter, defaultdict
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        counts1 = [Counter(word) for word in words1]
        counts2 = [Counter(word) for word in words2]
        max_counts2 = defaultdict(int)
        for letter in "abcdefghijklmnopqrstuvwxyz":
            for count2 in counts2:
                max_counts2[letter] = max(count2[letter], max_counts2[letter])
        answer = []
        for i, word1 in enumerate(counts1):
            for letter in "abcdefghijklmnopqrstuvwxyz":
                if word1[letter] < max_counts2[letter]:
                    break
            else:
                answer.append(words1[i])
        
        return answer