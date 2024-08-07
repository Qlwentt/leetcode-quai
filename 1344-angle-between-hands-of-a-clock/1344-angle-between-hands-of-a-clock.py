class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        
        hours_position = (hour%12) /12 + ((minutes/60) * 1/12)
        minutes_position = minutes/60
        
        distance = abs(hours_position-minutes_position) * 360
        
        return min(distance, 360-distance)
        
        
        
        
        