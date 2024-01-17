from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        freq = [[] for _ in range(max(counter.values())+1)]
     #   {1:3, 2:2, 3:1}
     #   [[], [3], [2], [1]]
       #   0.  1.  2. 3
    
        for item, count in counter.items():
            freq[count].append(item)
        answer = []    
        for i in range(len(freq)-1,0,-1):
            for item in freq[i]:
                answer.append(item)
                k -= 1
                if k == 0:
                    return answer
        return answer