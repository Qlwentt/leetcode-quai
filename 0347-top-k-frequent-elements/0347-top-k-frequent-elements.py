from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        bucket = [[] for i in range(max(counter.values())+1)]
        
        for num, count in counter.items():
            bucket[count].append(num)
            
        # [[][3][2][1]]
        #   0 1  2  3
        answer = []
        for i in range(len(bucket)-1,0,-1):
            for item in bucket[i]:
                if k:
                    answer.append(item)
                    k -= 1
        return answer