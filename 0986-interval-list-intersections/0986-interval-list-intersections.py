class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # merge two sorted list by start times
        # find the overlap points
        # two pointers
        
        p1 = 0
        p2 = 0
        answer = []
        while p1 < len(firstList) and p2 < len(secondList):
            if firstList[p1][0] < secondList[p2][0]:
                minStart = firstList[p1][0]
                maxStart = secondList[p2][0]
                
            else:
                minStart = secondList[p2][0]
                maxStart = firstList[p1][0]
                
            if firstList[p1][1] < secondList[p2][1]:
                minEnd = firstList[p1][1]
                maxEnd = secondList[p2][1]
                p1 += 1
            else:
                minEnd = secondList[p2][1]
                maxEnd = firstList[p1][1]
                p2 += 1
            if maxStart <= minEnd:
                answer.append([maxStart,minEnd])
        return answer