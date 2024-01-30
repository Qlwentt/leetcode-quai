class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # merge two sorted list by start times
        # find the overlap points
        # two pointers
        
        # to get overlap point
        # max start times
        # min of end times
        
        p1 = 0
        p2 = 0
        answer = []
        while p1 < len(firstList) and p2 < len(secondList):
            start1, end1 = firstList[p1]
            start2, end2 = secondList[p2]
            
            if start1 < start2:
                minStart = start1
                maxStart = start2
            else:
                minStart = start2
                maxStart = start1
                
            if end1 < end2:
                minEnd = end1
                maxEnd = end2
                p1 += 1
            else:
                minEnd = end2
                maxEnd = end1
                p2 += 1
            
            if maxStart <= minEnd:
                answer.append([maxStart, minEnd])
                
        return answer
    
# Time: O(M+N)
# Space: O(1) if you don't count the return O(M+N) if you count the return