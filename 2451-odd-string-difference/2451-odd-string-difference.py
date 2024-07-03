class Solution:
    def oddString(self, words: List[str]) -> str:
        differences = collections.defaultdict(lambda: [0, ""])
        for word in words:
            difference = []
            for i in range(1,len(word)):
                prev = word[i-1]
                char = word[i]
                difference.append(ord(char) - ord(prev))
            differences[tuple(difference)][0] += 1
            differences[tuple(difference)][1] = word
        
        for key in differences:
            count, word = differences[key]
            if count == 1:
                return word
        