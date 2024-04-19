class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        # [[2,1],[5,5],[1,5],[2,5],[4,2],[5,3],[1,2],[4,3],[3,2],[2,3]]
        #          A
        # [[1,1],[4,1],[3,3],[5,3],[1,4],[5,1],[4,1],[5,3],[3,5],[2,1]
        #                B
        
        # [2,1][8,1]
        
        
        p1 = 0
        p2 = 0
        answer = []
        while p1 < len(encoded1) and p2 < len(encoded2):
            val1, freq1 = encoded1[p1]
            val2, freq2 = encoded2[p2]
            
            ansFreq = min(freq1, freq2)
            ansVal = val1 * val2
            
            if freq1 < freq2:
                newFreq = freq2 - freq1
                encoded2[p2][1] = newFreq  
                p1 += 1
            elif freq2 < freq1:
                newFreq = freq1 - freq2
                encoded1[p1][1] = newFreq
                p2 += 1
            else:
                p1 += 1
                p2 += 1
            
            if not answer or answer[-1][0] != ansVal:
                answer.append([ansVal, ansFreq])
            else:
                answer[-1][1] = answer[-1][1] + ansFreq
            
        return answer