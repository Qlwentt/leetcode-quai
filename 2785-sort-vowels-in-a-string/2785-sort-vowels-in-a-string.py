class Solution:
    def sortVowels(self, s: str) -> str:
        vowelIndexes = [i for i, char in enumerate(s) if char.lower() in "aeiou"]
        answer = list(s)
        bucket = [0] * 128
        sortedVowels = []
        for i in vowelIndexes:
            asciiVal = ord(s[i])
            bucket[asciiVal] += 1
            
        for i, count in enumerate(bucket):
            sortedVowels.append(count * chr(i))
        
        sortedVowels = collections.deque(list("".join(sortedVowels)))
        
        for i in vowelIndexes:
            answer[i] = sortedVowels.popleft()
                                         
        return "".join(answer)
        
        