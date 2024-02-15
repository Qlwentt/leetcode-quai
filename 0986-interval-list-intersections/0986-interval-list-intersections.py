class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        p1 = 0
        p2 = 0
        answer = []
        while p1 < len(firstList) and p2 < len(secondList):
            start1, end1 = firstList[p1]
            start2, end2 = secondList[p2]
                        
            if end1 < end2:
                p1 += 1
            else:
                p2 += 1
            
            sIntersection = max(start1, start2)
            eIntersection = min(end1, end2)
            
            if eIntersection >= sIntersection:
                answer.append([sIntersection, eIntersection])
                
        return answer