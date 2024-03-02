class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        p1 = 0
        p2 = 0
        answer = []
        while p1 < len(encoded1) and p2 < len(encoded2):
            val1, freq1 = encoded1[p1] 
            val2, freq2 = encoded2[p2]
            
            ansVal = val1 * val2
            ansFreq = min(freq1, freq2)
            if freq1 < freq2:
                p1 += 1
                encoded2[p2][1] -= freq1
            elif freq2 < freq1:
                p2 += 1
                encoded1[p1][1] -= freq2
            else: # equal
                p1 += 1
                p2 += 1
            
            if answer and answer[-1][0] == ansVal:
                answer[-1][1] += ansFreq
            else:
                answer.append([ansVal, ansFreq])
        
        return answer