class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        p1 = 0
        p2 = 0
        answer = []
        while p1 < len(encoded1) and p2 < len(encoded2):
            val1, freq1 = encoded1[p1]
            val2, freq2 = encoded2[p2]
            
            if freq1 == freq2:
                freqAnswer = freq1
                p1 += 1
                p2 += 1
            elif freq1 < freq2:
                freqAnswer = freq1
                encoded2[p2][1] = freq2-freq1
                p1 += 1
            else: # freq1 > freq2
                freqAnswer = freq2
                encoded1[p1][1] = freq1 - freq2
                p2 += 1
            
            valAnswer = val1 * val2
            
            if answer and answer[-1][0] == valAnswer:
                answer[-1] = [valAnswer, freqAnswer + answer[-1][1]]
            else:
                answer.append([valAnswer, freqAnswer])
                
        return answer
    
# Time: O(M+N)
# Space: O(M+N)