class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        p1 = 0
        p2 = 0
        answer = []
        while p1 < len(firstList) and p2 < len(secondList):
            start1, end1 = firstList[p1]
            start2, end2 = secondList[p2]
            
            newStart = max(start1, start2)
            newEnd = min(end1, end2)
            
            if end1 < end2:
                p1 += 1
            else:
                p2 += 1
            
            if newEnd >= newStart:
                answer.append([newStart, newEnd])
                
        return answer