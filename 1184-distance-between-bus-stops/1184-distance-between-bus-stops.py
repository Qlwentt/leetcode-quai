class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, end: int) -> int:
    
        if start == end:
            return 0
    
        if start < end:
            right = distance[start:end]
            left = distance[:start]+distance[end:]
            return min(sum(right), sum(left))
        else:
            left = distance[end:start]
            right = distance[:end] + distance[start:]
            return min(sum(right), sum(left))
        
        
        
        