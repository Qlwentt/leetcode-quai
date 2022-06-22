class TimeMap:

    def __init__(self):
        self.storage = {}                 
                                          

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.storage:
            self.storage[key].append((timestamp, value))
        else:
            self.storage[key] = [(timestamp,value)]
    def get(self, key: str, timestamp: int) -> str:
        if not key in self.storage:
            return ""
        tuples = self.storage[key]
        
        foundIndex = self._modifiedBinarySearch(tuples,timestamp)
        if foundIndex == -1:
            return ""
        else:
            return tuples[foundIndex][1]

    def _modifiedBinarySearch(self,arr, target):
        l = 0
        r = len(arr) - 1
        res = -1
        while l <= r:
            mid = l + (r - l) // 2
            if target >= arr[mid][0]:
                res = mid
                l = mid + 1
            elif target < arr[mid][0]:
                r = mid - 1
        return res  
