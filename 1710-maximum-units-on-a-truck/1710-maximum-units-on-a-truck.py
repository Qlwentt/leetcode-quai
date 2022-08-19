class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = [(-numUnits, -numBoxes) for numBoxes, numUnits in boxTypes]
        heapq.heapify(boxTypes)
        
        totalUnits = 0
        while boxTypes and truckSize:
            numUnits, numBoxes = heapq.heappop(boxTypes)
            numUnits = -numUnits
            numBoxes = -numBoxes
            if numBoxes <= truckSize:
                totalUnits += numUnits * numBoxes
                truckSize -= numBoxes
            else:
                numBoxes -= 1
                heapq.heappush(boxTypes, (-numUnits, -numBoxes))
        return totalUnits