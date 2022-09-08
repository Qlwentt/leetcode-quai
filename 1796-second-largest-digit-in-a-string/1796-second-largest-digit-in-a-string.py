class Solution:
    def secondHighest(self, s: str) -> int:
        digitsMaxHeap = list(set([-int(digit) for digit in s if digit.isdigit()]))
        heapq.heapify(digitsMaxHeap)
        if digitsMaxHeap:
            heapq.heappop(digitsMaxHeap)
        
        return -digitsMaxHeap[0] if digitsMaxHeap else -1
            
            
        