class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        def get_max(sequence):
            p = 0
            count = 0
            answer = 0
            for char in sequence:
                if char == word[p]:
                    if p == len(word) - 1:
                        count += 1
                        p = 0
                        answer = max(answer, count)
                    else:
                        p += 1
                else:
                    count = 0
                    p = 0
            return answer
        
        answer = 0
        for i in range(len(sequence)):
            for j in range(i, len(sequence)):
                substring = sequence[i:j+1]
                answer = max(get_max(substring), answer)
        return answer
                
            
        