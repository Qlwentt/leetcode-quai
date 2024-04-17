class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        p1 = 0
        p2 = 0
        # max of starts
        # mins of ends
        answer = []
        while p1 < len(firstList) and p2 < len(secondList):
            start1, end1 = firstList[p1]
            start2, end2 = secondList[p2]
            
            intStart = max(start1, start2)
            intEnd = min(end1, end2)
            
            if end1 < end2:
                p1 += 1
            else:
                p2 += 1
            
            if intEnd >= intStart:
                answer.append([intStart, intEnd])
        return answer