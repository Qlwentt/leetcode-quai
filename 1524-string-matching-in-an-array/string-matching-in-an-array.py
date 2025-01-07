class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        substrings = set()
        for word in words:
            for i in range(len(word)):
                for j in range(i, len(word)):
                    if not (i==0 and j==len(word)-1):
                        substrings.add(word[i:j+1])
            
        
        answer = []
        for word in words:
            if word in substrings:
                answer.append(word)

        return answer

     