from collections import defaultdict
import bisect 
class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.store[key]
        if not values:
            return ""
        # 1,2,4,5,6
        #     L
        #     R
        #     M
        L = 0
        R = len(values) - 1
        maxTimeValue = (float('-inf'), None)
        while L <= R:
            mid = (L + R) // 2
            if values[mid][0] == timestamp:
                return values[mid][1]
            if values[mid][0] > timestamp:
                R = mid - 1
            else: # values[mid][0] < timestamp
                maxTimeValue = max([maxTimeValue, values[mid]], key=lambda tup: tup[0])
                L = mid + 1
        
        return maxTimeValue[1] if maxTimeValue[1] != None else ""
               

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)