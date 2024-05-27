class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counts = collections.Counter(arr)
        bucket = [[] for _ in range(len(arr)+1)]
        for num, count in counts.items():
            bucket[count].append(num)
        
        sorted_arr = []
        for i in range(len(bucket)-1,0,-1):
            lst = bucket[i]
            for item in lst:
                sorted_arr.extend([item]*i)
        while k:
            sorted_arr.pop()
            k -= 1
            
        return len(set(sorted_arr))
        