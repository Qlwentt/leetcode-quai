class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        averages = [((clazz[0]/clazz[1]), i) for i, clazz in enumerate(classes)]
        newAvgs = [(((clazz[0]+ 1)/(clazz[1]+ 1)), i) for i, clazz in enumerate(classes)]
        diffs = [(-(newAvg[0]-avg[0]), i) for i, (avg, newAvg) in enumerate(zip(averages,newAvgs))]
        heapq.heapify(diffs)
        while extraStudents:
            maxDiff, maxIndex = heapq.heappop(diffs)
            classes[maxIndex] = [(classes[maxIndex][0]+1), (classes[maxIndex][1]+1)]
            averages[maxIndex] = ((classes[maxIndex][0])/(classes[maxIndex][1]), maxIndex)
            extraStudents -= 1
            newPotential = (classes[maxIndex][0]+1)/(classes[maxIndex][1]+1)
            heapq.heappush(diffs,(-(newPotential-averages[maxIndex][0]), maxIndex))
        return sum([avg for avg, i in averages]) / len(averages)
        
        